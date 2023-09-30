#!/bin/bash

is_installed() {
    dpkg -l | grep -q $1
}

if ! is_installed "python3"; then
    echo "Python 3 is not installed. Installing Python 3..."
    sudo apt-get update
    sudo apt-get install -y python3
else
    echo "Python 3 is already installed."
fi

if ! is_installed "python3-pip"; then
    echo "pip for Python 3 is not installed. Installing pip for Python 3..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
else
    echo "pip for Python 3 is already installed."
fi

python3_version=$(python3 --version 2>&1)
pip3_version=$(pip3 --version 2>&1)

echo "Python 3 version: $python3_version"
echo "pip for Python 3 version: $pip3_version"

pip3 install pycryptodome pyperclip argon2-cffi getpass4 passlib re2
