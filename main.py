import os
import re
import glob

from utils import is_path_exists_or_creatable
from functions import create_new_database, open_existing_database
import art

folder_name = "Passwords"

home_dir = os.path.expanduser("~")
folder_path = os.path.join(home_dir, folder_name)

print(art.passman_ascii)
print("Welcome to Password Manager (passman) 🔐")
print("minimalist and easy tool to store your passwords safely")
print()

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print(f"Folder '{folder_path}' created successfully.")
else:
    print(f"Folder '{folder_path}' found.")

while True:
    print("—" * 80)
    print("Menu:")
    print("1. Create new database")
    print("2. Open existing database")
    print("Any key to Exit")
    print("—" * 80)

    choice = input("Enter your choice: ")

    if choice == "1":
        print("—" * 80)
        print("Creating a new database...")
        create_new_database(folder_path)
    elif choice == "2":
        print("—" * 80)
        print("Which database do you want to open?")

        items = os.listdir(folder_path)
        folder_names = []
        n = 1
        for item in items:
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                print(n, end=" "), print(item)
                folder_names.append(item)
                n += 1

        print("—" * 80)
        try:
            choice = int(input("Enter the number of the folder you want to open: "))

            if 1 <= choice <= len(folder_names):
                selected_folder = folder_names[choice - 1]
                folder_to_open = os.path.join(folder_path, selected_folder)

                print(f"You selected folder: {selected_folder}")
                print(f"Path to the selected folder: {folder_to_open}")
                open_existing_database(folder_to_open)
            else:
                print("Invalid choice. Please select a valid folder number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Exiting the program.")
        break
