import argparse
import os

def insert_string_at_position(directory_path, string, position):
    position = int(position)
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            new_filename = filename[:position] + string + filename[position:]
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
            print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Insert string at a specific position in file names.')
    parser.add_argument('directory_path', type=str, help='Directory path where files are located')
    parser.add_argument('string', type=str, help='String to insert')
    parser.add_argument('position', type=int, help='Position to insert the string at')
    args = parser.parse_args()

    insert_string_at_position(args.directory_path, args.string, args.position)