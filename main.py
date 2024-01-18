import customtkinter as ctk
from tkinter import filedialog
import os
import shutil
import json

file_move_history = []

def find_and_move_files(src_dir, dest_dir, search_term):                
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
        except OSError as e:
            print(f"Error creating destination directory: {dest_dir}, {e}")
            status_label.configure(text=f"Error: {e}")
            return

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if search_term.lower() in file.lower():
                src_file_path = os.path.join(root, file)
                if not os.path.exists(src_file_path):
                    print(f"Source file does not exist: {src_file_path}")
                    continue

                dest_file_path = os.path.join(dest_dir, file)
                try:
                    shutil.move(src_file_path, dest_file_path)
                    file_move_history.append((dest_file_path, src_file_path))
                    print(f"Moved: {src_file_path} -> {dest_file_path}")
                except OSError as e:
                    print(f"Error moving file {src_file_path}. {e}")
                    status_label.configure(text=f"Error: {e}")

def save_settings(settings):
    with open('settings.json', 'w') as f:
        json.dump(settings, f)

def load_settings():
    try:
        with open('settings.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"src_directory": "", "dest_directory": "", "search_term": ""}

def browse_folder(entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, ctk.END)
        entry.insert(0, folder_path)

def delete_empty_folders(path):
    while True:
        empty_folders_found = False

        for root, dirs, files in os.walk(path, topdown=False):
            if not dirs and not files:
                try:
                    os.rmdir(root)  
                    file_move_history.append((None, root))
                    empty_folders_found = True
                    print(f"Deleting empty folder: {root}")
                except OSError as e:
                    print(f"Error deleting folder: {root}, {e}")
                    status_label.configure(text=f"Error: {e}")
        if not empty_folders_found:
                status_label.configure(text=f"Deleted: empty folders")
                break

def undo_last_move():
    if file_move_history:
        last_move = file_move_history.pop()
        if last_move[0] is None:
            try:
                if not os.path.exists(last_move[1]):
                    os.makedirs(last_move[1])
                    print(f"Created folder: {last_move[1]}")
                    status_label.configure(text="Undo: last folder deletion")
                else:
                    print(f"Folder already exists: {last_move[1]}")
                    status_label.configure(text="Folder already exists")
            except OSError as e:
                print(f"Error creating folder: {last_move[1]}, {e}")
                status_label.configure(text=f"Error: {e}")
        else:
            dest_file_path, src_file_path = last_move
            try:
                shutil.move(dest_file_path, src_file_path)
                print(f"Moved: {dest_file_path} -> {src_file_path}")
                status_label.configure(text="Undo: last file move")
            except OSError as e:
                print(f"Error moving file: {dest_file_path}, {e}")
                status_label.configure(text=f"Error: {e}")
    else:
        status_label.configure(text="No move history")

def run_script():
    src = src_entry.get()
    dest = dest_entry.get()
    term = term_entry.get()
    find_and_move_files(src, dest, term)
    status_label.configure(text="Files moved successfully!")
    save_settings({"src_directory": src, "dest_directory": dest, "search_term": term})

# Window
root = ctk.CTk()
root.title("Sample Sort")

#  Load Settings
settings = load_settings()

# Main frame to hold widgets
main_frame = ctk.CTkFrame(root)
main_frame.pack(padx=5, pady=5) 

ctk.CTkLabel(main_frame, text="Source Directory:").pack(pady=(10, 0))
src_entry = ctk.CTkEntry(main_frame, width=400)
src_entry.insert(0, settings["src_directory"])
src_entry.pack(padx=5, pady=(1, 5))
ctk.CTkButton(main_frame, text="Browse", command=lambda: browse_folder(src_entry)).pack(pady=5)

ctk.CTkLabel(main_frame, text="Destination Directory:").pack()
dest_entry = ctk.CTkEntry(main_frame, width=400)
dest_entry.insert(0, settings["dest_directory"])
dest_entry.pack(padx=5, pady=5)
ctk.CTkButton(main_frame, text="Browse", command=lambda: browse_folder(dest_entry)).pack(pady=5)

ctk.CTkLabel(main_frame, text="Search Term:").pack()
term_entry = ctk.CTkEntry(main_frame, width=200)
term_entry.insert(0, settings["search_term"])
term_entry.pack(pady=5)

ctk.CTkButton(main_frame, text="Move Files", command=run_script).pack(pady=5)
ctk.CTkButton(main_frame, text="Delete Empty Folders", command=lambda: delete_empty_folders(src_entry.get())).pack(pady=(5,5))
ctk.CTkButton(main_frame, text="Undo Last Move", command=undo_last_move).pack(pady=5)

status_label = ctk.CTkLabel(main_frame, text="")
status_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()



# C:\Users\pchuc\Documents\Splice\Samples\packs
# C:\Users\pchuc\samples\splice\vocal