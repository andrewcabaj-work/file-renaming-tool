import argparse
import os

def rename_files_in_folder(directory_path, suffix):
    for filename in os.listdir(directory_path):
        orig_file_path = os.path.join(directory_path, filename)
        if os.path.isfile(orig_file_path):
            name, ext = os.path.splitext(filename)
            new_file_name = name + suffix + ext
            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(orig_file_path, new_file_path)
            print(f"Renamed {filename} to {new_file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add suffix to file names.')
    parser.add_argument('directory_path', type=str, help='Directory path where files are located')
    parser.add_argument('suffix', type=str, help='Suffix to add to the files')
    args = parser.parse_args()

    rename_files_in_folder(args.directory_path, args.suffix)