from file_renamer.renamer import rename_files_and_replace_content

def main():
    import argparse

    print("Welcome to the File Renamer Utility!")
    print("This tool will rename files, directories, and replace content recursively.")
    print("Press '.' if you want to start from the current directory.")

    root_dir = input("Enter the root directory path: ").strip()
    if root_dir == ".":
        root_dir = os.getcwd()

    if not os.path.exists(root_dir):
        print(f"The directory {root_dir} does not exist.")
        return

    old_word = input("Enter the word you want to replace: ").strip()
    new_word = input("Enter the word to replace it with: ").strip()

    if not old_word:
        print("Old word cannot be empty!")
        return

    print(f"Starting to replace '{old_word}' with '{new_word}' in {root_dir}...")
    rename_files_and_replace_content(root_dir, old_word, new_word)
    print("Replacement complete!")
