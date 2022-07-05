#!/usr/bin/python3
"""1-write_file writes a string to a text file (UTF8) and
returns the number of characters written
"""

def write_file(filename="", text=""):
    """Writes a string to a text file
    Args:
        filename: The file
        text: The string
    Return: Number of characters
    """
    with open(filename, 'w+') as f:
        return f.write(text)
