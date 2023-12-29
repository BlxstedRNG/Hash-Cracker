#!/usr/bin/env python3
from sys import argv
import hashlib


def hash_sha256(plain):
    hashed = hashlib.sha256(plain.encode()).hexdigest()
    if hashed == hash_to_match:
        return plain


def read_wordlist(file_path):
    with open(file_path, "r") as wordlist:
        for line in wordlist:
            line = line.strip()
            yield line


if __name__ == "__main__":
    try:
        file_path = argv[1]
    except IndexError:
        file_path = input("Enter a file path: ")
    try:
        hash_to_match = argv[2]
    except IndexError:
        hash_to_match = input("Enter a hash to match: ")
    for word in read_wordlist(file_path):
        result = hash_sha256(word)
        if result:
            print(f"Found: {word}")
            exit(0)
    print("No match found")
