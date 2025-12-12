# Style Guide

## File Naming

| Type         | Pattern                           | Examples                                         |
| ------------ | --------------------------------- | ------------------------------------------------ |
| Agent        | `{gem-name}.agent.yaml`           | `user-testing.agent.yaml`                        |
| Package      | `{gem-name}.package.yaml`         | `refinement.package.yaml`                        |
| Instructions | `{workflow-name}.instructions.md` | `refine.instructions.md`, `help.instructions.md` |
| Templates    | `{template-name}.template.md`     | `ticket.template.md`                             |
| Data         | `{name}.csv`                      | `users.csv`, `knowledge-base.csv`                |

Directories: kebab-case (lowercase with hyphens).

**Note:** These patterns cover common file types. You can add other files as needed. Follow the same naming convention: `{name}.{type}.md/yaml/etc`. Agents reference only what they explicitly declare in `dependencies:`. (See ARCHITECTURE.md for directory structure and gem organization.)

---

## Variables

Variables use the `_{{ }}_` syntax. The agent parses these to dynamically inject and reference content during runtime.

**⚠️ Important:** Variable names should use hyphens (kebab-case), not underscores. Underscores in variable names break styling. Use `_{{ ticket-title }}_` not `_{{ ticket_title }}_`.

**File references:**

- _{{ filename.extension }}_ — Reference entire file
- _{{ filename.extension | field }}_ — Reference specific field
- _{{ filename.extension | field.[variable] }}_ — Dynamic field access

**Examples:**

```
_{{ users.gsheet }}_
_{{ users.gsheet | personas }}_
_{{ package.yaml | release-notes.[version] }}_
```

---

## Package Metadata (`.package.yaml`)

Package metadata defines gem versioning and release information. Every gem requires this file.

```yaml
id: '{gem-name}-agent'
version: '{semver}'
release-date: '{MM-DD-YYYY}'
release-notes:
  version: '{version}'
  date: '{MM-DD-YYYY}'
  added:
    - 'Description'
```

This metadata is used by agents to reference gem version and release notes via variables like `_{{ package.yaml | version }}_`.

---

## Agent Definition (`.agent.yaml`)

```yaml
agent:
  metadata:
    name: {optional}
    title: {required}
    icon: {emoji}

  persona:
    identity: >
      {multi-line description of role and purpose}

    principles:
      - {principle 1}
      - {principle 2}

  dependencies:
    instructions:
      - {name}.instructions.gdoc
    templates:
      - {name}.template.gdoc
    data:
      - {name}.gsheet

  menu:
    - trigger: /{command}
      workflow: {name}.instructions.gdoc
      description: {concise user-facing description}
```

---

## Instruction Files (`.instructions.md`)

**Standard Structure**

```md
# {Title}

## Overview

{Brief description}

---

## {Section}

{content with numbered steps if applicable}

---

## {Section}

{content}
```

**Stepwise Workflows (Elicitation Pattern)**

For workflows that guide users through multi-step processes (especially collaborative ones), use this structure for each step:

```md
### Step {N}: {Title}

**Actions:**

- {What the agent does}

**Response to User:**
{What the agent says/asks}

**Wait for confirmation before proceeding to the next step.**

**Template Output Variables:** _{{ variable_names }}_
```

This pattern works well for workflows that require structured elicitation, proposal, and feedback cycles. See refinement gem's `refine.instructions.md` for a complete example.

### Help Instructions (`help.instructions.md`)

Every gem should include a help workflow. This is a recommended structure:

```md
# {Gem Name} - Help

## Available Commands

- **`/{command}`** — {Description}
- **`/{command}`** — {Description}
- **`/help`** — View this help message

---

## How to Use

### {Workflow Name}

{Step-by-step explanation}

> 💡 **Tip:** {Helpful guidance}

---

## {Additional Context}

{Information about gem capabilities, personas, data, or concepts}

_{{ reference.to.knowledge.files }}_

**Additional Resources:** See [Helpful Documentation](https://example.com/docs) for more information.

---

## Gem Information

**Version:** _{{ package.yaml | version }}_

**Recent Updates:**

_{{ package.yaml | release-notes.[version] }}_
```

This pattern ensures users always know what commands are available, how to use them, and can reference gem metadata and knowledge files.

---

## Template Files (`.template.md`)

Templates define structured output formats that agents populate with variables during workflow execution.

**Structure:**

```md
# _{{ variable-name }}_

**Label:** _{{ variable-name }}_

## Section

_{{ variable-name }}_

## Another Section

_{{ variable-name }}_
```

---

## Data Files

Structured data files (CSV format) that agents reference in workflows.

**CSV format:**

- Header row with column names
- Fields comma-separated
- Complex text in quotes
- Multi-value fields separated by semicolons; always quote cells containing multiple values

**Example:**

```csv
name,age,occupation,personality_type,traits
Sarah,34,PM,ENFJ,"Organized; Detail-oriented"
```

---

## Workflow Triggers

Slash commands in `menu:` section:

```yaml
menu:
  - trigger: /{kebab-case-action}
    workflow: {name}.instructions.gdoc
    description: {User-facing description}
```

**Patterns:**

- Always include `/help`
- Action-oriented names
- One-line descriptions

---

## Markdown Formatting

- `**bold**` for emphasis
- `` `/command` `` for slash commands
- `_{{ variable }}_` for file references
- `---` for major breaks
- `> 💡 **Note:**` for tips/callouts
- Numbered lists for steps, bullets for non-sequential items
- Headings: H1 title, H2 sections, H3 subsections

**Approved emojis:**

These emojis are whitelisted and preserved during the deployment script's stopgap word removal:

- ⚠️ Warnings and cautions
- ✅ Dos and completed items
- ❌ Don'ts and errors
- 💡 Tips and ideas
- 🎉 Successes and milestones
- 📝 Notes and documentation
- 🔧 Tools and configuration
- 🚀 Launches and deployments
- ✨ New features and enhancements
- 📋 Checklists and tasks
- 🔍 Search and investigation
- ⭐ Highlights and favorites

---

## File Type References

**When writing gems:**

- Write files as standard formats (`.md`, `.yaml`, `.csv`)
- Reference them in code/config using Google types (`.gdoc`, `.gsheet`)
- Deployment converts source files to Google Suite format

**File mapping:**

- `.md` sources → `.gdoc` references
- `.csv` sources → `.gsheet` references
- `.yaml` sources → `.gdoc` or `.yaml` references (varies by context)
