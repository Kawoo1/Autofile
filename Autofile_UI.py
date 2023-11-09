import os
import tkinter as tk
from tkinter import filedialog
import shutil

# Organize files
def organize_files():
    source_directory = source_entry.get()
    destination_directory = destination_entry.get()
    
    # Validate source and destination paths
    if not os.path.exists(source_directory) or not os.path.exists(destination_directory):
        status_label.config(text="Invalid source or destination path")
        return
    
    # Create the target folders if they don't exist (Because they wont)
    for folder in folders:
        folder_path = os.path.join(destination_directory, folder)
        os.makedirs(folder_path, exist_ok=True)
    
    # Function to determine the category of a file
    def get_category(file_name):
        ext = file_name.split(".")[-1]
        if ext in ('mp3', 'wav', 'flac'):
            return 'Audio'
        elif ext in ('mp4', 'avi', 'mkv'):
            return 'Video'
        elif ext in ('py', 'cpp', 'java', 'js', 'html'):
            return 'Coding'
        elif ext in ('pdf'):
            return 'PDFs'
        elif ext in ('doc', 'docx','rtf','ppt'):
            return 'School'
        elif ext in ('txt'):
            return 'Accounts'
        elif ext in ('jpg', 'png', 'gif', 'xcf'):
            return 'Entertainment'
        elif ext in ('exe', 'msi'):
            return 'PersonalSoftware'
        else:
            return 'Clutter'
    
    # Move files to their respective folders
    files = os.listdir(source_directory)
    for file in files:
        source_file = os.path.join(source_directory, file)
        category = get_category(file)
        destination_folder = os.path.join(destination_directory, category)
        destination_file = os.path.join(destination_folder, file)
    
        if os.path.isfile(source_file):
            if not os.path.exists(destination_file):
                shutil.move(source_file, destination_file)
            else:
                # Handle duplicate file names by appending a unique number
                count = 1
                while os.path.exists(destination_file):
                    base, ext = os.path.splitext(file)
                    new_file_name = f"{base}_{count}{ext}"
                    destination_file = os.path.join(destination_folder, new_file_name)
                    count += 1
                shutil.move(source_file, destination_file)
    
    status_label.config(text="File organization complete")

# Function to open a file dialog for source and destination selection
def browse_directory(entry_widget):
    directory = filedialog.askdirectory()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, directory)

# Define target folders
folders = [
    'Audio',
    'Video',
    'Coding',
    'PDFs',
    'School',
    'Accounts',
    'Entertainment',
    'PersonalSoftware',
    'Clutter'
]

# Create the main window
root = tk.Tk()
root.title("File Sorter")

# Create/place labels and entry widgets for source and destination directories
source_label = tk.Label(root, text="Source Directory:")
source_label.pack()
source_entry = tk.Entry(root)
source_entry.pack()

destination_label = tk.Label(root, text="Destination Directory:")
destination_label.pack()
destination_entry = tk.Entry(root)
destination_entry.pack()

source_browse_button = tk.Button(root, text="Browse", command=lambda: browse_directory(source_entry))
source_browse_button.pack()

destination_browse_button = tk.Button(root, text="Browse", command=lambda: browse_directory(destination_entry))
destination_browse_button.pack()

# Create/place the organize button
organize_button = tk.Button(root, text="Organize Files", command=organize_files)
organize_button.pack()

# Create/place a status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()