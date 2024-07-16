import os

def rename_files_in_folder(directory_path, suffix):

    for filename in os.listdir(directory_path):
        orig_file_path = os.path.join(directory_path, filename)
        if os.path.isfile(orig_file_path):
            new_file_name = filename + suffix
            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(orig_file_path, new_file_path)
            print(f"Renamed {filename} to {new_file_name}")

directory_path = input("Folder path: ")
suffix = input("Suffix:")
rename_files_in_folder(directory_path, suffix)