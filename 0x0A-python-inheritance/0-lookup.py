#!/usr/bin/python 3

"""module 0-lookup.py returns the list of available attributes and 
methods of an object
"""
def lookup(obj):
   """Returns list of attributes and methods
   
   Args:
      obj: The instance/Object
   """
    return dir(obj)
