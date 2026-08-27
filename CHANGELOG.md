# Changelog

All notable changes to the OpenModels MCP Server Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.10.0] - 2026-08-27
### Added
- `modelscope` — ModelScope's official server for model, dataset, Studio, paper, and MCP discovery plus supported image-generation workflows. The entry uses the published `uvx modelscope-mcp-server` stdio installation and also records the server's self-hosted HTTP/SSE transports.
### Changed
- Total MCP servers: 208 (from 207).

## [1.9.0] - 2026-08-22
### Added
- `jupyter` — notebook discovery, cell editing, code execution, and multimodal output for Jupyter and JupyterHub.
### Changed
- Total MCP servers: 207 (from 206).

## [1.8.0] - 2026-08-03
### Added
- 11 new AI-focused MCP servers, expanding the `AI` category from 10 to 21 entries:
  - **Inference & local models**: `groq` (official Groq — fast completions, vision, speech, batch) and `ollama` (local open-weight model management with a model advisor).
  - **Evaluation & observability**: `wandb` (official W&B Models + Weave), `opik` (official Comet), `confident-ai` (official, the platform behind DeepEval), and `arize-phoenix` (official Arize, remote MCP over OpenTelemetry traces).
  - **Retrieval**: `llamacloud` (official LlamaIndex — managed indexes and document extraction).
  - **Agent memory**: `mem0` (persistent semantic memory, optional Neo4j graph) and `letta` (stateful MemGPT-style agents and memory blocks).
  - **Generative media**: `fal` (fal.ai image/video/audio generation) and `comfyui` (local ComfyUI workflow control).
- Total MCP servers: 206 (from 195).

## [1.7.0] - 2026-07-28
### Changed
- **`anthropic`** — updated for the MCP 2026-07-28 spec release: stateless request/response core (serverless and edge deployable), versioned extensions framework covering MCP Apps and Tasks, and authorization hardened for production OAuth 2.0 / OIDC providers such as Entra and Okta. Added `http-streaming` transport, bumped to v2.0.0, and re-dated the entry so it surfaces as newly released.
### Added
- 8 new MCP servers from official vendors and maintained projects:
  - `quickbooks` (Intuit official) and `consul` (HashiCorp official) for accounting and service mesh / service discovery.
  - `nomad` for workload orchestration and `keycloak` for identity and user management.
  - `strapi`, `ghost`, and `woocommerce` for headless CMS, publishing, and ecommerce operations.
  - `mobile-mcp` for iOS/Android device automation and mobile QA.
- Total MCP servers: 195 (from 187).

## [1.6.0] - 2026-07-25
### Added
- 10 new MCP servers from established vendors and maintained open-source projects:
  - `mapbox` (geospatial: geocoding, routing, maps), `opensearch`, `cockroachdb`, `oracle-database`, and `kafka` for search, SQL, and event-streaming data access.
  - `trivy` (Aqua Security vulnerability/misconfig/secret scanning) and `grafana-tempo` (distributed tracing) for security and observability.
  - `apple-mcp`, `square`, and `spotify` for macOS-native productivity, commerce, and music/playback.
### Changed
- Total MCP servers: 187 (from 177).

## [1.5.0] - 2026-07-21
### Added
- 2 MCP servers on the theme of the latest Gemini Flash releases:
  - `google-mcp-security` — Google's official security MCP servers (SecOps, Threat Intelligence, Security Command Center) for agent-driven investigation and vulnerability triage.
  - `gemini-cli` — MCP server that delegates large-context analysis to the Google Gemini CLI.

## [1.4.0] - 2026-07-15

### Added

- 15 MCP servers from established organizations and maintained open-source platforms:
  - `mcp-toolbox`, `influxdb3`, `openbb`, and `mindsdb` for databases, financial research, and AI data workflows.
  - `octopus-deploy`, `prefect-mcp`, and `dagster-mcp` for delivery and workflow orchestration.
  - `agentmail`, `atlassian-mcp`, and `markitdown` for communication, collaboration, and document conversion.
  - `mcp-everything` and `mcp-context-forge` for protocol testing, MCP governance, and gateway controls.
  - `payload-mcp`, `directus-mcp`, and `medusa-mcp` for content, data, and commerce operations.

### Changed

- Total server count: 175 (from 160).

## [1.3.0] - 2026-07-15

### Added

