#!/bin/bash
set -e  # Exit on error

# ============================================================================
# Deployment Handler
# Orchestrates the deployment of a gem: caveman processing + web bundling
# ============================================================================

# Define paths
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
GEMS_DIR="$REPO_ROOT/gems/libs"

# Source logging utilities
source "$REPO_ROOT/scripts/logger.sh"

# Check if target argument is provided
if [ -z "$1" ]; then
  echo "📦 Available gems for deployment:"
  echo ""

  # List available gems
  find "$GEMS_DIR" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | grep -v '^\.' | sort | while read -r gem; do
    echo "  • $gem"
  done

  echo ""
  echo "Usage: npm run deploy:target -- <gem-name>"
  echo "Example: npm run deploy:target -- user-testing"
  exit 1
fi

TARGET="$1"
SOURCE_DIR="$REPO_ROOT/gems/libs/$TARGET/lib"
DEPLOY_DIR="$REPO_ROOT/deploy/gems/$TARGET"
DEPLOY_LIB_DIR="$DEPLOY_DIR/lib"

echo ""
log_step "Deploying gem: $TARGET"

# Validate source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
  log_error "Source directory not found: $SOURCE_DIR"
  log_info "Available gems in gems/libs/:"
  ls -1 "$REPO_ROOT/gems/libs/" 2>/dev/null | sed 's/^/    /' >&2
  exit 1
fi

# Step 1: Clean and create deployment directories
rm -rf "$DEPLOY_DIR"
mkdir -p "$DEPLOY_LIB_DIR"

# Step 2: Run caveman processing
log_step "Processing files with caveman"
caveman_output=$(python3 "$REPO_ROOT/scripts/tools/caveman.py" \
  --input "$SOURCE_DIR" \
  --output "$DEPLOY_LIB_DIR" 2>&1)

if [ $? -eq 0 ]; then
  log_info "$caveman_output"
else
  log_error "Caveman processing failed"
  echo "$caveman_output" >&2
  exit 1
fi

# Verify caveman produced output
if [ ! "$(ls -A "$DEPLOY_LIB_DIR")" ]; then
  log_error "Caveman produced no output files"
  exit 1
fi

# Step 3: Generate web bundle
log_step "Generating web bundle"
bundle_output=$("$REPO_ROOT/scripts/tools/generate-web-bundle.sh" "$DEPLOY_LIB_DIR" 2>&1 | tail -n 1)
log_info "$bundle_output"

# Step 4: Convert YAML files to Markdown with code fences
log_step "Converting YAML files to Markdown"
yaml_output=$(python3 "$REPO_ROOT/scripts/tools/yaml-to-md.py" --directory "$DEPLOY_DIR" 2>&1)

if [ $? -eq 0 ]; then
  log_info "$yaml_output"
else
  log_error "YAML conversion failed"
  echo "$yaml_output" >&2
  exit 1
fi

# Step 5: Format the deployed output
log_step "Formatting deployed files"
npx prettier --write "$DEPLOY_DIR/**/*.{md,yaml,json}" --log-level error > /dev/null 2>&1
log_info "Formatting complete"

log_divider
log_success "Deployment complete: $DEPLOY_DIR"
echo ""
