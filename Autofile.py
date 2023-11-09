import os
import shutil

# Define source and destination directories
source_directory = "C:\\Users\\YourUsername\\Desktop"  # Replace with your source directory
destination_directory = "C:\\File_Auto_Sorted"

# Create the target folders if they don't exist
folders = [
    'Audio',
    'Video',
    'Coding',
    'Finance',
    'ImportantFilesforLater',
    'School',
    'Accounts',
    'Entertainment',
    'PersonalSoftware',
    'Clutter'
]

for folder in folders:
    folder_path = os.path.join(destination_directory, folder)
    os.makedirs(folder_path, exist_ok=True)

# Get a list of files in the source directory
files = os.listdir(source_directory)

# Function to determine the category of a file
def get_category(file_name):
    ext = file_name.split(".")[-1]
    if ext in ('mp3', 'wav', 'flac'):
        return 'Audio'
    elif ext in ('mp4', 'avi', 'mkv'):
        return 'Video'
    elif ext in ('py', 'cpp', 'java', 'js', 'html'):
        return 'Coding'
    elif ext in ('pdf', 'xlsx', 'csv'):
        return 'Finance'
    elif ext in ('doc', 'txt'):
        return 'ImportantFilesforLater'
    elif ext in ('docx', 'pptx', 'ppt', 'xls'):
        return 'School'
    elif ext in ('acc', 'accdb'):
        return 'Accounts'
    elif ext in ('jpg', 'png', 'gif'):
        return 'Entertainment'
    elif ext in ('exe', 'msi'):
        return 'PersonalSoftware'
    else:
        return 'Clutter'

# Move files to their respective folders
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

print("File organization complete.")
