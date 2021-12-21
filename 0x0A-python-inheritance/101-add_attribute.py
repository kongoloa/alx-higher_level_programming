#!/usr/bin/python3
"""Provide a function that adds new attribute to an obj"""


def add_attribute(ob, attr, value):
    """add attribute to class else raises error"""
    if hasattr(ob, "__dict__"):
        setattr(ob, attr, value)
    else:
        raise TypeError("can't add new attribute")