- 15 new MCP server definitions from established vendors and open-source projects:
  - `chrome-devtools-mcp` — Chrome DevTools browser inspection, debugging, network, and performance workflows (Browser Automation)
  - `jetbrains-mcp` — JetBrains IDE and Android Studio development integration (Development)
  - `microsoft-learn-mcp` — trusted Microsoft Learn documentation and code samples (Research)
  - `firebase-mcp` — Firebase project context and development workflows (Cloud)
  - `buildkite` — CI/CD pipelines, builds, jobs, and artifacts (DevOps)
  - `growthbook` — feature flags, experiments, and metrics (Productivity)
  - `harness` — software delivery pipelines, services, environments, and insights (DevOps)
  - `apache-doris` — Doris analytics database schema and query workflows (Database)
  - `apache-iotdb` — IoT time-series data and telemetry exploration (Database)
  - `apache-skywalking` — tracing, service topology, metrics, and incident investigation (DevOps)
  - `apache-solr` — search collections, schema discovery, and relevance investigation (Database)
  - `jfrog` — artifact repositories, build information, and supply-chain workflows (DevOps)
  - `fivetran` — managed ELT connector and sync-health investigation (Database)
  - `cloud-run-mcp` — Google Cloud Run deployment and serverless service management (Cloud)
  - `google-ads-mcp` — Google Ads API resources and campaign operations (Productivity)

### Changed

- Total server count now 160 across categories (from 145)

## [1.2.0] - 2026-07-12

### Added

- 15 new MCP server definitions across 8 categories:
  - `couchbase` — Couchbase cluster access with SQL++ (N1QL) queries and document operations (Database)
  - `astra-db` — official DataStax Astra DB serverless Cassandra with vector search (Database)
  - `tinybird` — official Tinybird real-time analytics workspace queries and endpoints (Database)
  - `metabase` — Metabase built-in BI server, permission-scoped database queries and dashboards (Database)
  - `confluent` — official Confluent/Apache Kafka topics, connectors, Schema Registry, and Flink SQL (DevOps)
  - `honeycomb` — Honeycomb observability queries across events, traces, and boards (DevOps)
  - `dynatrace` — official Dynatrace problems, vulnerabilities, and DQL over logs/metrics/traces (DevOps)
  - `contentful` — official Contentful CMS content, models, and asset management (Development)
  - `sanity` — official Sanity CMS GROQ queries, document writes, and schema tools (Development)
  - `wordpress` — Automattic's remote WordPress server for posts, pages, and media (Productivity)
  - `n8n` — popular n8n workflow node knowledge, validation, and workflow management (Productivity)
  - `webflow` — official Webflow sites, CMS collections, and publishing via the Data API (Cloud)
  - `google-analytics` — official Google Analytics 4 reporting and metadata discovery (Research)
  - `zoom` — official Zoom remote server for meeting search, recordings, and Docs (Communication)
  - `infisical` — official Infisical secret management with machine-identity auth (Security)

### Changed

- Total server count now 145 across categories

## [1.1.0] - 2026-07-12

### Added

- 18 new MCP server definitions across 9 categories:
  - `prisma` — official Prisma ORM and Prisma Postgres schema/migration management (Database)
  - `motherduck` — official DuckDB and MotherDuck SQL analytics over local and cloud data (Database)
  - `meilisearch` — official Meilisearch index management and full-text search (Database)
  - `prometheus` — query and analyze Prometheus metrics with PromQL (DevOps)
  - `pulumi` — official Pulumi AI-assisted Infrastructure as Code (DevOps)
  - `azure-devops` — official Microsoft Azure DevOps work items, repos, and pipelines (DevOps)
  - `postman` — official Postman workspaces, collections, and API workflows (Development)
  - `apollo-graphql` — official Apollo server exposing GraphQL operations as MCP tools (Development)
  - `unity` — Coplay's MCP bridge for AI-driven Unity Editor game development (Development)
  - `duckduckgo` — privacy-friendly DuckDuckGo web search and content fetching (Research)
  - `algolia` — official Algolia search, index settings, and analytics (Research)
  - `kagi` — official Kagi search and Universal Summarizer tools (Research)
  - `browserstack` — official BrowserStack cross-browser and device testing (Browser Automation)
  - `whatsapp` — local-first WhatsApp message search and sending via the web multi-device API (Communication)
  - `excel` — read/write Excel workbooks, formulas, and charts without Excel installed (Productivity)
  - `auth0` — official Auth0 Management API for apps, Actions, and tenant logs (Security)
  - `render` — official Render service deploys, logs, and managed databases (Cloud)
  - `cloudinary` — official Cloudinary media upload, transformation, and asset management (Cloud)

### Changed

- Total server count now 130 across categories

## [1.0.0] - 2026-07-09

### Added

