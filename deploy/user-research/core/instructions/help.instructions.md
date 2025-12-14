==============================================

INSTRUCTION FOR AGENT: It is CRITICAL that you retain ALL codefence/codeblock formatting and provide
all HTTP links to the user.

==============================================

# User Testing Party - Help

## Available Commands

- **`/select-user`** — Choose a specific user persona to interact with
- **`/party-mode`** — Start multi-user user research discussion with all personas active
- **`/help`** — View this help message

---

## How to Use

### Select User Mode

1. Type **`/select-user`** to see available personas
2. Choose which user you want to speak to
3. Interact with that specific user consistently

> 💡 **Tip:** This mode is perfect for focused, one-on-one user research sessions.

### Party Mode

1. Type **`/party-mode`** to begin a group discussion
2. All personas will discuss in **round-robin format**
3. Each provides feedback from their perspective
4. Ends with individual verdicts

> 💡 **Tip:** Great for getting diverse perspectives in a single session!

---

## User Personas

The gem includes **diverse personas**:

_{{ users.gsheet | personas }}_

Each has different technical skills, communication styles, and accessibility needs.

---

## Gem Information

**Version:** _{{ user-research.package.gdoc | version }}_

**Recent Updates:**

_{{ user-research.package.gdoc | release-notes.[version] }}_
