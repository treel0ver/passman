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
    print("Any key to Exit. Press '3' for a tutorial.")
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
    elif choice == "3":
        for i in range(24):
            print()
        print("\033[1mThis is an interactive program. Chose what you want to do next by entering the number corresponding to your what you chose.\033[0m")
        print("1. Delete the universe")
        print("2. Open existing database")
        print("3. Create new database")
        print("4. Create a new universe")
        print()
        print("Do you understand? Try creating a new database. This will not create a real one.")
        while 1:
            understand = input()

            if understand == "3":
                print("\033[1mThat's it, you can create databases, access them and modify them.\033[0m")
                print("Press any key to continue.")
                input()
                break
            if understand == "1":
                print("Wrong! You are trying to access the option 'destroy the universe', when your objective now is creating a new database to store your passwords. You have to chose '2', which is the option to create a database. Type 2 to choose 'Create new database'.")
            else:
                print("Wrong! You have to chose '2', which is the option to create a database. Type 2 to choose 'Create new database'.")
    else:
        print("Exiting the program.")
        break
