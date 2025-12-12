# Quill - Refinement Workflow Agent Help

## Available Commands

- **`/refine`** — Refine ticket through structured workflow
- **`/help`** — View this help message

---

## Helpful Tools to Prepare Your Inputs

### [code2prompt](https://code2prompt.dev/docs/tutorials/getting_started/)

Generate code assets from your repository to provide context for refinement.

### [tree](https://www.npmjs.com/package/tree-node-cli)

Generate your source tree structure to help the agent understand the codebase organization.

### Task Split Workflow

For advanced ticket decomposition, consider breaking the refined ticket into discrete tasks using
your agent:

**Prompt 1: Generate Task Breakdown for Review**

```md
Analyze `@{ticket}` and propose a high-level breakdown into discrete tasks. Present this as a simple
numbered list of tasks for review. After presenting the proposed breakdown, explicitly request user
feedback and refinements.
```

**Prompt 2: Create Task Files** (use after approving the breakdown)

```md
Split each task from the approved breakdown into separate Markdown files. Each file should contain
all details for that single task, including its title and all subtasks. Include a reference within
the files to `@{ticket}` so that broader context is understood. Use sequential filenames (e.g.,
01-[task-name].md, 02-[task-name].md) to allow for the planning and execution of individually
stop-gapped tasks.
```

This two-step approach enables discrete task execution where tasks are completed in turn. If an
investigation produces output, it can inform the next task without running all steps sequentially.

## Knowledge Base

This gem works with a knowledge base to provide domain-specific knowledge, expertise, patterns, and
best practices. The knowledge base is referenced during workflow execution to inform suggestions and
technical guidance.

If you'd like to customize or configure your knowledge base to better reflect your practices and
domain knowledge, consult the gem documentation or knowledge files for setup options.

---

## Gem Information

**Version:** _{{ refinement.package.yaml | version }}_

**Release:** _{{ refinement.package.yaml | release-notes.[version] }}_
