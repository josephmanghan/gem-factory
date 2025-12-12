#!/bin/bash
set -e  # Exit on error

# Check if directory argument is provided
if [ -z "$1" ]; then
  echo "Error: Directory argument required" >&2
  echo "Usage: npm run generate:web-bundle -- <directory>" >&2
  exit 1
fi

input_path="$1"
parent_path=$(dirname "$input_path")
output_dir="$parent_path/web-bundle"
output_path="$output_dir/$(basename "$parent_path").web-bundle.md"

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
