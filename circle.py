"""
Program name: Geometry Calculator
Author: Rediet Ayele
Purpose: Contains functions: Calculates and returns the area,Calculates and returns the circumference.
Date: 06/20/26
"""
import math

def calc_area(radius):
    area = math.pi * radius ** 2
    return area

def calc_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference