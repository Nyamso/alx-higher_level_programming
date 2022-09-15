#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-square.py
This module contains an class
A class that defines a square by:
-Private instance attribute: size
-Instantiation with size (no type/value verification)
"""

class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
