# Ragify-Python

Ragify-Python is a Python command-line tool for concatenating files within a directory based on specified include and exclude patterns. This tool is particularly useful for merging files with different extensions and organizing content from various sources into a single output file.

## Features

- Concatenate files from a specified directory and its subdirectories.
- Include files based on patterns specified in an include file.
- Exclude files based on patterns specified in an exclude file.
- Specify file extensions to include.
- Output the concatenated content to a specified file.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ragify-python.git
   cd ragify-python
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use .\venv\Scripts\activate
   ```

3. Install the package in editable mode:

   ```bash
   pip install -e .
   ```

4. Verify the installation:

   ```bash
   ragify --help
   ```

## Usage

### Basic Usage

To concatenate files in a directory:

```bash
ragify <folder> --output <output_file>
```

### Including and Excluding Files

1. Create an include patterns file (`include_patterns.txt`) and specify patterns for files to include:

   ```
   *.py
   *.js
   ```

2. Create an exclude patterns file (`exclude_patterns.txt`) and specify patterns for files to exclude:

   ```
   *.txt
   *.md
   ```

3. Run the tool with the include and exclude patterns:

   ```bash
   ragify <folder> --include include_patterns.txt --exclude exclude_patterns.txt --output output/output.txt
   ```

### Example

```bash
ragify test_dir --include include_patterns.txt --exclude exclude_patterns.txt --output output/output.txt
```

## Testing

To test the tool, you can use the provided `test.sh` script. This script will generate a test environment with directories and files, run the `ragify` command, and display the output.

1. Make the script executable:

   ```bash
   chmod +x test.sh
   ```

2. Run the script:

   ```bash
   ./test.sh
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Author

Pranav Dhoolia
