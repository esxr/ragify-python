# ragify/main.py
import os
import sys
import re
import argparse

def load_patterns(pattern_file):
    if not os.path.isfile(pattern_file):
        print(f"Error: The file '{pattern_file}' does not exist.")
        sys.exit(1)
    with open(pattern_file, 'r') as file:
        patterns = file.read().splitlines()
    # Convert shell-like patterns to regex
    regex_patterns = []
    for pattern in patterns:
        if pattern and not pattern.startswith('#'):
            # Escape dots, convert "*" to ".*" and "?" to ".", and handle directory separators
            pattern = pattern.replace(".", r"\.").replace("*", ".*").replace("?", ".")
            regex_patterns.append(re.compile(pattern))
    return regex_patterns

def matches_pattern(file, patterns):
    return any(pattern.search(file) for pattern in patterns)

def concatenate_files(input_folder, output_file, extensions, include_patterns, exclude_patterns):
    with open(output_file, 'w') as out_file:
        for root, _, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                if exclude_patterns and matches_pattern(file_path, exclude_patterns):
                    continue
                if include_patterns and not matches_pattern(file_path, include_patterns):
                    continue
                if not extensions or any(file.endswith(ext) for ext in extensions):
                    out_file.write(f"---\nfile: {os.path.relpath(file_path, input_folder)}\n---\n")
                    with open(file_path, 'r') as in_file:
                        out_file.write(in_file.read())
                    out_file.write("\n---\n")

def main():
    parser = argparse.ArgumentParser(description="Concatenate all files in a folder into one text file.")
    parser.add_argument('folder', type=str, help="Folder containing the files to concatenate.")
    parser.add_argument('--files', type=str, help="File containing extensions to include.")
    parser.add_argument('--output', type=str, default='output.txt', help="Output file name.")
    parser.add_argument('--include', type=str, help="File containing patterns of files to include.")
    parser.add_argument('--exclude', type=str, help="File containing patterns of files to exclude.")

    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Error: The folder '{args.folder}' does not exist.")
        sys.exit(1)

    extensions = []
    if args.files:
        if not os.path.isfile(args.files):
            print(f"Error: The file '{args.files}' does not exist.")
            sys.exit(1)
        with open(args.files, 'r') as ext_file:
            extensions = ext_file.read().splitlines()

    include_patterns = load_patterns(args.include) if args.include else None
    exclude_patterns = load_patterns(args.exclude) if args.exclude else None

    concatenate_files(args.folder, args.output, extensions, include_patterns, exclude_patterns)
    print(f"All specified files in {args.folder} have been concatenated into {args.output}")

if __name__ == "__main__":
    main()