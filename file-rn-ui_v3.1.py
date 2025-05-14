import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import subprocess
import os

root = tk.Tk()
root.title("File Renaming Tool")

# Function to call renaming script
def call_renaming_script(script, *args):
    script_folder = r"C:\Users\Andrew.Cabaj\Documents\python-projects\general-utilities\file-renaming\versions\v3"  # Static script folder location
    os.chdir(script_folder)
    subprocess.run(['python', script, *args], check=True)

# Function to select folder
def select_folder():
    directory_path = filedialog.askdirectory()
    if directory_path:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, directory_path)

# Function to handle threads for renaming
def start_renaming_thread(script, *args):
    directory_path = args[0]
    if not directory_path:
        messagebox.showerror("Error", "Please select a directory.")
        return
    threading.Thread(target=call_renaming_script, args=(script, *args), daemon=True).start()

# Functions to handle prefix and suffix
def handle_prefix_operation(operation_type, string):
    directory_path = folder_path_entry.get()
    if operation_type == "add":
        start_renaming_thread('file-rn-pre-add v3.py', directory_path, string)
    elif operation_type == "sub":
        start_renaming_thread('file-rn-pre-sub v3.py', directory_path, string)

def handle_suffix_operation(operation_type, string):
    directory_path = folder_path_entry.get()
    if operation_type == "add":
        start_renaming_thread('file-rn-post-add v3.py', directory_path, string)
    elif operation_type == "sub":
        start_renaming_thread('file-rn-post-sub v3.py', directory_path, string)

# Function to run find and replace operation
def handle_find_replace(directory_path, keyword, replacement):
    directory_path = folder_path_entry.get()
    start_renaming_thread('file-rn-find-replace.py', directory_path, keyword, replacement)

# Function to handle mid operation (inserting in the middle)
# def handle_mid_operation(string, position):
#     directory_path = folder_path_entry.get()
#     if not position.isdigit():
#         messagebox.showerror("Error", "Position must be a number.")
#         return
#     start_renaming_thread('file-rn-mid-add v3.py', directory_path, string, position)

# def calculate_length(input_string):
#     result = subprocess.run(['python', 'file-rn-len-count.py', input_string], capture_output=True, text=True)
#     output = result.stdout.strip()
#     print(output)
#     entry_position.delete(0, tk.END)
#     entry_position.insert(0, output)
#     entry_input.delete(0, tk.END)  # Clear the entry_input field

# Change interface based on combo selection
def on_combobox_change(event):
    option = combo.get()
    
    # Hide all widgets below combo box
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) > 1:
            widget.grid_forget()
    
     # Common elements (folder path)
    if option:
        folder_label.grid(row=1, column=0, padx=2, pady=2, sticky='w')
        folder_path_entry.grid(row=1, column=1, padx=2, pady=2, sticky='ew')
        browse_button.grid(row=1, column=2, columnspan=2, padx=2, pady=2, sticky='ew')

    if option == 'PREFIX':
        # Update buttons to call prefix operations
        label_input.grid(row=2, column=0, padx=2, pady=2, sticky='w')
        entry_input.grid(row=2, column=1, padx=2, pady=2, sticky='ew')
        button_add.config(command=lambda: handle_prefix_operation('add', entry_input.get()))
        button_remove.config(command=lambda: handle_prefix_operation('sub', entry_input.get()))
        button_add.grid(row=2, column=2, padx=2, pady=2, sticky='ew')
        button_remove.grid(row=2, column=3, padx=2, pady=2, sticky='ew')

    elif option == 'SUFFIX':
        # Update buttons to call suffix operations
        label_input.grid(row=2, column=0, padx=2, pady=2, sticky='w')
        entry_input.grid(row=2, column=1, padx=2, pady=2, sticky='ew')
        button_add.config(command=lambda: handle_suffix_operation('add', entry_input.get()))
        button_remove.config(command=lambda: handle_suffix_operation('sub', entry_input.get()))
        button_add.grid(row=2, column=2, padx=2, pady=2, sticky='ew')
        button_remove.grid(row=2, column=3, padx=2, pady=2, sticky='ew')

    # elif option == 'MID':
    #     # Update for mid option, showing additional entry for position
    #     label_input.grid(row=2, column=0, padx=2, pady=2, sticky='w')
    #     entry_input.grid(row=2, column=1, padx=2, pady=2, sticky='ew')
    #     label_position.config(text="Input length")
    #     label_position.grid(row=3, column=0, padx=2, pady=2, sticky='w')
    #     entry_position.grid(row=3, column=1, padx=2, pady=2, sticky='ew')
    #     button_len.config(text="Calc. Len.", command=lambda: calculate_length(entry_input.get()))
    #     button_len.grid(row=2, column=2, padx=2, pady=2, sticky='ew')
    #     button_add.config(command=lambda: handle_mid_operation(entry_input.get(), entry_position.get()))
    #     button_add.grid(row=3, column=2, padx=2, pady=2, sticky='ew')

    elif option == 'FIND & REPLACE':
        keyword_label.grid(row=4, column=0, padx=2, pady=0, sticky='w')
        keyword_entry.grid(row=4, column=1, padx=2, pady=0, sticky='ew')
        replacement_label.grid(row=5, column=0, padx=2, pady=0, sticky='w')
        replacement_entry.grid(row=5, column=1, padx=2, pady=0, sticky='ew')
        rename_button.grid(row=4, column=2, rowspan=2, padx=2, pady=2, sticky='ew')

