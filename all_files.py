import os
import subprocess
import pyperclip

# Constants for exclusions
EXCLUDE_FILES = ['__init__.py', 'all_files.py']
EXCLUDE_DIRS = ['__pycache__', 'client_tests', 'server_tests']

def read_files(folder, extensions):
    """
    Recursively reads files with specified extensions in visible folders,
    excluding unwanted directories and files.
    """
    result = {}
    for root, dirs, files in os.walk(folder):
        # Exclude hidden folders and unwanted directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in EXCLUDE_DIRS]

        for file in files:
            if any(file.endswith(ext) for ext in extensions) and file not in EXCLUDE_FILES:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    result[file] = f.read()
    return result

def get_tree_structure(folder):
    """
    Get the directory tree structure using the `tree` command.
    """
    try:
        # Use subprocess to execute the tree command
        tree_output = subprocess.check_output(["tree", folder], text=True)
        return tree_output
    except FileNotFoundError:
        # Fallback in case `tree` is not installed
        print("The 'tree' command is not installed on your system.")
        return ""

def main():
    import sys
    if len(sys.argv) < 3:
        print("Usage: script.py <folder> <ext1> <ext2> ...")
        return

    folder = sys.argv[1]
    extensions = sys.argv[2:]

    # Read file contents
    file_dict = read_files(folder, extensions)

    # Get directory tree structure
    tree_structure = get_tree_structure(folder)

    # Combine results
    result_str = "{\n" + ",\n".join([f'"{k}": """{v}"""' for k, v in file_dict.items()]) + "\n}"
    result_str += "\n\nTree Structure:\n" + tree_structure

    try:
        pyperclip.copy(result_str)
        print("Copied to clipboard!")
    except pyperclip.PyperclipException:
        output_file = "output.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result_str)
        print(f"Output saved to {output_file}")

if __name__ == '__main__':
    main()
