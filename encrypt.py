from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import os
import pyperclip

def new_entry_encryption(MP, iteration_number, entry_name, entry_password):
    password = MP
    salt = os.urandom(16)
    key = PBKDF2(password, salt, dkLen=32, count=iteration_number)
    cipher = AES.new(key, AES.MODE_CBC)

    plain_text = entry_password
    padded_plain_text = pad(plain_text.encode(), AES.block_size)
    cipher_text = cipher.encrypt(padded_plain_text)

    with open(entry_name, "wb") as file:
        file.write(salt)
        file.write(cipher.iv)
        file.write(cipher_text)

    print("The password safe has been created with encrypted content.")

def unpad_data(data):
    padding_size = data[-1]
    if padding_size <= 0 or padding_size > AES.block_size:
        raise ValueError("Invalid padding size")
    return data[:-padding_size]

def decrypt(file_to_open, MP, iteration_number):
    with open(file_to_open, "rb") as file:
        salt = file.read(16)  # Read the salt
        iv = file.read(16)    # Read the IV
        cipher_text = file.read()

    password = MP
    key = PBKDF2(password, salt, dkLen=32, count=iteration_number)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(cipher_text)
    plain_text = unpad_data(decrypted_data).decode('utf-8')
    pyperclip.copy(plain_text)
