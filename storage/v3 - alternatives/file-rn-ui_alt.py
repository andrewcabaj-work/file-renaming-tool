import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QFrame
import threading
import subprocess
import os

class FileRenamingTool(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Folder Path
        folder_layout = QHBoxLayout()
        self.folder_label = QLabel("PATH")
        folder_layout.addWidget(self.folder_label)

        self.folder_path_entry = QLineEdit()
        folder_layout.addWidget(self.folder_path_entry)

        self.browse_button = QPushButton("BROWSE")
        self.browse_button.clicked.connect(self.select_folder)
        folder_layout.addWidget(self.browse_button)

        layout.addLayout(folder_layout)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Prefix
        prefix_layout = QHBoxLayout()
        self.prefix_label = QLabel("PREFIX")
        prefix_layout.addWidget(self.prefix_label)

        self.prefix_entry = QLineEdit()
        prefix_layout.addWidget(self.prefix_entry)

        self.add_prefix_button = QPushButton("INSERT")
        self.add_prefix_button.clicked.connect(lambda: self.handle_prefix_operation('add', self.prefix_entry.text()))
        prefix_layout.addWidget(self.add_prefix_button)

        self.sub_prefix_button = QPushButton("REMOVE")
        self.sub_prefix_button.clicked.connect(lambda: self.handle_prefix_operation('sub', self.prefix_entry.text()))
        prefix_layout.addWidget(self.sub_prefix_button)

        layout.addLayout(prefix_layout)

        # Suffix
        suffix_layout = QHBoxLayout()
        self.suffix_label = QLabel("SUFFIX")
        suffix_layout.addWidget(self.suffix_label)

        self.suffix_entry = QLineEdit()
        suffix_layout.addWidget(self.suffix_entry)

        self.add_suffix_button = QPushButton("INSERT")
        self.add_suffix_button.clicked.connect(lambda: self.handle_suffix_operation('add', self.suffix_entry.text()))
        suffix_layout.addWidget(self.add_suffix_button)

        self.sub_suffix_button = QPushButton("REMOVE")
        self.sub_suffix_button.clicked.connect(lambda: self.handle_suffix_operation('sub', self.suffix_entry.text()))
        suffix_layout.addWidget(self.sub_suffix_button)

        layout.addLayout(suffix_layout)

        # Keyword Replacement
        keyword_layout = QHBoxLayout()
        self.keyword_label = QLabel("KEYWORD")
        keyword_layout.addWidget(self.keyword_label)

        self.keyword_entry = QLineEdit()
        keyword_layout.addWidget(self.keyword_entry)

        layout.addLayout(keyword_layout)

        replacement_layout = QHBoxLayout()
        self.replacement_label = QLabel("REPLACEMENT")
        replacement_layout.addWidget(self.replacement_label)

        self.replacement_entry = QLineEdit()
        replacement_layout.addWidget(self.replacement_entry)

        layout.addLayout(replacement_layout)

        self.rename_button = QPushButton("RENAME FILES")
        self.rename_button.clicked.connect(lambda: self.handle_keyword_replacement(self.folder_path_entry.text(), self.keyword_entry.text(), self.replacement_entry.text()))
        layout.addWidget(self.rename_button)

        self.setLayout(layout)
        self.setWindowTitle('File Renaming Tool')

    def select_folder(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory_path:
            self.folder_path_entry.setText(directory_path)

    def call_renaming_script(self, script, *args):
        script_folder = r"C:\Users\andrew.cabaj\GitHub\file-renaming-tool\versions\v3"  # Static script folder location
        os.chdir(script_folder)
        subprocess.run(['python', script, *args], check=True)

    def start_renaming_thread(self, script, *args):
        directory_path = args[0]
        if not directory_path:
            QMessageBox.critical(self, "Error", "Please select a directory.")
            return
        threading.Thread(target=self.call_renaming_script, args=(script, *args), daemon=True).start()

    def handle_prefix_operation(self, operation_type, string):
        directory_path = self.folder_path_entry.text()
        if operation_type == "add":
            self.start_renaming_thread('file-rn-pre-add v3.py', directory_path, string)
        elif operation_type == "sub":
            self.start_renaming_thread('file-rn-pre-sub v3.py', directory_path, string)

    def handle_suffix_operation(self, operation_type, string):
        directory_path = self.folder_path_entry.text()
        if operation_type == "add":
            self.start_renaming_thread('file-rn-post-add v3.py', directory_path, string)
        elif operation_type == "sub":
            self.start_renaming_thread('file-rn-post-sub v3.py', directory_path, string)

    def handle_keyword_replacement(self, directory_path, keyword, replacement):
        self.start_renaming_thread('file-rn-find-replace.py', directory_path, keyword, replacement)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileRenamingTool()
    ex.show()
    sys.exit(app.exec_())