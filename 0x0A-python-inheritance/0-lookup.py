#!/usr/bin/python3

"""module 0-lookup.
returns the list of available attributes and 
methods of an object
"""
def lookup(obj):
   """Returns list of attributes and methods
   
   Args:
      obj: The instance/Object
   """
   return dir(obj)
