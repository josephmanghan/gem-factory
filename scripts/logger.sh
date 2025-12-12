#!/bin/bash

# ============================================================================
# Logging Utility
# Provides consistent formatting for deployment scripts
# ============================================================================

# Colors
RESET='\033[0m'
BOLD='\033[1m'
DIM='\033[2m'

# Main step indicator
log_step() {
  echo -e "${BOLD}→ $1${RESET}"
}

# Success message (indented)
log_success() {
  echo -e "  ✓ $1"
}

# Info message (indented)
log_info() {
  echo -e "  ${DIM}$1${RESET}"
}

# Error message (indented, to stderr)
log_error() {
  echo -e "  ✗ $1" >&2
}

# Divider
log_divider() {
  echo ""
}
