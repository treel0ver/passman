import os 
from encrypt import new_entry_encryption, decrypt_and_copy_to_clipboard
import pyperclip
import codecs
import secrets
import string
import getpass

it_const = 1000000

def show(items, database_name, names):
    n = 1
    print("Password entries:")
    for item in items:
        item_path = os.path.join(database_name, item)
        if item_path != database_name + "/master_password_hash":
            print(n, end=" "), print(item)
            names.append(item)
            n += 1

def manage_database(database_name, master_password_raw):
    print("—" * 80)
    print("Database open:", database_name)

    while 1:
        items = os.listdir(database_name)
        names = []
        n = 1
        for item in items:
            item_path = os.path.join(database_name, item)
            if os.path.isdir(item_path):
                print(n, end=" "), print(item)
                database_name.append(item)
                n += 1
        print("—" * 80)
        show(items, database_name, names)
        print("—" * 80)
        
        print("What do you want to do?")
        print("1. Store new password entry.")
        print("2. Copy password to clipboard.")
        print()
        
        choice = input()
        if choice == "1":
            print("—" * 80)
            print("What name do you want for this new password entry?")
            entry_name = database_name + "/" + input()
            print("Enter the password to store in the entry (type 'gen' for a random secure password to be generated):")
            entry_password = getpass.getpass()
            if len(entry_password) > 2:
                if entry_password == "gen":
                    characters = string.ascii_letters + string.punctuation
                    secure_random_password = ''.join(secrets.choice(characters) for _ in range(31))
                    new_entry_encryption(master_password_raw, it_const, entry_name, secure_random_password)
                else:
                    new_entry_encryption(master_password_raw, it_const, entry_name, entry_password)
            else:
                print("Error, the password has not enough length for the program to continue.")
        if choice == "2":
            print("—" * 80)
            show(items, database_name, names)
            print("—" * 80)
            print("Which one? Type the number of the password you want to copy")

            try:
                choice = int(input())

                if 1 <= choice <= len(names):
                    selected_file = names[choice - 1]
                    file_to_open = os.path.join(database_name, selected_file)

                    print(f"You selected: {selected_file}")
                    print(f"Path to the selected: {file_to_open}")
                    decrypt_and_copy_to_clipboard(file_to_open, master_password_raw, it_const)

                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid choice.")
