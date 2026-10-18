#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:48:14 2026
@author: ayushmaan-singh
"""

# This is the Parent class (Base class) representing a 2D vector
class Vector:
    # The __init__ method sets up the initial state (attributes) of the object
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # def norm(self):

# This is the Child class (Derived class) representing a 3D vector.
# By putting (Vector) in parentheses, it inherits from the Vector class.
class Vec3D(Vector):
    def __init__(self, x, y, z):
        # super() is a shortcut that calls the parent class's __init__ method.
        # This automatically sets up self.x and self.y for us!
        super().__init__(x, y)
        
        # Now we only have to add the new 3rd dimension (z) specific to Vec3D
        self.z = z