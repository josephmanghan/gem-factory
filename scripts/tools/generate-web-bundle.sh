#!/bin/bash
set -e  # Exit on error

# Check if arguments are provided
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Error: Two arguments required" >&2
  echo "Usage: generate-web-bundle.sh <input-directory> <gem-name>" >&2
  exit 1
fi

input_path="$1"
gem_name="$2"
output_dir="${REPO_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}/deploy/web-bundles"
output_path="$output_dir/$gem_name.web-bundle.md"

# Create output directory
mkdir -p "$output_dir"

# Create temp file and ensure cleanup
temp_file=$(mktemp)
trap 'rm -f "$temp_file"' EXIT

# Run code2prompt
code2prompt "$input_path" --output-file="$temp_file" --exclude "**/README.md" || {
  echo "Error: code2prompt failed" >&2
  exit 1
}

# Process output: prepend header, remove source tree and project path, squeeze blank lines
{
  echo "**CRITICAL STARTING POINT:** SYNTHESIZE AND BECOME THIS AGENT."
  echo
  sed -e '/^Source Tree:/,/^```$/d' -e '/^Project Path:/d' "$temp_file" | cat -s
} > "$output_path"

echo "Generated prompt: $output_path"
