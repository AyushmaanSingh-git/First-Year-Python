#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:41:38 2026
@author: ayushmaan-singh
"""

def enter_age(age):
    # We set a strict rule: age must be between 0 and 100.
    if age < 0 or age > 100:
        # 'raise' artificially triggers an error if the rule is broken.
        raise ValueError("Age should be between 0 and 100")
    
    print("age is now set to : ", age)

# The 'try' block attempts to run risky code that might cause an error.
try:
    enter_age(150) # This will fail because 150 > 100

# The 'except' block catches the specific error (ValueError) so the program doesn't crash.
except ValueError:
    print("You're NOT human")