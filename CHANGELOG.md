# Changelog

All notable changes to the OpenModels MCP Server Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] - 2026-06-12

### Added

- 6 new MCP server definitions:
  - `e2b` — E2B MCP server for running code in secure isolated cloud sandboxes (Development)
  - `pinecone` — official Pinecone Developer MCP server for vector search and RAG workflows (Database)
  - `azure` — official Microsoft Azure MCP server for Storage, Cosmos DB, Monitor/KQL, and Azure CLI (Cloud)
  - `shopify` — official Shopify Dev MCP server for docs search, GraphQL schema introspection, and Functions (Development)
  - `google-drive` — Google Drive MCP server for listing, searching, and reading Drive files via OAuth (Filesystem)
  - `discord` — Discord MCP server for sending and reading channel messages via a bot (Communication)

### Changed

- Total server count now 57 across 11 categories

## [0.5.0] - 2026-06-04

### Added

- 10 new MCP server definitions:
  - `aws` — AWS MCP server for S3, Lambda, DynamoDB, and CloudWatch access (Cloud)
  - `terraform` — HashiCorp Terraform MCP server for plan, validate, state inspection, and module discovery (Cloud)
  - `anthropic` — official Anthropic MCP server for Claude model invocation within agentic workflows (AI)
  - `openai` — official OpenAI MCP server for GPT, DALL-E, Whisper, and embeddings (AI)
  - `datadog` — Datadog MCP server for metrics, logs, traces, and monitor management (DevOps)
  - `posthog` — PostHog MCP server for product analytics, funnels, and feature flags (Productivity)
  - `resend` — Resend MCP server for transactional email delivery and template management (Communication)
  - `twilio` — Twilio MCP server for SMS, voice calls, and phone number lookup (Communication)
  - `clickhouse` — ClickHouse MCP server for OLAP analytics and query profiling (Database)
  - `chromadb` — ChromaDB MCP server for vector search and RAG workflows (Database)

### Changed

- Total server count now 51 across 11 categories

## [0.4.1] - 2026-05-31

### Added

- 5 new MCP server definitions:
  - `elasticsearch` — official Elastic MCP server for natural language queries against Elasticsearch 8.x/9.x clusters, index management, and document indexing via Docker (Database)
  - `kubernetes` — native Go Kubernetes/OpenShift MCP server with direct API access, pod exec/logs, Helm, Tekton, and multi-cluster support — no kubectl wrapper (DevOps)
  - `jira` — official Atlassian Rovo MCP server for Jira, Confluence, and Compass via OAuth 2.1 or API token; remote HTTP-streaming at mcp.atlassian.com (Productivity)
  - `huggingface` — official Hugging Face MCP server for model/dataset/paper search, Hub inference, and Gradio Spaces; remote endpoint at huggingface.co/mcp (AI)
  - `vscode` — VSCode-as-MCP-server extension exposing editor, terminal, diagnostics, debug sessions, and URL preview to external AI agents (Development)

### Fixed

- `figma` — corrected repository URL from `figma/figma-mcp` to `figma/mcp-server-guide`

### Changed

- Total server count now 41 across 11 categories

## [0.4.0] - 2026-05-27

### Added
- 4 new MCP server definitions:
  - `expo` — official Expo MCP server for React Native development, EAS builds/workflows, TestFlight crashes, documentation, and visual automation (Development)
  - `vercel` — official Vercel MCP server for deployment management, project configuration, logs, and documentation search (DevOps)
  - `figma` — official Figma MCP server for design-to-code workflows, screenshots, design system search, Code Connect, and file creation (Development)
  - `xcode` — official Apple Xcode MCP server (xcrun mcpbridge) with 20 native IDE tools for building, testing, previewing, code editing, and documentation search (Development)
- Total server count now 36 across 11 categories

## [0.3.0] - 2026-05-26

### Added
- 9 new MCP server definitions:
  - `tavily` — AI-optimized web search for RAG, news search, content extraction (Research)
  - `firecrawl` — web scraping and crawling to clean markdown, sitemap extraction (Research)
  - `grafana` — Prometheus/Loki queries, dashboards, alerts for observability (DevOps)
  - `stripe` — payments, customers, subscriptions, refunds via Stripe API (Development)
  - `neon` — serverless PostgreSQL with instant branching, SQL queries (Database)
  - `arxiv` — arXiv paper search, download, reading, citation graphs (Research)
  - `qdrant` — vector search, semantic memory, RAG with FastEmbed (Database)
  - `mongodb` — MongoDB/Atlas queries, aggregations, schema inspection, cluster management (Database)
  - `perplexity` — official Perplexity AI search, deep research, reasoning with Sonar models (Research)
- Total server count now 32 across 11 categories

## [0.2.0] - 2026-05-25

### Added
- 12 new MCP server definitions: playwright, context7, linear, notion, docker, sentry, supabase, sqlite, redis, exa, cloudflare, time, git
- "Install MCP server" button on server detail pages with copy-to-clipboard and dropdown options
- Server comparison feature with auto-scroll to comparison table
- Total server count now 23 across 9 categories

## [0.1.0] - 2026-05-25

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
