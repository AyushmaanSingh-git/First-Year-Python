#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:29:06 2026
@author: ayushmaan-singh
"""

# This is the Parent class (Base class)
class Animal:
    def speak(self):
        print("I am Confused")
        
    def eat(self):
        print("I eat food")

# This is the Child class (Derived class). 
# By putting (Animal) in the parentheses, Dog inherits everything from Animal.
class Dog(Animal):
    # The Dog class overrides the parent's speak() method with its own version.
    def speak(self):
        print("BHOW BHOW")
        
    # Notice we didn't write an eat() method here. 
    # Because it inherits from Animal, a Dog object can still use eat()!