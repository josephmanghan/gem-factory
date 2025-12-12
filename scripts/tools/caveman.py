#!/usr/bin/env python3

import argparse
import re
import shutil
import sys
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

SUPPORTED_EXTENSIONS = {'.md', '.txt'}
EXEMPT_FILES = {'README.md', 'help.instructions.md'}
EXEMPT_SUFFIXES = {'.template.md', '.package.yaml'}

# Approved emojis for this repo
# See STYLE-STUFF.md for the full list and usage guidelines
ALLOWED_EMOJIS = (
    '⚠️'  # Warning sign - for alerts and cautions
    '✅'  # Check mark - for completed items or approvals
    '❌'  # Cross mark - for errors or rejections
    '💡'  # Light bulb - for tips and ideas
    '🎉'  # Celebration - for successes and milestones
    '📝'  # Memo - for notes and documentation
    '🔧'  # Wrench - for tools and configuration
    '🚀'  # Rocket - for launches and deployments
    '✨'  # Sparkles - for new features or enhancements
    '📋'  # Clipboard - for checklists and tasks
    '🔍'  # Magnifying glass - for search and investigation
    '⭐'  # Star - for highlights and favorites
)

STOP_WORDS = {
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
    'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being',
    'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't",
    'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during',
    'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't",
    'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here',
    "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i',
    "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's",
    'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself',
    'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought',
    'our', 'ours', 'ourselves', 'over', 'own', 'same', "shan't", 'she',
    "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such',
    'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves',
    'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're",
    "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up',
    'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were',
    "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which',
    'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would',
    "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours',
    'yourself', 'yourselves',
}

# ============================================================================
# COMPILED PATTERNS (for performance)
# ============================================================================

PATTERN_SINGLE_COMMENT = re.compile(r'//.*$', re.MULTILINE)
PATTERN_BLOCK_COMMENT = re.compile(r'/\*[\s\S]*?\*/')
PATTERN_WHITESPACE = re.compile(r'\s+')
PATTERN_BOX_CHARS = re.compile(r'[┌─┐↓↑├┤└┘]')
PATTERN_NON_WORD = re.compile(r'[^\w\s#\-\./\{\}]')
PATTERN_EMOJI = re.compile('(' + '|'.join(re.escape(e) for e in ALLOWED_EMOJIS) + ')')  # Matches any allowed emoji
PATTERN_EXCESS_NEWLINES = re.compile(r'\n\s*\n\s*\n')
PATTERN_CODE_SEGMENTS = re.compile(r'(```[\s\S]*?```|`[^`]+`)')
PATTERN_CODE_FENCE = re.compile(r'^```(\w+)?\n([\s\S]*?)\n```$')

# ============================================================================
# CORE CONVERSION LOGIC
# ============================================================================

def compact_code(code: str) -> str:
    """Removes comments and compacts whitespace in code blocks."""
    code = PATTERN_SINGLE_COMMENT.sub('', code)
    code = PATTERN_BLOCK_COMMENT.sub('', code)
    return PATTERN_WHITESPACE.sub(' ', code)


def remove_stop_words(text: str) -> str:
    """Removes stop words while preserving markdown structure."""
    # Protect emojis by replacing them with placeholders BEFORE lowercasing
    emoji_placeholders = {}
    def replace_emoji(match):
        placeholder = f'__EMOJI_{len(emoji_placeholders)}__'
        emoji_placeholders[placeholder.lower()] = match.group(0)  # Store with lowercase key
        return placeholder
    
    text = PATTERN_EMOJI.sub(replace_emoji, text)
    
    text = text.lower().replace('\n', ' __newline__ ')
    text = PATTERN_NON_WORD.sub('', text)
    
    words = [
        word for word in text.split()
        if word == '__newline__'
        or word.startswith(('#', '-', '__emoji_'))
        or (word not in STOP_WORDS and len(word) > 1)
    ]
    
    result = ' '.join(words).replace('__newline__', '\n')
    result = re.sub(r'[ \t]+', ' ', result)  # Only compact spaces/tabs, not newlines
    result = PATTERN_EXCESS_NEWLINES.sub('\n\n', result).strip()
    
    # Restore emojis (now they're lowercase in the result)
    for placeholder, emoji in emoji_placeholders.items():
        result = result.replace(placeholder, emoji)
    
    return result


