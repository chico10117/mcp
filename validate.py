#!/usr/bin/env python3
"""
MCP Server Registry Validation Script
Usage:
    python validate.py
"""

import sys
import json
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from jsonschema import Draft7Validator, FormatChecker


@dataclass
class ValidationError:
    """Represents a validation error for a specific field"""
    field: str
    message: str
    expected: str
    actual: str


@dataclass
class ValidationResult:
    """Result of validating a single file"""
    valid: bool
    errors: List[ValidationError] = field(default_factory=list)


@dataclass
class ValidationReport:
    """Complete validation report for the MCP server registry"""
    success: bool
    total_files: int = 0
    valid_files: int = 0
    invalid_files: int = 0
    errors: Dict[str, List[ValidationError]] = field(default_factory=dict)
    duplicate_ids: List[str] = field(default_factory=list)
    filename_errors: List[str] = field(default_factory=list)


class McpValidator:
    """Validates YAML files in the OpenModels MCP server registry"""

    def __init__(self, registry_path: Optional[Path] = None):
        self.registry_path = registry_path or Path(__file__).parent
        self.schemas_path = self.registry_path / 'schemas'
        self.servers_path = self.registry_path / 'servers'

        self.server_schema = self._load_schema('server.schema.json')

        self.server_validator = Draft7Validator(
            self.server_schema,
            format_checker=FormatChecker()
        )

    def _load_schema(self, schema_filename: str) -> Dict[str, Any]:
        """Load a JSON schema from file"""
        schema_path = self.schemas_path / schema_filename
        if not schema_path.exists():
            raise FileNotFoundError(f"Schema not found: {schema_path}")

        with open(schema_path, 'r') as f:
            return json.load(f)

    def _json_pointer_path(self, path) -> str:
        """Convert jsonschema error path to JSON pointer format (e.g., /tools/0/name)"""
        if not path:
            return '/'
        return '/' + '/'.join(str(p) for p in path)

    def check_yaml_syntax(self, file_path: Path) -> Optional[str]:
        """
        Check if a YAML file has valid syntax.

        Returns:
            None if valid, error message string if invalid.
        """
        try:
            with open(file_path, 'r') as f:
                yaml.safe_load(f)
            return None
        except yaml.YAMLError as e:
            return f"YAML parse error: {e}"
        except Exception as e:
            return f"Error reading file: {e}"

    def check_schema(self, file_path: Path) -> ValidationResult:
        """Validate a YAML file against the MCP server JSON schema"""
        syntax_error = self.check_yaml_syntax(file_path)
        if syntax_error:
            return ValidationResult(
                valid=False,
                errors=[ValidationError(
                    field='/',
                    message=syntax_error,
                    expected='valid YAML',
                    actual='parse error'
                )]
            )

        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
        except Exception as e:
            return ValidationResult(
                valid=False,
                errors=[ValidationError(
                    field='/',
                    message=str(e),
                    expected='valid YAML',
                    actual='parse error'
                )]
            )

        errors = []
        for error in self.server_validator.iter_errors(data):
            field_path = self._json_pointer_path(error.absolute_path)

            expected = 'valid value'
            if error.validator == 'type':
                expected = f"type: {error.validator_value}"
            elif error.validator == 'enum':
                expected = f"one of: {', '.join(str(v) for v in error.validator_value)}"
            elif error.validator == 'required':
                missing_prop = error.message.split("'")[1] if "'" in error.message else 'unknown'
                expected = f"required field: {missing_prop}"
                # Point to the parent object where the field is missing
                field_path = self._json_pointer_path(error.absolute_path) + '/' + missing_prop if error.absolute_path else '/' + missing_prop
            elif error.validator == 'pattern':
                expected = f"pattern: {error.validator_value}"
            elif error.validator in ('minimum', 'maximum', 'minLength', 'maxLength', 'minItems', 'maxItems'):
                expected = f"{error.validator}: {error.validator_value}"
            elif error.validator == 'format':
                expected = f"format: {error.validator_value}"
            elif error.validator == 'additionalProperties':
                expected = 'no additional properties'
            elif error.validator == 'uniqueItems':
                expected = 'unique items'

            # Determine actual value
            actual = 'invalid value'
            if error.instance is not None:
                if isinstance(error.instance, (dict, list)):
                    actual = f"type: {'array' if isinstance(error.instance, list) else 'object'}"
                else:
                    actual = str(error.instance)[:100]

            errors.append(ValidationError(
                field=field_path,
                message=error.message,
                expected=expected,
                actual=actual
            ))

        return ValidationResult(valid=len(errors) == 0, errors=errors)

    def check_filename_id_match(self, file_path: Path) -> Optional[str]:
        """
        Verify that filename matches the id field inside.

        Returns:
            None if match, error message string if mismatch.
        """
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
                if data and 'id' in data:
                    expected_filename = f"{data['id']}.yaml"
                    if file_path.name != expected_filename:
                        return (
                            f"Filename mismatch: file is '{file_path.name}' but id field is '{data['id']}' "
                            f"(expected filename: {expected_filename})"
                        )
        except Exception:
            pass  # YAML errors are caught elsewhere
        return None

    def check_duplicate_ids(self) -> List[str]:
        """
        Find duplicate server IDs across all files.
        Reports both conflicting files for each duplicate.

        Returns:
            List of duplicate ID error messages.
        """
        duplicates = []
        server_ids: Dict[str, Path] = {}

        if not self.servers_path.exists():
            return duplicates

        for yaml_file in sorted(self.servers_path.glob('*.yaml')):
            if yaml_file.name == '_template.yaml':
                continue

            try:
                with open(yaml_file, 'r') as f:
                    data = yaml.safe_load(f)
                    if data and 'id' in data:
                        server_id = data['id']
                        if server_id in server_ids:
                            duplicates.append(
                                f"Duplicate ID '{server_id}': found in "
                                f"{server_ids[server_id].name} and {yaml_file.name}"
                            )
                        else:
                            server_ids[server_id] = yaml_file
            except Exception:
                pass  # YAML errors are caught elsewhere

        return duplicates

    def validate_all(self) -> ValidationReport:
        """Validate all MCP server YAML files in the registry"""
        report = ValidationReport(success=True)

        if not self.servers_path.exists():
            print("  Warning: servers/ directory not found")
            return report

        yaml_files = sorted(self.servers_path.glob('*.yaml'))
        server_files = [f for f in yaml_files if f.name != '_template.yaml']

        for yaml_file in server_files:
            report.total_files += 1

            result = self.check_schema(yaml_file)
            if result.valid:
                report.valid_files += 1
            else:
                report.invalid_files += 1
                report.success = False
                report.errors[str(yaml_file)] = result.errors

            filename_error = self.check_filename_id_match(yaml_file)
            if filename_error:
                report.filename_errors.append(filename_error)
                report.success = False

        report.duplicate_ids = self.check_duplicate_ids()
        if report.duplicate_ids:
            report.success = False

        return report


