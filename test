#!/bin/bash

# Create test directories and files
mkdir -p test_dir/subdir1
mkdir -p test_dir/subdir2

# Create sample files
echo "Content of file1.py" > test_dir/file1.py
echo "Content of file2.txt" > test_dir/file2.txt
echo "Content of file3.md" > test_dir/file3.md
echo "Content of file4.cpp" > test_dir/subdir1/file4.cpp
echo "Content of file5.js" > test_dir/subdir1/file5.js
echo "Content of file6.html" > test_dir/subdir2/file6.html
echo "Content of file7.css" > test_dir/subdir2/file7.css

# Create include patterns file (include only .py and .js files)
echo "*.py" > include_patterns.txt
echo "*.js" >> include_patterns.txt

# Create exclude patterns file (exclude .txt and .md files)
echo "*.txt" > exclude_patterns.txt
echo "*.md" >> exclude_patterns.txt

# Create output directory
mkdir -p output

# Activate virtual environment
source venv/bin/activate

# Run the ragify script with include and exclude patterns
ragify test_dir --include include_patterns.txt --exclude exclude_patterns.txt --output output/output.txt

# Display the concatenated output file
cat output/output.txt

# Cleanup (optional)
deactivate