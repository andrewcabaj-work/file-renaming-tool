import argparse
import os

def rename_files_in_folder(directory_path, suffix_to_remove):
    for filename in os.listdir(directory_path):
        orig_file_path = os.path.join(directory_path, filename)
        if os.path.isfile(orig_file_path):
            base_name, extension = os.path.splitext(filename)
            # Check if the base name actually ends with the suffix to remove
            if suffix_to_remove and base_name.endswith(suffix_to_remove):
                new_base_name = base_name[:-len(suffix_to_remove)]
                new_filename = new_base_name + extension
                new_file_path = os.path.join(directory_path, new_filename)
                # Check if the new filename already exists to avoid FileExistsError
                if not os.path.exists(new_file_path):
                    os.rename(orig_file_path, new_file_path)
                    print(f"Renamed {filename} to {new_filename}")
                else:
                    print(f"Cannot rename {filename} to {new_filename} because the target file already exists.")
            elif not suffix_to_remove:
                print(f"No suffix provided. Skipping {filename}.")
            else:
                print(f"Suffix '{suffix_to_remove}' not found in '{filename}'. Skipping.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove suffix from file names while preserving the file extension.')
    parser.add_argument('directory_path', type=str, help='Directory path where files are located')
    parser.add_argument('suffix_to_remove', type=str, help='Suffix to remove from the files')
    args = parser.parse_args()

    rename_files_in_folder(args.directory_path, args.suffix_to_remove)