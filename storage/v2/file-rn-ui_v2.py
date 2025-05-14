import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import subprocess
import os

root = tk.Tk()
root.title("File Renaming Tool")

def call_renaming_script(script, directory_path, string):
    script_folder = r"C:\Users\andrew.cabaj\Project Code\file-renaming-tool\versions\v2" # Static script folder location
    os.chdir(script_folder)
    subprocess.run(['python', script, directory_path, string], check=True)

def select_folder():
    directory_path = filedialog.askdirectory()
    if directory_path:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, directory_path)

def start_renaming_thread(script, directory_path, string):
    if not directory_path:
        messagebox.showerror("Error", "Please select a directory.")
        return
    threading.Thread(target=call_renaming_script, args=(script, directory_path, string), daemon=True).start()

def handle_prefix_operation(operation_type, string):
    directory_path = folder_path_entry.get()
    if operation_type == "add":
        start_renaming_thread('file-rn-pre-add v2.py', directory_path, string)
    elif operation_type == "sub":
        start_renaming_thread('file-rn-pre-sub v2.py', directory_path, string)

def handle_suffix_operation(operation_type, string):
    directory_path = folder_path_entry.get()
    if operation_type == "add":
        start_renaming_thread('file-rn-post-add v2.py', directory_path, string)
    elif operation_type == "sub":
        start_renaming_thread('file-rn-post-sub v2.py', directory_path, string)

folder_label = tk.Label(root, text="PATH", font=('Helvetica', 8, 'bold'))
folder_label.grid(row=0, column=0, sticky='W', padx=5, pady=(5,0))
folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=(5,0), sticky='ew')
browse_button = tk.Button(root, text="BROWSE", command=select_folder, bg='#A9A9A9', font=('Helvetica', 7, 'bold'))
browse_button.grid(row=0, column=3, padx=5, pady=(5,0), sticky='ew')

separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=1, column=0, columnspan=4, sticky='ew', padx=10, pady=5)

# Moved prefix widgets from row=1 to row=2
prefix_label = tk.Label(root, text="PREFIX", font=('Helvetica', 8, 'bold'))
prefix_label.grid(row=2, column=0, sticky='e', padx=5, pady=0)
prefix_entry = tk.Entry(root, width=50)
prefix_entry.grid(row=2, column=1, padx=5, pady=0)
add_prefix_button = tk.Button(root, text="  INSERT  ", command=lambda: handle_prefix_operation('add', prefix_entry.get()), bg='#A9A9A9', font=('Helvetica', 7, 'bold'))
add_prefix_button.grid(row=2, column=2, padx=0, pady=0, sticky='ew')
sub_prefix_button = tk.Button(root, text="REMOVE", command=lambda: handle_prefix_operation('sub', prefix_entry.get()), bg='#A9A9A9', font=('Helvetica', 7, 'bold'))
sub_prefix_button.grid(row=2, column=3, padx=5, pady=0, sticky='ew')

# Moved suffix widgets from row=2 to row=3
suffix_label = tk.Label(root, text="SUFFIX", font=('Helvetica', 8, 'bold'))
suffix_label.grid(row=3, column=0, sticky='e', padx=5, pady=0)
suffix_entry = tk.Entry(root, width=50)
suffix_entry.grid(row=3, column=1, padx=5, pady=0)
add_suffix_button = tk.Button(root, text="  INSERT  ", command=lambda: handle_suffix_operation('add', suffix_entry.get()), bg='#A9A9A9', font=('Helvetica', 7, 'bold'))
add_suffix_button.grid(row=3, column=2, padx=0, pady=0, sticky='ew')
sub_suffix_button = tk.Button(root, text="REMOVE", command=lambda: handle_suffix_operation('sub', suffix_entry.get()), bg='#A9A9A9', font=('Helvetica', 7, 'bold'))
sub_suffix_button.grid(row=3, column=3, padx=5, pady=5, sticky='ew')

root.mainloop()