- 20 new MCP server definitions:
  - `duckdb` — DuckDB in-process analytical SQL over local files (Database)
  - `neo4j` — official Neo4j graph database with Cypher queries (Database)
  - `dbt` — official dbt Labs analytics engineering and Semantic Layer (Database)
  - `replicate` — Replicate hosted ML models for generative media and inference (AI)
  - `elevenlabs` — official ElevenLabs text-to-speech, voice, and transcription (AI)
  - `wolfram-alpha` — Wolfram Alpha computational knowledge and math (Research)
  - `reddit` — Reddit search, posts, and comment threads for research (Research)
  - `hackernews` — Hacker News stories, comments, and trends (Research)
  - `netlify` — official Netlify site deploys and build logs (DevOps)
  - `launchdarkly` — official LaunchDarkly feature flags and targeting (DevOps)
  - `railway` — Railway project and service deployment management (Cloud)
  - `digitalocean` — official DigitalOcean App Platform and infrastructure (Cloud)
  - `google-sheets` — read/write Google Sheets ranges and tabs (Productivity)
  - `obsidian` — Obsidian vault notes via Local REST API (Productivity)
  - `dropbox` — official Dropbox file storage and sharing (Filesystem)
  - `box` — official Box enterprise content management with Box AI (Filesystem)
  - `zendesk` — Zendesk Support tickets and replies (Communication)
  - `intercom` — Intercom conversations and contacts (Communication)
  - `paypal` — official PayPal orders, invoices, and refunds (Development)
  - `plaid` — official Plaid banking, balances, and transactions (Development)

### Changed

- Total server count now 112 across categories

## [0.9.0] - 2026-07-09

### Added

- 15 new MCP server definitions:
  - `weaviate` — Weaviate vector database for semantic and hybrid search (Database)
  - `milvus` — official Milvus vector database for similarity search (Database)
  - `databricks` — Databricks lakehouse SQL, Unity Catalog, and jobs (Database)
  - `pagerduty` — official PagerDuty incident management and on-call (DevOps)
  - `jenkins` — Jenkins CI/CD builds, jobs, and console logs (DevOps)
  - `circleci` — official CircleCI pipeline status and failure logs (DevOps)
  - `langfuse` — Langfuse LLM observability and prompt management (AI)
  - `clickup` — ClickUp tasks, spaces, and lists (Productivity)
  - `monday` — official monday.com Work OS boards and items (Productivity)
  - `google-maps` — Google Maps geocoding, places, and directions (Productivity)
  - `browserbase` — official Browserbase cloud browser automation with Stagehand (Browser Automation)
  - `vault` — HashiCorp Vault secrets management (Security)
  - `semgrep` — official Semgrep SAST scanning (Security)
  - `telegram` — Telegram Bot API messaging and notifications (Communication)
  - `wikipedia` — Wikipedia search and article retrieval for research (Research)

### Changed

- Total server count now 92 across categories

## [0.8.0] - 2026-06-24

### Added

- 10 new MCP server definitions:
  - `bitbucket` — Atlassian Bitbucket repositories, pull requests, and pipelines (Development)
  - `sonarqube` — official SonarQube code quality and security analysis (Development)
  - `mysql` — MySQL/MariaDB schema inspection and SQL queries (Database)
  - `trello` — Trello boards, lists, and cards (Productivity)
  - `confluence` — Atlassian Confluence wiki search and page management (Productivity)
  - `todoist` — Todoist task management (Productivity)
  - `google-calendar` — Google Calendar events and scheduling (Productivity)
  - `gmail` — Gmail read, search, draft, and send (Communication)
  - `apify` — official Apify Actors for web scraping and automation (Browser Automation)
  - `heroku` — official Heroku Platform app and dyno management (Cloud)

### Changed

- Total server count now 77 across categories

## [0.7.0] - 2026-06-19

### Added

- 10 new MCP server definitions:
  - `gitlab` — official GitLab MCP server for projects, issues, merge requests, and CI/CD pipelines (Development)
  - `airtable` — Airtable MCP server for reading/writing records, bases, and schemas (Database)
  - `snowflake` — official Snowflake MCP server for SQL queries and Cortex AI over the Data Cloud (Database)
  - `bigquery` — Google BigQuery MCP server for dataset exploration and SQL analytics with dry-run costing (Database)
  - `asana` — official Asana MCP server for tasks, projects, and work management (Productivity)
  - `salesforce` — Salesforce MCP server for SOQL queries, CRM records, and Apex execution (Productivity)
  - `hubspot` — official HubSpot MCP server for CRM contacts, companies, and deals (Productivity)
  - `zapier` — official Zapier MCP server exposing thousands of app actions and automations (Productivity)
  - `snyk` — official Snyk MCP server for code, dependency, container, and IaC security scanning (Security)
  - `youtube-transcript` — YouTube transcript and metadata MCP server for video summarization and research (Research)

### Changed

- Total server count now 67 across 11 categories

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
