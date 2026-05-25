# OpenModels MCP Server Registry

A community-maintained registry of MCP (Model Context Protocol) servers — structured, searchable, and integrated with the [OpenModels](https://openmodels.run) ecosystem.

## Stats

| Metric | Count |
|--------|-------|
| Servers | 10 |
| Categories | 11 |
| Transport types | 3 (stdio, sse, http-streaming) |

## What is this?

This registry catalogs MCP servers that extend AI agents with tools, resources, and prompts. Each server entry includes:

- **Description** — what the server does and what capabilities it exposes
- **Tools** — available tool definitions with input schemas
- **Resources & Prompts** — exposed resources and prompt templates
- **Install config** — how to install and run the server
- **Metadata** — category, tags, transport protocols, author, license

## Directory Structure

```
mcp/
├── servers/                 # One YAML file per MCP server
│   ├── _template.yaml      # Template for contributors
│   ├── aws-docs.yaml
│   ├── brave-search.yaml
│   ├── fetch.yaml
│   ├── filesystem.yaml
│   ├── github.yaml
│   ├── memory.yaml
│   ├── postgres.yaml
│   ├── puppeteer.yaml
│   ├── sequential-thinking.yaml
│   └── slack.yaml
├── categories/
│   └── categories.yaml     # Category definitions
├── schemas/
│   └── server.schema.json  # JSON Schema (Draft 7) for validation
├── validate.py             # Validation script
├── requirements.txt        # Python dependencies (PyYAML, jsonschema)
├── CONTRIBUTING.md          # Contribution guide
├── CHANGELOG.md             # Version history
├── LICENSE                  # MIT
├── README.md                # This file
└── VERSION                  # Current version (0.1.0)
```

## Quick Start

### Browse servers

Visit [openmodels.run/mcp](https://openmodels.run/mcp) to search, filter, and compare MCP servers with a web UI.

Or explore the YAML files directly in the [`servers/`](servers/) directory.

### Add a new server

1. Fork this repository
2. Copy `servers/_template.yaml` to `servers/{your-server-id}.yaml`
3. Fill in your server details (see [CONTRIBUTING.md](CONTRIBUTING.md))
4. Validate locally: `python validate.py`
5. Submit a pull request

## Server Format

Each server is a YAML file validated against a [JSON Schema](schemas/server.schema.json):

```yaml
id: github
name: GitHub MCP Server
description: >
  Provides access to the GitHub API through the Model Context Protocol...
author:
  name: GitHub
  github: github
repository: https://github.com/modelcontextprotocol/servers
transport:
  - stdio
category: Development
tags:
  - github
  - git
  - version-control
tools:
  - name: create_issue
    description: Create a new issue in a GitHub repository.
    input_schema:
      type: object
      properties:
        owner:
          type: string
        repo:
          type: string
        title:
          type: string
      required: [owner, repo, title]
install:
  npm: "@modelcontextprotocol/server-github"
  command: npx
  args: ["-y", "@modelcontextprotocol/server-github"]
env_vars:
  - name: GITHUB_PERSONAL_ACCESS_TOKEN
    description: GitHub personal access token for API authentication
    required: true
license: MIT
version: "0.6.2"
stars: 18500
created_at: "2024-11-25T00:00:00.000Z"
updated_at: "2025-06-01T00:00:00.000Z"
```

## Categories

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

## Validation

All server definitions are validated against JSON Schema on every PR:

```bash
pip install -r requirements.txt
python validate.py
```

Validation checks:
- YAML syntax
- Schema conformance (required fields, types, enums, patterns)
- No duplicate IDs across all server definitions
- Filename matches the `id` field

### CI Integration

A GitHub Actions workflow runs validation automatically on every pull request that modifies files in `servers/`, `schemas/`, or `validate.py`. PRs that fail validation cannot be merged.

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

**Quick steps:**

1. Fork this repository
2. Copy `servers/_template.yaml` and fill in your server details
3. Run validation: `python validate.py`
4. Submit a pull request

## Integration with OpenModels

MCP servers are ingested into the OpenModels platform and available via:

- **Web UI** — browse, filter, search, and compare at [openmodels.run/mcp](https://openmodels.run/mcp)
- **API** — query programmatically via `/api/v1/mcp/servers`
- **IDE configs** — generate connection snippets for Claude Code, Cursor, Windsurf, Gemini CLI, Kiro, and VS Code

## License

MIT
