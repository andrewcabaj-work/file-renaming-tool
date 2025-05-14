import argparse
import os

def rename_files_in_folder(directory_path, keyword, replacement):
    for filename in os.listdir(directory_path):
        orig_file_path = os.path.join(directory_path, filename)
        if os.path.isfile(orig_file_path) and keyword in filename:
            new_file_name = filename.replace(keyword, replacement)
            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(orig_file_path, new_file_path)
            print(f"Renamed {filename} to {new_file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace keyword in file names.')
    parser.add_argument('directory_path', type=str, help='Directory path where files are located')
    parser.add_argument('keyword', type=str, help='Keyword to replace in the file names')
    parser.add_argument('replacement', type=str, help='Replacement string for the keyword')
    args = parser.parse_args()

    rename_files_in_folder(args.directory_path, args.keyword, args.replacement)