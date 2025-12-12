## Overview

We make **gems** and **prompts**.

## Gems

### Architecture

**Key components:**

- **agent/** - Contains the agent definition
- **core/** - Houses gem content: `instructions/`, `data/`, `templates/`, and other directories as needed
- **package** - Metadata and version information
- **README** - Optional documentation

### File Type References

When working with gem files, you'll notice references to `.gdoc` and `.gsheet` file types:

- **Gems are deployed to Google Drive**, so they're referenced using Google file types (`.gdoc`, `.gsheet`)
- **Source files are standard formats** (`.md`, `.yaml`, `.csv`, etc.)
- **File references in code** use the Google Drive naming convention, even though the actual files are written in standard formats

### Style Guide

#### Variables

Variables are used to pass information throughout gem files. Follow these formatting guidelines:

- **Wrap variables in underscore and double curly braces:** _{{ variable }}_
- **Use pipes (`|`) to extract specific information:** _{{ file.gdoc | property }}_
- **Use object notation to access nested properties:** _{{ file.gdoc | object.property }}_ or _{{ file.gdoc | array.[index] }}_

**Examples:**

- _{{ users.gsheet | personas }}_ - Extract personas from users.gsheet
- _{{ user-testing.package.yaml | version }}_ - Get version from package
- _{{ user-testing.package.yaml | release-notes.[version] }}_ - Access nested array property
