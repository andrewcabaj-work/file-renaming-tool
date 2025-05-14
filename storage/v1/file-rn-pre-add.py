import os

def rename_files_in_folder(directory_path, prefix):

    for filename in os.listdir(directory_path):
        orig_file_path = os.path.join(directory_path, filename)
        if os.path.isfile(orig_file_path):
            new_file_name = prefix + filename
            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(orig_file_path, new_file_path)
            print(f"Renamed {filename} to {new_file_name}")

directory_path = input("Folder path: ")
prefix = input("Prefix: ")
rename_files_in_folder(directory_path, prefix)