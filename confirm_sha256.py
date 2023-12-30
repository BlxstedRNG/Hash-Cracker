#!/usr/bin/env python3
from sys import argv
import hashlib

try:
    password = argv[1]
except IndexError:
    password = input("Enter a password to hash: ")

# Hash the password using SHA-256 and print the result
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print("Hashed Password:", hashed_password)
