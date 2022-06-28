#!/usr/bin/python3

"""module text_indentation prints a text of two lines
after each of any of the given delimiters"""

def text_indentation(text):
    """Prints text with added two newlines
        after each of these characters: { '.', '?', ':'}"""

        if type(text) is not str:
            raise TypeError("text must be a string")

        for delim in ".:?":
            Text = (delim + "\n\n".join([line.strip(" ") for line in text.split(delim)])
        print("{}".format(text), end="")
