import os
import re

def remove_trailing_numbers(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            name, ext = os.path.splitext(filename)
            new_name = re.sub(r' \(\d+\)$', '', name)
            new_filename = f"{new_name}{ext}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Add or remove trailing numbers from filenames.')
    parser.add_argument('directory', type=str, help='The directory containing the files')
    parser.add_argument('--remove', action='store_true', help='Remove trailing numbers from filenames')
    args = parser.parse_args()

    if args.remove:
        remove_trailing_numbers(args.directory)
    else:
        print("Please specify --remove")