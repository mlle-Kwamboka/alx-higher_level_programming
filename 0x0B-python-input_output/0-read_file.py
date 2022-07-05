#!/usr/bin/python3
"""Module 0-read_file reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """Reads a file.
    Args:
        filename - File to be read
    """
    
    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
