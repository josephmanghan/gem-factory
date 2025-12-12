# Gemini Gems Platform Overview

## What is a Gemini Gem?

A Gemini Gem is a customized version of Google's Gemini AI model, tailored for specific use cases through system instructions and knowledge files. Gems allow users to create specialized AI assistants with domain-specific expertise and behavior.

## Core Gem Capabilities

A Gemini Gem can be customized to have:

- **Personality and Role:** Define who the Gem is and how it presents itself
- **Response Style:** Control tone, format, and communication approach
- **Boundaries and Constraints:** Set operational limits and rules
- **Workflows and Procedures:** Establish task-handling processes and instructions
- **Domain Knowledge:** Provide specialized information beyond general training data
- **Instructions and Guidance:** Include procedural steps, checklists, and frameworks

## Configuration Architecture

Gems are configured through **two distinct spaces**. Both spaces can contain any of the capabilities above - the distinction is architectural, not functional.

### System Instructions Space

A dedicated input field for defining Gem configuration. Typically used for core personality, role definition, and high-level behavioral guidelines, but can contain any type of instruction or information.

### Knowledge Files Space

A file-based configuration space supporting up to 10 files.

**Key Characteristics:**

- **Maximum:** 10 files per Gem
- **Sources:** Direct upload or Google Suite connection (Drive, Docs, Sheets)
- **Auto-updates:** Suite-connected files sync automatically; uploads require manual updates
- **Searchable:** When queried, the Gem searches knowledge files first for relevant information
- **File Format:** All knowledge files must be Google Suite files (`.gdoc`, `.gsheet`, `.gslide`, etc.). While source files in this repository use conventions like `.md`, `.yaml` and `.csv`, deployed Gem knowledge files are exclusively Google Suite files.

**Purpose:** Provides a structured way to include extensive domain-specific content, reference material, instructions, and data. Knowledge files act as the Gem's private knowledge base, enabling it to answer questions about specialized, proprietary, or niche topics by referencing uploaded content rather than relying solely on general training data.

**Example:** A "Company Handbook Assistant" Gem with uploaded policy documents, org charts, and process guides can answer "What's our parental leave policy?" by referencing specific uploaded HR documents.

## Model Options

Gems support two Gemini model variants:

- **Gemini 3 Pro:** Higher intelligence, deeper reasoning, better for complex solutioning and expertise. Limited usage quota.
- **Gemini Flash:** Faster responses, lighter reasoning. Higher usage limits. Better for quick tasks and high-volume interactions.

### Integration

- Google Suite native integration (Drive, Docs, Sheets)
- Automatic synchronization of connected knowledge files
- Seamless access within Gemini interface

## Platform Constraints

1. **Knowledge File Limit:** Maximum 10 files per Gem
2. **File Sources:** Google Suite or direct uploads only
3. **Update Mechanism:** Manual for uploads, automatic for Suite-connected files

## How Gems Work

1. **Configuration:** User defines system instruction + selects up to 10 knowledge files
2. **Contextualization:** Gem uses system instruction to shape behavior + knowledge files for domain expertise
3. **Runtime:** User interacts with Gem through standard Gemini interface
4. **Maintenance:** Knowledge files from Google Suite auto-update; system instructions require manual updates. This enables centralized management where a single maintainer can update shared Gems, and all consumers automatically receive the latest knowledge without any additional configuration.

## Reference Documentation

- [Gemini Gems Overview](https://gemini.google/overview/gems/)
- [Creating and Using Gems](https://support.google.com/gemini/answer/15146780)
