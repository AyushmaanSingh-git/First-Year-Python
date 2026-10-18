#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:11:56 2026
@author: ayushmaan-singh
"""

# Importing the tools needed to create abstract classes
from abc import ABC, abstractmethod

# SecuritySystem is an Abstract Base Class (blueprint)
class SecuritySystem(ABC):
    
    # @abstractmethod forces any child class to build their own 'trigger_alarm' function.
    # You cannot actually use this base class on its own.
    @abstractmethod
    def trigger_alarm(self):
        pass

# DoorSensor follows the blueprint and provides its own specific alarm logic.
class DoorSensor(SecuritySystem):
    def trigger_alarm(self):
        return "ALERT! Front door breached!"

# SmokeDetector inherits the blueprint but uses 'pass'. 
# Because it fails to actually write code for trigger_alarm(), 
# Python will throw an error if you try to use SmokeDetector in a real program!
class SmokeDetector(SecuritySystem):
    pass