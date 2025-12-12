# Gem Architecture

## Overview

This architecture describes how gems in Gem Factory are structured and organized. It defines the component model we use, how they relate to each other, and the reasoning behind each design decision.

## Core Requirements

Every gem requires two files:

### Agent Definition

The agent definition is what the Gemini platform reads to instantiate the gem. It declares:

- **Metadata** — Name, title, icon
- **Persona** — Identity statement and guiding principles
- **Dependencies** — Explicit list of which instructions, templates, and data files are active
- **Menu** — Slash commands that trigger workflows

### Package Metadata

The package file defines gem versioning and release information. It includes version, release date, and release notes.

## Recommended Components

Beyond the agent definition, this architecture advocates for three additional components organized in the gem's `core/` directory. These can be used as best befits the complexity and requirements of the gem.

### Instructions

Instruction files define workflows—the procedures, decision trees, and multi-step processes that guide the gem's behavior. They range from simple help documentation to complex collaborative workflows with structured elicitation steps.

Instructions are written in Markdown and can include:

- Step-by-step procedures
- Decision logic
- Prompts and response patterns
- References to templates and data

### Templates

Templates are structured formats for consistent output. They define the shape of deliverables—proposal formats, ticket templates, report structures, etc.

Templates are written in Markdown and can include:

- Sections and fields
- Examples
- Variable placeholders for dynamic content

### Data

Data files provide factual information, reference materials, and structured knowledge. Common use cases include user personas, knowledge bases, configuration tables, and domain-specific datasets.

Data is stored as CSV and can be referenced by other files.

## Dependency Model

The agent definition declares all available knowledge files through its `dependencies:` section. Dependencies are declaratively itemized with labels identifying what each file does—instructions, templates, data.

All declared files are loaded when the gem initializes. There is no lazy loading. This means the gem's performance depends directly on what you include. Keep dependencies focused on what the gem actually uses.

The explicit, labeled declaration gives the gem clarity about its own composition. The gem understands immediately what instructions, templates, and data it has available.

## Directory Structure

Each gem follows a standardized directory layout:

```
gems/gem-name/
├── README.md              # Local documentation (not deployed)
├── CHANGELOG.md           # Version history (not deployed)
└── internal/              # Deployed gem code
    ├── agent/
    │   └── {gem-name}.agent.yaml
    ├── core/
    │   ├── instructions/
    │   ├── templates/
    │   ├── data/
    │   └── {custom directories as needed}
    └── {gem-name}.package.yaml
```

### Platform Alignment

The directory structure directly supports the Gemini platform's two configuration spaces:

- **System instructions** ← Agent definition
- **Knowledge files** ← Core instructions, templates and data

### Fixed Structure: `agent/` at `internal/` Root

The `agent/` directory exists at the top level of `internal/` due to alphabetical ordering. The deployment script relies on it existing at the top in order to generate the web bundle.

```
internal/
├── agent/               ← Must be here
│   └── {gem-name}.agent.yaml
└── core/
```

### Flexible Structure: `core/` Subdirectories

Everything else lives under `core/`. The standard structure includes:

- `core/instructions/` — Workflow definition files
- `core/templates/` — Output template files
- `core/data/` — CSV data files

You can add additional directories to `core/` as needed for organization:

```
core/
├── instructions/
├── templates/
├── data/
├── reference/          ← Custom directory (example)
├── schemas/            ← Custom directory (example)
└── {other}/
```

All files must follow kebab-case naming conventions: `{name}.{type}.md/yaml/csv`.
