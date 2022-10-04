#!/usr/bin/python3
"""Takes URL, sends a request to URL and displays
the X-Request-Id variable found in the header of the response"""

if __name__ == "__main__":
    import urllib
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.header.get('X-Request-Id')
        print(head)
