# Changelog

All notable changes to the OpenModels MCP Server Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-06-01

### Added
- Initial MCP Server Registry structure
- JSON Schema (Draft 7) for server definitions at `schemas/server.schema.json`
- Python validation script (`validate.py`) with schema validation, duplicate ID detection, and filename matching
- Category definitions (11 categories: Development, Productivity, Database, DevOps, AI, Research, Browser Automation, Communication, Filesystem, Cloud, Security)
- Server template at `servers/_template.yaml` with all fields documented
- 10 seed server definitions: filesystem, github, postgres, puppeteer, fetch, memory, slack, aws-docs, sequential-thinking, brave-search
- GitHub Actions CI workflow for automated PR validation
- CONTRIBUTING.md with submission workflow and YAML format documentation
- MIT license
