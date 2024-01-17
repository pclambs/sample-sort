import customtkinter as ctk
from tkinter import filedialog
import os
import shutil
import json

def find_and_move_files(src_dir, dest_dir, search_term):                
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if search_term.lower() in file.lower():
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                shutil.move(src_file_path, dest_file_path)
                print(f"Moved: {src_file_path} -> {dest_file_path}")

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

def run_script():
    src = src_entry.get()
    dest = dest_entry.get()
    term = term_entry.get()
    find_and_move_files(src, dest, term)
    status_label.configure(text="Files moved successfully!")
    save_settings({"src_directory": src, "dest_directory": dest, "search_term": term})

# Set up the main application window
root = ctk.CTk()
root.title("Sample Sort")

# Load settings
settings = load_settings()

# Create and place widgets
ctk.CTkLabel(root, text="Source Directory:").pack()
src_entry = ctk.CTkEntry(root, width=400)
src_entry.insert(0, settings["src_directory"])
src_entry.pack()
ctk.CTkButton(root, text="Browse", command=lambda: browse_folder(src_entry)).pack()

ctk.CTkLabel(root, text="Destination Directory:").pack()
dest_entry = ctk.CTkEntry(root, width=400)
dest_entry.insert(0, settings["dest_directory"])
dest_entry.pack()
ctk.CTkButton(root, text="Browse", command=lambda: browse_folder(dest_entry)).pack()

ctk.CTkLabel(root, text="Search Term:").pack()
term_entry = ctk.CTkEntry(root, width=200)
term_entry.insert(0, settings["search_term"])
term_entry.pack()

ctk.CTkButton(root, text="Move Files", command=run_script).pack()

status_label = ctk.CTkLabel(root, text="")
status_label.pack()

# Start the GUI event loop
root.mainloop()