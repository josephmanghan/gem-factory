# Gem Factory

A development environment for creating and deploying Gemini Gems with deep reasoning and sophisticated instruction patterns.

This repository provides tools and structure for developing Gems that unlock Gemini's reasoning potential through a thoughtful, well-architected system and knowledge organization.

## Why Gems?

Recent Gemini updates represent a marked advancement in reasoning ability and processing power. The **2 million token context window** of the Gemini Web UI is large enough to include extensive code, comprehensive documentation, and rich contextual information — without the context management friction of IDEs (limited to ~200k tokens). That's a significant difference, and it opens up possibilities for relatively sophisticated agent architectures.

More importantly, the Web UI is accessible to everyone — product managers, designers, non-technical stakeholders — not locked to engineers. This democratization is what makes Gems genuinely interesting: we can all exist in the same ecosystem, using the same tools, with the same level of power. Combined with Gemini's cost-effectiveness, this creates a niche but compelling case for Gems as a vehicle for AI agent development.

Gems can be easily maintained and shared with collaborators. When you connect knowledge files from Google Drive, they receive automatic updates — no need to recreate or redistribute. Update once, everyone gets it for free. This enables sustainable, iterative development where both users and dependent Gems automatically receive improvements without any friction.

The architecture is designed around this update pattern: minimal iteration on system instructions, with most improvements happening through knowledge file updates. This keeps Gems stable while remaining flexible.

## Quick Start

1. Clone the repository and install dependencies: `npm install`
2. Explore existing Gems in the `gems/` directory to understand the architecture
3. If using an agentic IDE/tool (like Cursor or Claude Code), agents will automatically leverage the [AGENTS.md](./AGENTS.md) file to help you create new Gems following project conventions
4. Run `npm run deploy:target {gem-name}` to prepare a gem for deployment
5. See [Getting Started](#getting-started-setting-up-a-gem) below for complete deployment instructions

## Requirements

- **Access to Gemini** - You'll need access to the Gemini Web UI to create and deploy Gems
- **Access to Google Drive** - Knowledge files must be stored in Google Drive to enable automatic updates
- **npm** - Required to install dependencies and run validation scripts
- **Python** - Required if you want to use the deployment scripts (for caveman processing and YAML conversion)

## Working with Agents

This repository is structured to be compatible with agentic IDEs that follow the [AGENTS.md specification](https://agents.md/), now recognised as a standard by the [Linux Foundation's Agentic AI Foundation](https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/). The [AGENTS.md](./AGENTS.md) file supports agents in contributing to this repo.

For complete architectural and style guidelines that both agents and humans should follow when creating gems, see [docs/index.md](./docs/index.md). For an overview of the Gemini Gems platform itself, see [docs/platform-overview.md](./docs/platform-overview.md).

## Examples

This repository includes two reference implementations:

- **[Refinement Gem](./gems/refinement/)** - Helps refine requirements and generate tickets
  - [Live Gem](https://gemini.google.com/gem/1yoZvdDaRLYp7oQUwX0NVvLy3falyKSp0) | [Refinement Drive Folder](https://drive.google.com/drive/folders/1eZqZ2hWnxFk5rIP7Gf0_gh-Qsjm2xaGe)
- **[User Research Gem](./gems/user-research/)** - Simulates personas for user research
  - [Live Gem](https://gemini.google.com/gem/1z_72jQ0Md9mT703Zxk-KqXdsd0mt3K_b) | [User Research Drive Folder](https://drive.google.com/drive/folders/1h39Jt069eYs7r-lgjo9PuSoCY79goUhG)

Explore these to understand the architecture in practice.

## Repository Structure

```
gems/                      # Individual gem directories
  {gem-name}/             # Each gem follows the standard structure
    internal/             # Core gem components (source files)
      agent/              # Agent definition (system instructions)
      core/               # Instructions, templates, and data
    README.md             # Gem-specific documentation
    CHANGELOG.md          # Version history

deploy/                    # Generated deployment artifacts (output)
  {gem-name}/             # Markdown versions ready for Gemini UI
  web-bundles/            # Portable single-file bundles

docs/                      # Project documentation
  index.md                # Entry point with links to all documentation

scripts/                   # Deployment and automation scripts
```

## Validation & Deployment

### Validation

Before deploying, validate your gem with:

```bash
npm run pr
```

This runs linting, CSV validation, and formatting checks to ensure your gem meets project standards.

### Deployment

Prepare a specific gem for deployment:

```bash
npm run deploy:target {gem-name}
```

The deployment script:

1. **Converts YAML to Markdown** - Your `{gem-name}.agent.yaml` definitions are converted to Markdown for easier pasting into the Gemini UI
2. **Optimizes Context** - Removes filler words and stopgap words (caveman processing) to reduce token count while preserving reasoning ability and meaning. While Gemini can handle extensive context, more initialization data impacts performance and reliability — optimization keeps gems responsive.
3. **Generates Web Bundle** - Creates a consolidated, portable `.md` file containing your complete gem definition

The web bundle is particularly valuable — you can copy-paste it directly into any AI chat interface (Gemini, ChatGPT, Claude, etc.) for quick testing and sharing, no formal Gem creation needed.

## Getting Started: Setting Up a Gem

### Step 1: Prepare Your Files in Google Drive

1. **For Markdown files** - You can either:
   - Copy and paste your `.md` content directly into a Google Doc, or
   - Drag your `.md` files into Google Drive, open them (they render as Google Docs), then delete the original files

2. **For CSV files** - Create a Google Sheet and import your CSV (don't drag CSV files directly — Gemini gets very confused by them)

You can edit CSVs either in your local IDE or directly in Google Sheets. Both approaches work equally well.

> **Note** - It should also be possible to make use of an MCP to write directly to Drive.

### Step 2: Create Your Gem

1. Go to the [Gems app](https://gemini.google.com/gems/view) and click **New Gem**
2. Enter a name and description

> **Note** - If your Gem included a help command, it's recommended to add the description "use /help to get started" so that a user immediately knows how to get started when they load a fresh Gem.

3. Copy your processed `{gem-name}.agent.md` content from the `deploy/` directory and paste it into the **System instructions** pane (or use the raw YAML from `internal/agent/{gem-name}.agent.yaml` if you haven't run deployment yet)

> **Tip** - In Google Docs, enable Markdown formatting (Tools > Preferences > Markdown) to easily paste and format Markdown content.

4. Click the **+** button next to **Knowledge**
5. Add up to 10 knowledge files from Google Drive (this is important — adding from Drive enables automatic updates)

### Step 3: Share

Click **Share** and distribute your Gem. All users will automatically receive updates to any Google Drive-connected knowledge files without needing new links or redistributions.
