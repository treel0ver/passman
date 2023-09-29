import os
import argon2
from utils import is_path_exists_or_creatable
from manage import manage_database
import getpass

ph = argon2.PasswordHasher(
    time_cost=40,   
    memory_cost=65536, 
    parallelism=2,
    hash_len=128, 
    type=argon2.Type.ID
)

def create_new_database(folder_path):
    while True:
        name = input("Enter the name for your new database (or 'exit' to cancel): ")
        if name == 'exit':
            break

        folder_name = os.path.join(folder_path, name)

        if not is_path_exists_or_creatable(folder_name):
            print("Not a valid name for a new database.")
        else:

            master_password = getpass.getpass("Enter your new master password: ")
            master_password_test = getpass.getpass("Enter it again for confirmation: ")
            if master_password == master_password_test:
                print("Passwords match!")
                os.mkdir(folder_name)
                print(f"Folder '{folder_name}' created successfully.")
                hash = ph.hash(master_password)

                MP_file = os.path.join(folder_name, "master_password_hash")
                try:
                    with open(MP_file, "x") as file:
                        file.write(hash)
                    print(f"Hashed password written to {MP_file}.")
                    break
                except FileExistsError:
                    print(f"File '{MP_file}' already exists. Choose a different filename.")

            else:
                print("Passwords do not match. Please try again.")

def open_existing_database(name):
    stored_hash_file = name + "/" + "master_password_hash"

    try:
        with open(stored_hash_file, 'r') as file:
            file_contents = file.read()

            stored_hash = file_contents
    except FileNotFoundError:
        print(f"File not found: {stored_hash_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    master_password_try = getpass.getpass("Enter the master password: ")

    if ph.verify(stored_hash, master_password_try):
        print("\033[32mPassword is correct.\033[0m")
        manage_database(name, master_password_try)
    else:
        print("Password is incorrect.")
