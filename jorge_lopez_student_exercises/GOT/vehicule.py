#! /usr/bin/env python
# Author: BersuitX
# Description: This about script copy and optionally filter
# source collection to a destination collection using different methods.
"""
    Vehicle Base Class
"""

class Vehicle:
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None