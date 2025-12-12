# Gem Factory Architecture

## Overview

Gem Factory is a monorepo development environment for building Gemini gems. It provides complete tooling infrastructure, standards, and example gems in a single workspace where developers can build and deploy their own gems.

## Repository Structure

```
gem-factory/
├── gems/                   # Gem packages
│   ├── basic-gem/         # Starter example (ships with repo)
│   │   ├── internal/      # Gem code (deployed)
│   │   ├── README.md      # Gem documentation
│   │   └── CHANGELOG.md   # Version history
│   └── advanced-gem/      # Advanced example (ships with repo)
│       ├── internal/
│       ├── README.md
│       └── CHANGELOG.md
├── docs/                   # Documentation
│   ├── style-guide.md     # Coding and architectural standards
│   ├── platform-guide.md  # Gemini platform overview
│   └── architecture.md    # Technical stack and patterns
├── scripts/                # Tooling and automation
│   ├── deployment-handler.sh
│   └── tools/
├── deploy/                 # Build output (generated)
│   ├── basic-gem/
│   └── advanced-gem/
├── AGENTS.md              # AI/agent context and instructions
├── package.json           # Scripts, dependencies, tooling
├── eslint.config.mjs      # Code quality standards
└── prettier.config.mjs    # Code formatting rules
```

## Design Philosophy

### Monorepo Development Environment

This repository IS the workspace - not just documentation or templates. Developers:

1. Clone gem-factory
2. Study the example gems in `gems/`
3. Create new gems directly in `gems/`
4. Use included tooling for building and deploying
5. Benefit from shared standards and infrastructure

### Unified Build System

All gems in `gems/` are treated uniformly:

- Same deployment process
- Same code quality standards
- Same formatting rules
- Same tooling access

The deployment script processes any gem in `gems/`:

```bash
npm run deploy:target -- my-gem
```

### Infrastructure as Product

The value isn't just the example gems - it's the complete environment:

- Pre-configured linting and formatting
- Deployment automation
- Documentation and style guides
- AI-ready context (AGENTS.md)
- Extensible scripting infrastructure

## Developer Workflow

### Getting Started

1. Clone the repository
2. Run `npm install`
3. Explore the example gems in `gems/`
4. Read documentation in `docs/`

### Creating a New Gem

1. Create a new directory in `gems/my-new-gem/`
2. Create `gems/my-new-gem/internal/` for gem code
3. Add `gems/my-new-gem/README.md` for documentation
4. Follow patterns from example gems
5. Reference style guide in `docs/`
6. Use deployment script to build

### Building and Deploying

```bash
# List available gems
npm run deploy:target

# Deploy a specific gem
npm run deploy:target -- my-gem

# Run code quality checks
npm run check

# Fix formatting and linting
npm run fix
```

## Key Architectural Decisions

### Directory Structure: `gems/gem-name/internal/`

**Top-level `gems/` directory:**

- Follows monorepo conventions (similar to `packages/`, `apps/`, `libs/`)
- Domain-specific naming makes purpose immediately clear
- Standard approach in Turborepo, Lerna, and Nx monorepos

**Per-gem `internal/` directory:**

- Follows Go's established convention for implementation code
- Clear separation: `internal/` = deployed, everything else = local only
- Enables flexibility (README, CHANGELOG, notes stay local, only `internal/` gets deployed)
- Simple deployment logic: copy `gems/gem-name/internal/` → `deploy/gem-name/`

### Why Monorepo Instead of Separate Examples?

- Single source of truth for tooling and standards
- Examples remain in sync with infrastructure
- Users have everything they need in one place
- Easier to maintain consistency
- Deploy script works uniformly across all gems

### Why Ship with Example Gems?

The example gems serve multiple purposes:

- Demonstrate best practices
- Provide starting points for new gems
- Validate that the tooling works
- Show different complexity levels

## Future Extensibility

### Planned Enhancements

1. **Gem Generation Prompts**: AI-powered templates and scaffolding
2. **Additional Examples**: More gems demonstrating various patterns
3. **Enhanced Tooling**: Additional scripts for testing, validation, etc.
4. **Interactive Guides**: Tutorials and walkthroughs in documentation

### Design for Growth

The architecture supports expansion without structural changes:

- Add new gems to `gems/` following the standard structure
- Add new scripts to `scripts/` for automation
- Add new documentation to `docs/`
- Extend AGENTS.md with additional context

All additions work within the existing deployment and tooling infrastructure.

## Gem Structure

Each gem in `gems/` follows a standard package structure:

```
gems/gem-name/
├── internal/          # Gem code (deployed)
│   ├── agent/
│   ├── core/
│   └── *.yaml
├── README.md          # Gem documentation
├── CHANGELOG.md       # Version history (optional)
```

**Key principle:**

- Everything in `internal/` gets deployed
- Everything at gem root stays local
- This allows gems to have documentation, notes, and other artifacts without affecting deployment

## Standards and Tooling

### Code Quality

- ESLint for code standards
- Prettier for formatting
- CSV validation for data files
- Pre-commit hooks (planned)

### Deployment Pipeline

1. Caveman processing (context optimization)
2. Web bundle generation
3. YAML to Markdown conversion
4. Automated formatting

### Documentation

- AGENTS.md for AI/agent context
- Style guides for consistency
- Platform documentation for reference
- Architecture documentation (this file)

## Principles

1. **Convention over Configuration**: Follow industry standards
2. **Complete over Minimal**: Provide full working environment
3. **Consistent over Flexible**: Uniform treatment of all gems
4. **Iterative over Perfect**: Build and refine over time
5. **Professional over Casual**: Production-quality infrastructure
