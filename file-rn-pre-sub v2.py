import argparse
import os

def rename_files_in_folder(directory_path, prefix_to_remove):
    for filename in os.listdir(directory_path):
        orig_file_path = os.path.join(directory_path, filename)
        if os.path.isfile(orig_file_path) and filename.startswith(prefix_to_remove):
            new_file_name = filename[len(prefix_to_remove):]
            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(orig_file_path, new_file_path)
            print(f"Renamed {filename} to {new_file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove prefix from file names.')
    parser.add_argument('directory_path', type=str, help='Directory path where files are located')
    parser.add_argument('prefix_to_remove', type=str, help='Prefix to remove from the files')
    args = parser.parse_args()

    rename_files_in_folder(args.directory_path, args.prefix_to_remove)