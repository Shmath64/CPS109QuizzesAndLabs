# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:44:37 2023

@author: m1davis
"""
import math

#polygon area finder
"""Read number of sides (int)
read in side length
calculate perimeter 
calculate apothem (center to midpoint of a side)
two decimal points of precision
"""
#Get necessary inputs (Number of Sides and their length) and cast as int or float
numOfSides = int(input("Number of sides: ")) 
sideLength = float(input("Side Length: "))

apothem = sideLength/(2*math.tan(math.pi/numOfSides)) #Calculate Apothem
perimeter = sideLength*numOfSides #Calculate perimeter 
area = (apothem * perimeter) / 2 #Find area using apothem and perimeter

#Print the Perimeter and Area to screen
print(f"Perimeter: {perimeter}")
print(f"Area: {area:.2f}")
