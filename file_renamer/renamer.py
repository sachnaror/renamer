import os

def read_file_with_encoding(file_path):
    """
    Attempts to read a file with multiple encodings.
    Returns the content of the file or raises UnicodeDecodeError.
    """
    encodings = ['utf-8', 'latin-1', 'windows-1252']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            pass
    raise UnicodeDecodeError(f"Cannot read {file_path}: Tried all encodings.")

def rename_files_and_replace_content(root_dir, old_word, new_word):
    """
    Renames files, directories, and replaces content recursively in the directory structure.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Replace content inside files
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_content = read_file_with_encoding(file_path)
                if old_word in file_content:
                    new_content = file_content.replace(old_word, new_word)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Updated content in file: {file_path}")
            except UnicodeDecodeError:
                print(f"Skipping file {file_path}: Unable to decode.")

        # Rename filenames
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if old_word in filename:
                new_filename = filename.replace(old_word, new_word)
                new_file_path = os.path.join(dirpath, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {file_path} -> {new_file_path}")

        # Rename directory names
        for dirname in dirnames:
            if old_word in dirname:
                old_dir = os.path.join(dirpath, dirname)
                new_dir = os.path.join(dirpath, dirname.replace(old_word, new_word))
                os.rename(old_dir, new_dir)
                print(f"Renamed directory: {old_dir} -> {new_dir}")
