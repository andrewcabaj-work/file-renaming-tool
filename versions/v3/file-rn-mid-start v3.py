import argparse
import os
import sys

def add_string_n_chars_in(directory_path, string, n):
    for filename in os.listdir(directory_path):
        orig_file_path = os.path.join(directory_path, filename)
        if os.path.isfile(orig_file_path):
            name, ext = os.path.splitext(filename)
            # Ensure n does not exceed the length of the filename
            insert_position = min(n, len(name))
            # Insert the string n characters from the beginning of the filename
            new_file_name = name[:insert_position] + string + name[insert_position:] + ext
            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(orig_file_path, new_file_path)
            print(f"Renamed {filename} to {new_file_name}")

def get_input_interactively():
    directory_path = input("Enter the directory path where files are located: ")
    string = input("Enter the string to add into the file names: ")
    n = int(input("Enter the number of characters from the beginning to insert the string: "))
    return directory_path, string, n

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description='Add a string n characters into the file names.')
        parser.add_argument('directory_path', type=str, help='Directory path where files are located')
        parser.add_argument('string', type=str, help='String to add into the file names')
        parser.add_argument('n', type=int, help='Number of characters from the beginning to insert the string')
        args = parser.parse_args()

        add_string_n_chars_in(args.directory_path, args.string, args.n)
    else:
        directory_path, string, n = get_input_interactively()
        add_string_n_chars_in(directory_path, string, n)