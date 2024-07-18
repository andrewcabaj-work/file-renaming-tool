import os

def delete_prefix_from_filenames(folder_path, num_chars_to_delete):
	if num_chars_to_delete < 0:
		print("Number of characters to delete must be non-negative.")
		return

	# List all files in the given folder
	for filename in os.listdir(folder_path):
		file_path = os.path.join(folder_path, filename)
		
		# Skip directories
		if os.path.isdir(file_path):
			continue
		
		# Calculate the new filename
		new_filename = filename[num_chars_to_delete:]
		
		# Ensure the new filename is not empty
		if not new_filename:
			print(f"Skipping '{filename}' as its new name would be empty.")
			continue
		
		new_file_path = os.path.join(folder_path, new_filename)
		
		# Rename the file
		try:
			os.rename(file_path, new_file_path)
			print(f"Renamed '{filename}' to '{new_filename}'")
		except Exception as e:
			print(f"Error renaming '{filename}' to '{new_filename}': {e}")

# Example usage
if __name__ == "__main__":
	folder_path = input("Enter the path to the folder: ")
	num_chars_to_delete = int(input("Enter the number of characters to delete: "))
	delete_prefix_from_filenames(folder_path, num_chars_to_delete)