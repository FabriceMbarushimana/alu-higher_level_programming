#!/usr/bin/python3
"""Return the list of attributes and methods of an object"""

def lookup(obj):
    """Return the list of available attributes and methods of the given object."""
    return list(dir(obj))
