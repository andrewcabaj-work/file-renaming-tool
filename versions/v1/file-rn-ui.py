import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading

# Create the main window
root = tk.Tk()
root.title("File Renaming Tool")

def rename_files_in_folder(directory_path, prefix, update_progress_callback):
    count = 0
    files = os.listdir(directory_path)
    total_files = len([name for name in files if os.path.isfile(os.path.join(directory_path, name))])
    for filename in files:
        orig_file_path = os.path.join(directory_path, filename)
        if os.path.isfile(orig_file_path):
            new_file_name = prefix + filename
            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(orig_file_path, new_file_path)
            count += 1
            update_progress_callback(count, total_files)  # Update the progress bar through the callback

def start_renaming_thread():
    completion_message.config(text="")
    directory_path = folder_path_entry.get()
    prefix = prefix_entry.get()
    threading.Thread(target=rename_files_in_folder, args=(directory_path, prefix, update_progress), daemon=True).start()

def select_folder():
    directory_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, directory_path)

def start_renaming():
    start_renaming_thread()

def undo_rename(directory_path, prefix, total_files):
    count = 0
    for filename in os.listdir(directory_path):
        if filename.startswith(prefix):
            new_name = filename[len(prefix):]  # Remove the prefix
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_name))
            count += 1
            update_progress(count, total_files)  # Pass total_files to update_progress
    completion_message.config(text="File Rename Undone")

def start_undo_thread():
    directory_path = folder_path_entry.get()
    prefix = prefix_entry.get()
    total_files = sum(1 for filename in os.listdir(directory_path) if filename.startswith(prefix))
    threading.Thread(target=undo_rename, args=(directory_path, prefix, total_files), daemon=True).start()

# Create and pack the widgets
tk.Label(root, text="Folder Path:").pack()
folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.pack()

browse_button = tk.Button(root, text="Browse", command=select_folder)
browse_button.pack(pady=(5, 10))

tk.Label(root, text="Prefix:").pack(pady=(0, 5))

prefix_entry = tk.Entry(root, width=50)
prefix_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=(5, 10))

rename_button = tk.Button(button_frame, text="Rename Files", command=start_renaming)
rename_button.pack(side=tk.LEFT, padx=(0, 5))

undo_button = tk.Button (button_frame, text="Undo", command=start_undo_thread)
undo_button.pack(side=tk.LEFT)

completion_message = tk.Label(root, text="", fg="green")
completion_message.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=(5, 5))

def update_progress(count, total_files):
    progress_bar['maximum'] = total_files if total_files > 0 else 1
    progress_bar['value'] = count
    root.update_idletasks()
    if count == total_files:
        completion_message.config(text="Renaming Complete!" if total_files > 0 else "No files to rename.")

# Start the GUI event loop
root.mainloop()