def parse_markdown(text: str) -> list[dict]:
    """Parses markdown into segments: text, code-fence, or inline-code."""
    segments = []
    last_index = 0
    
    for match in PATTERN_CODE_SEGMENTS.finditer(text):
        if match.start() > last_index:
            segments.append({'type': 'text', 'content': text[last_index:match.start()]})
        
        content = match.group(0)
        seg_type = 'code-fence' if content.startswith('```') else 'inline-code'
        segments.append({'type': seg_type, 'content': content})
        last_index = match.end()
    
    if last_index < len(text):
        segments.append({'type': 'text', 'content': text[last_index:]})
    
    return segments


def to_caveman(text: str) -> str:
    """Converts text to caveman format, preserving code blocks."""
    if not text:
        return ''
    
    text = PATTERN_BOX_CHARS.sub('', text)
    segments = parse_markdown(text)
    result_parts = []
    
    for segment in segments:
        seg_type = segment['type']
        content = segment['content']
        
        if seg_type == 'inline-code':
            result_parts.append(content)
        elif seg_type == 'code-fence':
            match = PATTERN_CODE_FENCE.match(content)
            if match:
                lang = match.group(1) or ''
                code = compact_code(match.group(2))
                result_parts.append(f'```{lang}\n{code}\n```')
            else:
                result_parts.append(content)
        else:
            result_parts.append(remove_stop_words(content))
    
    return ''.join(result_parts)

# ============================================================================
# FILE PROCESSING
# ============================================================================

def process_file(file_path: Path, input_dir: Path, output_dir: Path) -> tuple[str, int, int]:
    """
    Process a single file.
    Returns: (status_message, original_size, caveman_size)
    """
    relative_path = file_path.relative_to(input_dir)
    output_path = output_dir / relative_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Copy exempt files without processing
    if file_path.name in EXEMPT_FILES or any(file_path.name.endswith(suffix) for suffix in EXEMPT_SUFFIXES):
        shutil.copy2(file_path, output_path)
        return f'→ Copied (exempt): {relative_path}', 0, 0
    
    # Process supported file types
    if file_path.suffix in SUPPORTED_EXTENSIONS:
        content = file_path.read_text(encoding='utf-8')
        caveman_content = to_caveman(content)
        output_path.write_text(caveman_content, encoding='utf-8')
        return f'✓ Processed: {relative_path}', len(content), len(caveman_content)
    
    # Copy other files as-is
    shutil.copy2(file_path, output_path)
    return f'→ Copied: {relative_path}', 0, 0


# ============================================================================
# MAIN PROCESSING
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Caveman Converter - Compacts markdown/text files by removing stop words'
    )
    parser.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help='Input directory path'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help='Output directory path'
    )
    args = parser.parse_args()
    
    input_dir = Path(args.input).resolve()
    output_dir = Path(args.output).resolve()

    if not input_dir.is_dir():
        print(f'Input directory not found: {input_dir}', file=sys.stderr)
        sys.exit(1)

    all_files = [f for f in input_dir.rglob('*') if f.is_file() and not f.name.startswith('.')]
    stats = {'processed': 0, 'copied': 0, 'original_size': 0, 'caveman_size': 0}

    for file_path in all_files:
        try:
            _, orig_size, cave_size = process_file(file_path, input_dir, output_dir)

            if orig_size > 0:
                stats['processed'] += 1
                stats['original_size'] += orig_size
                stats['caveman_size'] += cave_size
            else:
                stats['copied'] += 1
        except Exception as e:
            print(f'Warning: {file_path.relative_to(input_dir)}: {e}', file=sys.stderr)

    if stats['processed'] == 0 and stats['copied'] == 0:
        print('No files were processed or copied.', file=sys.stderr)
        sys.exit(1)

    # Output simple summary
    if stats['processed'] > 0:
        reduction = round((1 - stats['caveman_size'] / stats['original_size']) * 100)
        print(f"Processed {stats['processed']} files, copied {stats['copied']} ({reduction}% reduction)")
    else:
        print(f"Copied {stats['copied']} files")


if __name__ == '__main__':
    sys.dont_write_bytecode = True
    main()
