# Changelog

All notable changes to the OpenModels MCP Server Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
