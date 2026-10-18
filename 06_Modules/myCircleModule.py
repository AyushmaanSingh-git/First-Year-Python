#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:47:07 2026
@author: ayushmaan-singh
"""

# We define a constant variable that can be used by all functions below
pi = 3.14

def area(r):
    # Calculates the area of a circle (π * r^2)
    return pi * r * r

def circum(r):
    # Calculates the circumference of a circle (2 * π * r)
    return 2 * pi * r

def sphereVol(r):
    # Calculates the volume of a sphere (4/3 * π * r^3)
    # The ** operator is used for exponents in Python
    return (4/3) * pi * r ** 3

def sphereArea(r):
    # Calculates the surface area of a sphere (4 * π * r^2)
    return 4 * pi * r * r