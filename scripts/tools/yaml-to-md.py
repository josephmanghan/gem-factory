#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

# ============================================================================
# YAML to Markdown Converter
# Converts .yaml files to .md files with YAML code fences
# ============================================================================

def convert_yaml_to_md(yaml_path: Path) -> tuple[bool, Path | None]:
    """
    Converts a YAML file to Markdown with code fence.
    Returns: (success, output_path)
    """
    try:
        # Read YAML content
        yaml_content = yaml_path.read_text(encoding='utf-8')

        # Create markdown with code fence
        md_content = f"```yaml\n{yaml_content}\n```\n"

        # Create .md file path (same name, different extension)
        md_path = yaml_path.with_suffix('.md')

        # Write markdown file
        md_path.write_text(md_content, encoding='utf-8')

        # Remove original YAML file
        yaml_path.unlink()

        return True, md_path

    except Exception as e:
        print(f'Error converting {yaml_path.name}: {e}', file=sys.stderr)
        return False, None


def main():
    parser = argparse.ArgumentParser(
        description='YAML to Markdown Converter - Wraps YAML files in markdown code fences'
    )
    parser.add_argument(
        '-d', '--directory',
        type=str,
        required=True,
        help='Directory to process (searches recursively for .yaml files)'
    )
    args = parser.parse_args()

    target_dir = Path(args.directory).resolve()

    if not target_dir.is_dir():
        print(f'Directory not found: {target_dir}', file=sys.stderr)
        sys.exit(1)

    # Find all .yaml files
    yaml_files = list(target_dir.rglob('*.yaml'))

    if not yaml_files:
        print('No YAML files found')
        sys.exit(0)

    converted = 0
    failed = 0

    for yaml_file in yaml_files:
        success, _ = convert_yaml_to_md(yaml_file)

        if success:
            converted += 1
        else:
            failed += 1

    # Output simple summary
    if failed > 0:
        print(f'Converted {converted} YAML files ({failed} failed)')
    else:
        print(f'Converted {converted} YAML files')


if __name__ == '__main__':
    sys.dont_write_bytecode = True
    main()
