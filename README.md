# OpenModels MCP Server Registry

A community-maintained registry of MCP (Model Context Protocol) servers — structured, searchable, and integrated with the [OpenModels](https://openmodels.run) ecosystem.

## Stats

| Metric | Count |
|--------|-------|
| Servers | 207 |
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
│   ├── arxiv.yaml
│   ├── aws-docs.yaml
│   ├── brave-search.yaml
│   ├── cloudflare.yaml
│   ├── context7.yaml
│   ├── docker.yaml
│   ├── elasticsearch.yaml
│   ├── exa.yaml
│   ├── expo.yaml
│   ├── fetch.yaml
│   ├── figma.yaml
│   ├── firecrawl.yaml
│   ├── filesystem.yaml
│   ├── git.yaml
│   ├── github.yaml
│   ├── grafana.yaml
│   ├── huggingface.yaml
│   ├── jira.yaml
│   ├── jupyter.yaml
│   ├── kubernetes.yaml
│   ├── linear.yaml
│   ├── memory.yaml
│   ├── mongodb.yaml
│   ├── neon.yaml
│   ├── notion.yaml
│   ├── perplexity.yaml
│   ├── playwright.yaml
│   ├── postgres.yaml
│   ├── puppeteer.yaml
│   ├── qdrant.yaml
│   ├── redis.yaml
│   ├── sentry.yaml
│   ├── sequential-thinking.yaml
│   ├── slack.yaml
│   ├── sqlite.yaml
│   ├── stripe.yaml
│   ├── supabase.yaml
│   ├── tavily.yaml
│   ├── time.yaml
│   ├── vercel.yaml
│   ├── vscode.yaml
│   ├── xcode.yaml
│   ├── aws.yaml
│   ├── terraform.yaml
│   ├── anthropic.yaml
│   ├── openai.yaml
│   ├── datadog.yaml
│   ├── posthog.yaml
│   ├── resend.yaml
│   ├── twilio.yaml
│   ├── clickhouse.yaml
│   └── chromadb.yaml
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
└── VERSION                  # Current version (1.9.0)
```

## Quick Start

### Browse servers

Visit [openmodels.run/mcp](https://openmodels.run/mcp) to search, filter, and compare MCP servers with a web UI.

Or explore the YAML files directly in the [`servers/`](servers/) directory.

### Install a server

Each server detail page at `openmodels.run/mcp/{server-id}` includes an **Install MCP server** button that copies the install command to your clipboard and provides IDE-specific configuration snippets.

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
repository: https://github.com/github/github-mcp-server
transport:
  - stdio
  - http-streaming
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
  npm: "@github/github-mcp-server"
  command: docker
  args: ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"]
env_vars:
  - name: GITHUB_PERSONAL_ACCESS_TOKEN
    description: GitHub personal access token for API authentication
    required: true
license: MIT
version: "1.0.5"
stars: 30200
created_at: "2024-11-25T00:00:00.000Z"
updated_at: "2026-05-21T00:00:00.000Z"
```

## Selected servers

The table below highlights representative entries. See the [`servers/`](servers/) directory for
the complete 207-server registry.

| Server | Category | Author | Transport |
|--------|----------|--------|-----------|
| [ArXiv](servers/arxiv.yaml) | Research | Joe Blazick | stdio, http-streaming |
| [AWS Docs](servers/aws-docs.yaml) | Development | AWS Labs | stdio |
| [Brave Search](servers/brave-search.yaml) | Research | Brave | stdio |
| [Cloudflare](servers/cloudflare.yaml) | Cloud | Cloudflare | stdio |
| [Context7](servers/context7.yaml) | Development | Upstash | stdio, http-streaming |
| [Docker](servers/docker.yaml) | DevOps | Docker | stdio |
| [Elasticsearch](servers/elasticsearch.yaml) | Database | Elastic | stdio, http-streaming |
| [Exa](servers/exa.yaml) | Research | Exa Labs | stdio |
| [Expo](servers/expo.yaml) | Development | Expo | stdio, http-streaming |
| [Fetch](servers/fetch.yaml) | Development | Anthropic | stdio |
| [Figma](servers/figma.yaml) | Development | Figma | stdio, http-streaming |
| [Firecrawl](servers/firecrawl.yaml) | Research | Mendable | stdio |
| [Filesystem](servers/filesystem.yaml) | Filesystem | Anthropic | stdio |
| [Git](servers/git.yaml) | Development | Anthropic | stdio |
| [GitHub](servers/github.yaml) | Development | GitHub | stdio, http-streaming |
| [Grafana](servers/grafana.yaml) | DevOps | Grafana Labs | stdio, sse |
| [Hugging Face](servers/huggingface.yaml) | AI | Hugging Face | stdio, http-streaming |
| [Jira (Atlassian)](servers/jira.yaml) | Productivity | Atlassian | stdio, http-streaming |
| [Jupyter](servers/jupyter.yaml) | Development | Datalayer | stdio |
| [Kubernetes](servers/kubernetes.yaml) | DevOps | Marc Nuri | stdio, http-streaming |
| [Linear](servers/linear.yaml) | Productivity | Linear | stdio |
| [Memory](servers/memory.yaml) | AI | Anthropic | stdio |
| [MongoDB](servers/mongodb.yaml) | Database | MongoDB | stdio, http-streaming |
| [Neon](servers/neon.yaml) | Database | Neon | stdio |
| [Notion](servers/notion.yaml) | Productivity | Notion | stdio |
| [Perplexity](servers/perplexity.yaml) | Research | Perplexity AI | stdio, http-streaming |
| [Playwright](servers/playwright.yaml) | Browser Automation | Microsoft | stdio |
| [PostgreSQL](servers/postgres.yaml) | Database | Anthropic | stdio |
| [Puppeteer](servers/puppeteer.yaml) | Browser Automation | Anthropic | stdio |
| [Qdrant](servers/qdrant.yaml) | Database | Qdrant | stdio, sse, http-streaming |
| [Redis](servers/redis.yaml) | Database | Anthropic | stdio |
| [Sentry](servers/sentry.yaml) | DevOps | Sentry | stdio |
| [Sequential Thinking](servers/sequential-thinking.yaml) | AI | Anthropic | stdio |
| [Slack](servers/slack.yaml) | Communication | Anthropic | stdio |
| [SQLite](servers/sqlite.yaml) | Database | Anthropic | stdio |
| [Stripe](servers/stripe.yaml) | Development | Stripe | stdio |
| [Supabase](servers/supabase.yaml) | Database | Supabase | stdio |
| [Tavily](servers/tavily.yaml) | Research | Tavily | stdio |
| [Time](servers/time.yaml) | Productivity | Anthropic | stdio |
| [Vercel](servers/vercel.yaml) | DevOps | Vercel | stdio, http-streaming |
| [VSCode](servers/vscode.yaml) | Development | acomagu | stdio |
| [Xcode](servers/xcode.yaml) | Development | Apple | stdio |
| [AWS](servers/aws.yaml) | Cloud | AWS Labs | stdio |
| [Anthropic](servers/anthropic.yaml) | AI | Anthropic | stdio |
| [ChromaDB](servers/chromadb.yaml) | Database | Chroma | stdio |
| [ClickHouse](servers/clickhouse.yaml) | Database | ClickHouse | stdio |
| [Datadog](servers/datadog.yaml) | DevOps | Datadog | stdio |
| [OpenAI](servers/openai.yaml) | AI | OpenAI | stdio |
| [PostHog](servers/posthog.yaml) | Productivity | PostHog | stdio |
| [Resend](servers/resend.yaml) | Communication | Resend | stdio |
| [Terraform](servers/terraform.yaml) | Cloud | HashiCorp | stdio |
| [Twilio](servers/twilio.yaml) | Communication | Twilio | stdio |

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
- **Install button** — one-click copy of install commands on each server detail page

## License

MIT
