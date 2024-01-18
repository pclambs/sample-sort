# Sample Sort

![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

## Description
Sample Sort is a Python application designed to help organize audio samples. It allows users to move audio files from a source directory to a destination directory based on a search term. Additionally, it provides features to delete empty directories and undo previous file operations.

## Features
Move Files: 
- Easily move files from a specified source directory to a destination directory based on a search term.

Delete Empty Folders: 
- Clean up the source directory by removing empty folders.

Undo Last Move: 
- Undo the last move operation, whether it's a file move or a folder deletion.

Save Settings: 
- Remember the last used source and destination paths between sessions.

## Installation
To run Sample Sort, you'll need Python installed on your system. If you don't have Python installed, download and install it from [Python.org](https://python.org).

Once Python is installed, clone or download this repository to your local machine.

## Dependencies
Sample Sort uses the customtkinter package for its GUI. To install customtkinter, run:

`pip install customtkinter`

## Usage
1. Start the Application:<br>
Navigate to the directory containing 'main.py' and run:

    `python main.py`

2. Set Source and Destination Directories:<br>
Use the 'Browse' buttons to select the source and destination directories.

3. Enter Search Term:<br>
Type the search term for the files you want to move in the 'Search Term' field.

4. Move Files:<br>
Click the 'Move Files' button to start moving files that match the search term.

5. Delete Empty Folders:<br>
Optionally, click the 'Delete Empty Folders' button to remove empty folders from the source directory.

6. Undo Last Move:<br>
If you need to undo the last file move or folder deletion, click the 'Undo Last Move' button.

## Error Handling
Sample Sort includes basic error handling for common issues like missing files, permission errors, and non-existent directories.

## License

This project is covered under the MIT license.

## To-Do's

[ ] ability to filter what file formats to look for

[ ] collect errors in a list and then show a summary after ops

[ ] user confirmation for file deletion and folder deletion

[ ] real-time feedback of ops (threading for responsiveness?)

[ ] more robust search. no white space search/allow multiple strings

[ ] add view of the two file directories right on the app

[ ] design a "proper" gui (probs try that grid look like the cool kids seem to do these days)

[ ] interactive block resizing