import os
import shutil

# Define the path to the folder you want to organize
FOLDER_PATH = r"D:\Trail"  #os.getcwd()  # Get the current working directory 

# Define the file extensions and their corresponding folder names
FOLDERS_TYPE = {
    'video': ['.mp4', '.avi', '.mov', '.mkv'],
    'audio': ['.mp3', '.wav', '.flac', '.aac'],
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'document': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'archive': ['.zip', '.rar', '.tar', '.gz'],
    'code': ['.py', '.js', '.html', '.css', '.java'], # Don't move this folder, it contains the code for the project
    'other': []  # For files with extensions not listed above
}

# Create folders for each file type if they don't exist
for folder in FOLDERS_TYPE.keys():
    folder_path = os.path.join(FOLDER_PATH, folder) # folder path is the path to the folder where the files will be moved
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for files in os.listdir(FOLDER_PATH): # Loop through all files in the folder
    file_path = os.path.join(FOLDER_PATH, files)

    #  skip the folders
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    file_extension = os.path.splitext(files)[1].lower() # Get the file extension and convert it to lowercase

    # Move the file to the corresponding folder based on its extension
    for folder, extensions in FOLDERS_TYPE.items():
        if file_extension in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, files))
            break 
print("Files have been organized successfully.")