# UI setup
# Path input and browse
folder_label = tk.Label(root, text="FOLDER", font=('Helvetica', 8,'bold'))
folder_path_entry = tk.Entry(root, width=50)
browse_button = tk.Button(root, text="BROWSE", command=select_folder, bg='#A9A9A9', font=('Helvetica', 7, 'bold'))
# Input string
label_input = tk.Label(root, text="TEXT", font=('Helvetica', 8, 'bold'))
entry_input = tk.Entry(root)
# label_position = tk.Label(root, font=('Helvetica', 10))
# entry_position = tk.Entry(root)

button_add = tk.Button(root, text="ADD", command=lambda: handle_prefix_operation('add', entry_input.get()), bg='#A9A9A9', font=('Helvetica', 7, 'bold'), width=5)
button_remove = tk.Button(root, text="ERASE", command=lambda: handle_prefix_operation('sub', entry_input.get()), bg='#A9A9A9', font=('Helvetica', 7, 'bold'), width=5)
# button_len = tk.Button(root, text="Calc. Len", command=lambda: calculate_length(entry_input.get(), bg='#A9A9A'))
# button_add_mid = tk.Button(root, text="ADD", command=lambda: handle_mid_operation(entry_input.get(), entry_position.get()), bg='#A9A9A9')

keyword_label = tk.Label(root, text="FIND", font=('Helvetica', 8, 'bold'))
keyword_entry = tk.Entry(root, width=50)
replacement_label = tk.Label(root, text="REPLACE", font=('Helvetica', 8, 'bold'))
replacement_entry = tk.Entry(root, width=50)
rename_button = tk.Button(root, text="RENAME FILES", command=lambda: handle_find_replace(folder_path_entry.get(), keyword_entry.get(), replacement_entry.get()), bg='#A9A9A9', font=('Helvetica', 7, 'bold'), height=3)

# Combo Box for Prefix/Suffix/Mid selection
label_combo = tk.Label(root, text="SELECT", font=('Helvetica', 8, 'bold'))
label_combo.grid(row=0, column=0, padx=2, pady=2, sticky='w')
combo = ttk.Combobox(root, width=50, values=['PREFIX', 
                                   'SUFFIX', 
                                   'FIND & REPLACE'
                                #    ,'MID'
                                ])
combo.grid(row=0, column=1, padx=2, pady=2, sticky='ew', columnspan=1)
combo.bind("<<ComboboxSelected>>", on_combobox_change)

# Initialize default view
on_combobox_change(None)

# Configure column widths for proper spacing
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()