def format_report(report: ValidationReport) -> str:
    """Format validation report for terminal output"""
    lines = []

    if report.success:
        lines.append("✅ Validation Passed")
        lines.append(f"\n  Validated {report.total_files} files successfully.")
    else:
        lines.append("❌ Validation Failed")
        lines.append(f"\n  Summary: {report.invalid_files} of {report.total_files} files failed validation.")

        if report.errors:
            lines.append("\n  Schema Validation Errors:")
            lines.append("  " + "-" * 50)
            for file_path, errors in report.errors.items():
                lines.append(f"\n  📄 {file_path}")
                for error in errors:
                    lines.append(f"    • {error.field}: {error.message}")
                    lines.append(f"      Expected: {error.expected}")
                    lines.append(f"      Actual:   {error.actual}")

        if report.duplicate_ids:
            lines.append("\n  Duplicate ID Errors:")
            lines.append("  " + "-" * 50)
            for duplicate in report.duplicate_ids:
                lines.append(f"    • {duplicate}")

        if report.filename_errors:
            lines.append("\n  Filename Mismatch Errors:")
            lines.append("  " + "-" * 50)
            for error in report.filename_errors:
                lines.append(f"    • {error}")

    return "\n".join(lines)


def main():
    """Main entry point"""
    print("OpenModels MCP Server Registry Validator")
    print("=" * 50)

    try:
        validator = McpValidator()
    except (json.JSONDecodeError, ValueError) as e:
        print(f"\n❌ Error: Malformed schema file — {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

    print("Validating MCP server registry...")
    report = validator.validate_all()

    print("\n" + format_report(report))

    sys.exit(0 if report.success else 1)


if __name__ == '__main__':
    main()
