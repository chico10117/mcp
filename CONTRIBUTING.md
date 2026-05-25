# Contributing to OpenModels MCP Registry

Thanks for contributing! This guide covers how to add new MCP servers to the registry.

## Adding a New MCP Server

### 1. Create the YAML file

Copy the template and create `servers/{server-id}.yaml` where `{server-id}` matches the `id` field inside the file.

```bash
cp servers/_template.yaml servers/my-server.yaml
```

**Naming conventions:**
- Use kebab-case: lowercase alphanumeric with hyphens
- Pattern: `^[a-z0-9]+(-[a-z0-9]+)*$`
- Maximum 128 characters
- Be descriptive but concise (e.g., `github`, `brave-search`, not `gh` or `bs`)
- Filename must match the `id` field exactly

### 2. Fill in required fields

Every MCP server definition must include:

| Field | Description |
|-------|-------------|
| `id` | Unique kebab-case identifier (must match filename) |
| `name` | Human-readable display name (max 255 chars) |
| `description` | What the server does and when to use it (10-2000 chars) |
| `author` | Object with `name` (required) and `github` (required) |
| `repository` | URL to the source code repository |
| `transport` | Array of supported protocols: `stdio`, `sse`, `http-streaming` |
| `category` | One of the 11 categories (see below) |
| `tags` | 1-20 searchable tags in kebab-case (max 64 chars each) |
| `created_at` | ISO 8601 timestamp (e.g., `"2025-06-01T00:00:00.000Z"`) |
| `updated_at` | ISO 8601 timestamp |

### 3. Add tools, resources, and prompts

These are optional but highly recommended — they're what makes your server discoverable:

**Tools** (max 200 per server):
```yaml
tools:
  - name: tool_name              # Max 128 chars
    description: What it does    # Max 1000 chars
    input_schema:
      type: object
      properties:
        param:
          type: string
          description: Parameter description
      required:
        - param
```

**Resources** (max 100 per server):
```yaml
resources:
  - uri_template: "file:///{path}"   # Max 2048 chars
    description: What it provides    # Max 1000 chars
```

**Prompts** (max 100 per server):
```yaml
prompts:
  - name: prompt_name            # Max 128 chars
    description: What it does    # Max 1000 chars
    arguments:
      - name: arg_name           # Max 128 chars
        description: Arg desc    # Max 500 chars
```

### 4. Optional fields

| Field | Description |
|-------|-------------|
| `install` | Installation config (`npm`, `command`, `args`) |
| `env_vars` | Environment variables needed (`name`, `description`, `required`) |
| `license` | SPDX license identifier (e.g., `MIT`, `Apache-2.0`) |
| `version` | Current version of the MCP server |
| `stars` | GitHub star count (updated periodically by maintainers) |

### 5. Validate locally

```bash
pip install -r requirements.txt
python validate.py
```

Validation checks:
- YAML syntax is valid
- All required fields are present and correctly typed
- Schema constraints are met (string lengths, patterns, enums)
- Filename matches the `id` field
- No duplicate IDs across all server definitions

### 6. Submit a pull request

1. **Fork** this repository
2. **Create** your server YAML file in `servers/`
3. **Validate** locally with `python validate.py`
4. **Commit** with a descriptive message (e.g., `Add my-server MCP server definition`)
5. **Open a PR** with a brief description of the server's purpose

## Submission Workflow

```
Fork repo → Create YAML → Validate locally → Open PR → CI validates → Review → Merge
```

### What happens after you open a PR:

1. **Automated validation** — GitHub Actions runs `validate.py` on your PR. If validation fails, a comment is posted with the specific errors.
2. **Review** — A maintainer reviews the submission for quality and accuracy.
3. **Merge** — Once validation passes and a maintainer approves, the PR is merged.
4. **Ingestion** — On the next deployment, your server is ingested into the platform and appears on [openmodels.run/mcp](https://openmodels.run/mcp).

## Review Process

Maintainers check for:

- **Accuracy** — does the server actually exist and work as described?
- **Completeness** — are tools, resources, and prompts documented?
- **Quality** — are descriptions clear and helpful?
- **No duplicates** — is this server already in the registry under a different ID?
- **Valid repository** — does the repository URL point to a real, accessible project?

## Categories

Choose the most appropriate category for your server:

| Category | Description |
|----------|-------------|
| Development | Code generation, testing, debugging, and software development tools |
| Productivity | Task management, note-taking, workflow automation |
| Database | Database querying, schema management, and data manipulation |
| DevOps | CI/CD, infrastructure management, monitoring |
| AI | Machine learning, model management, and AI utilities |
| Research | Web search, knowledge retrieval, and information gathering |
| Browser Automation | Web scraping, browser control, and automated testing |
| Communication | Messaging, email, notifications, and collaboration |
| Filesystem | File operations, directory management, and local storage |
| Cloud | Cloud provider APIs, serverless functions, and cloud storage |
| Security | Authentication, encryption, and vulnerability scanning |

## YAML Format Reference

See the full schema at [`schemas/server.schema.json`](schemas/server.schema.json) and the annotated template at [`servers/_template.yaml`](servers/_template.yaml).

Key constraints:
- `id`: kebab-case, max 128 chars, must match filename
- `name`: 1-255 chars
- `description`: 10-2000 chars
- `transport`: array of 1-3 values from `stdio`, `sse`, `http-streaming`
- `tags`: 1-20 kebab-case strings, each max 64 chars
- `tools`: max 200 entries
- `resources`: max 100 entries
- `prompts`: max 100 entries
- Timestamps: ISO 8601 format (`YYYY-MM-DDTHH:MM:SS.sssZ`)

## Tips for Good Submissions

- **Be specific** in descriptions — explain what problems the server solves
- **Document all tools** — users discover servers by their tool capabilities
- **Include install config** — makes it easy for users to get started
- **List environment variables** — users need to know what credentials are required
- **Use accurate tags** — they power search and discovery
- **One server per PR** — easier to review and faster to merge

## Code of Conduct

Be respectful, constructive, and inclusive. We're building a community resource.
