#!/usr/bin/env python

import math


class Circle(object):
    u"""Create a circle with a given radius."""

    def __init__(self, radius):
        self.radius = radius

    def set_diameter(self, diameter):
        self.radius = diameter / 2.0

    def get_diameter(self):
        return self.radius * 2.0

    def get_area(self):
        return math.pi*(self.radius**2)

    diameter = property(get_diameter, set_diameter)
    area = property(get_area)

    def __repr__(self):
        return "Circle(%s)" % self.radius

    def __str__(self):
        return "Circle with radius: %.6f" % self.radius
