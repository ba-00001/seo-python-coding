#!/usr/bin/python3
"""
Module: inherits_from

This module provides a function for checking
if an object is an instance of a class that
inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a class that inherited
         (directly or indirectly) from the specified class. False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
