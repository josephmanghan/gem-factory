# Gem Factory

A development environment for creating and deploying Gemini Gems with deep reasoning and sophisticated instruction architectures.

## Why Gems?

Recent Gemini updates represent a marked advancement in reasoning ability and processing power. The **2 million token context window** of the Gemini Web UI is large enough to include extensive code, comprehensive documentation, and rich contextual information—without the context management friction of IDEs (limited to ~200k tokens).

Critically, the Web UI is accessible to everyone—product managers, designers, non-technical stakeholders—not locked to engineers. This democratization, combined with Gemini's cost-effectiveness relative to token usage, makes Gems a niche but compelling vehicle for exploring AI agent potential across diverse teams and skill levels.

Gems can be easily maintained and shared with collaborators. When you connect knowledge files from Google Drive, they receive automatic updates—no need to recreate or redistribute. This enables sustainable, iterative development where both users and dependent gems automatically receive improvements.

The purpose of this repository is to provide an environment for developing Gems that unlock Gemini's reasoning potential through thoughtful, well-architected system instructions and knowledge organization.

## Requirements

- **Access to Gemini** - You'll need access to the Gemini Web UI to create and deploy Gems
- **Access to Google Drive** - Knowledge files must be stored in Google Drive to enable automatic updates
- **npm** - Required to install dependencies and run validation scripts
- **Python** - Required if you want to use the deployment scripts (for caveman processing and YAML conversion)

## Working with Agents

This repository is structured to be compatible with agentic IDEs that follow the [AGENTS.md specification](https://agents.md/), now recognised as a standard by the [Linux Foundation](https://tinyurl.com/37kdev8t). The [AGENTS.md](./AGENTS.md) file supports agents in contributing to this repo.

For complete architectural and style guidelines that both agents and humans should follow when creating gems, see [docs/index.md](./docs/index.md). For an overview of the Gemini Gems platform itself, see [docs/platform-overview.md](./docs/platform-overview.md).

## Repository Structure

```
gems/                      # Individual gem directories
  {gem-name}/             # Each gem follows the standard structure
    internal/             # Core gem components
      agent/              # Agent definition (system instructions)
      core/               # Instructions, templates, and data

docs/                      # Documentation
  index.md                # Entry point with links to all documentation

scripts/                   # Deployment and automation scripts
deploy/                    # Generated deployment artifacts
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

1. **Converts YAML to Markdown** - Your `{gem-name}.agent.yaml` definitions are converted to Markdown for easier Gemini UI pasting
2. **Optimizes Context** - Removes filler words and unnecessary markup (caveman processing) to reduce token usage while preserving reasoning ability and meaning
3. **Generates Web Bundle** - Creates a portable `.md` file containing your complete gem definition

The web bundle is particularly valuable for quick testing and sharing—you can copy-paste it directly into any AI chat interface (Gemini, ChatGPT, Claude, etc.) without needing to create a formal Gem first.

## Getting Started: Setting Up a Gem

### Step 1: Prepare Your Files in Google Drive

1. **For Markdown files** - You can either:
   - Copy and paste your `.md` content directly into a Google Doc, or
   - Drag your `.md` files into Google Drive, open them (they render as Google Docs), then delete the original files

2. **For CSV files** - Create a Google Sheet and import your CSV (don't drag CSV files directly—Gemini interprets them incorrectly)

You can edit CSVs either in your local IDE or directly in Google Sheets. Both approaches work equally well.

> **Note** - It should also be possible to make use of an MCP to write directly to Drive.

### Step 2: Create Your Gem

1. Go to the [Gems app](https://gemini.google.com/gems/view) and click **New Gem**
2. Enter a name and description

> **Note** - If your Gem included a help command, it's recommended to add the description "use /help to get started" so that a user immediately knows how to get started when they load a fresh Gem.

3. Copy your `{gem-name}.agent.yaml` content and paste it into the **System instructions** pane
4. Click the **+** button next to **Knowledge**
5. Add up to 10 knowledge files from Google Drive (this is important—adding from Drive enables automatic updates)

### Step 3: Share

Click **Share** and distribute your Gem. All users will automatically receive updates to any Google Drive-connected knowledge files without needing new links or redistributions.

## Key Advantages of This Approach

- **Automatic Updates**: Knowledge files connected from Google Drive sync automatically. Update once, all users get the new version for free.
- **Minimal Configuration Changes**: The architecture is designed to require minimal iteration on system instructions. Most improvements happen through knowledge file updates.
- **Performance-Conscious**: While Gemini's reasoning capacity is very high and this architecture allows for considerable complexity, bear in mind that adding more initialization data will impact performance, and past a certain point, will likely impact reliability as well.
