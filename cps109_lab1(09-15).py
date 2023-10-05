# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:20:39 2023

@author: m1davis
"""
import math

#functions used in multiple questions:
def GetFloatInput(message): #takes prompt string for input as parameter
    inputString = input(message)
    try: #try/except statement ensures the input can be converted to float without crashing
        inputFloat = float(inputString)
        return inputFloat #returns the inputted value as a float
    except:
        print("Invalid Input, please enter an integer or float")
        return GetFloatInput(message) #try again if it can't be converted to float

#Q1 
""" 
Read in a temperature from the user in Celsius. Calculate and print the temperature in
Fahrenheit, and Kelvin. Think about what type seems most appropriate for representing
temperature, and why. Read the value using the input() function, but don’t forget that
input() returns string! You will have to convert accordingly"""

"""
print("-CELSIUS TO FAHRENHEIT & KELVIN CONVERTER-")

celsius = GetFloatInput("Degrees Celsius: ") #gets input celsius as float
fahrenheit = celsius*(9/5) + 32 #converts to fahrenheit 
kelvin = celsius + 273.15 #converts to kelvin

print(f"{fahrenheit}°F \n{kelvin} Kelvin") #print output to console
"""

#Q2
"""
Request three values from the user (once again, choose your types appropriately). These
three values represent polynomial coefficients (a, b, c in the equation below). Using these
coefficients, evaluate the quadratic formula and print the roots. Notice what happens when
the discriminant (b2-4ac) is negative""" 
"""
print("-QUADRATIC FORMULA-")
aInput = GetFloatInput("Input a: ")
bInput = GetFloatInput("Input b: ")
cInput = GetFloatInput("Input c: ")

def PrintRoots(a,b,c):
    discriminant = b**2 - (4*a*c)
    if discriminant < 0:
        print(f"Discriminant is {discriminant} which is less than 0; no real roots.")
        return
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"one root at x={root}")
        return
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots at x = {root1} & x = {root2}")
    
PrintRoots(aInput,bInput,cInput)
"""

#Q3
"""Request three more values from the user. If these three values could represent the sides of
a triangle, print True. Otherwise, print False. You do not need if/else for this!"""


print("-TRIANGLE POSSIBLE?-")
print("note: negative values are invalid and will be automatically converted to positive numbers")

legs = [] #list that stores all three legs
#Get all three leg lengths from user
legs.append(abs(GetFloatInput("Input Length of leg1: ")))
legs.append(abs(GetFloatInput("Input Length of leg2: ")))
legs.append(abs(GetFloatInput("Input Length of leg3: ")))
longestLeg = 0 #initalize variable that will hold the longest leg measurement
longestLegIndex = 0 #index of that leg in list
for leg in legs: #for loop finds the longest leg and its index
    if leg > longestLeg:
        longestLeg = leg
        longestLegIndex = legs.index(leg)
        
legs.pop(longestLegIndex) #remove longest leg from list
twoLegSum = legs[0] + legs[1] #finds the sum of the smaller legs
if twoLegSum > longestLeg:
    print(f"A triangle CAN be made because {legs[0]} + {legs[1]} > {longestLeg}")
elif twoLegSum == longestLeg:
    print(f"A triangle CANNOT be made because {legs[0]} + {legs[1]} = {longestLeg} (you have merely a line)")
else:
    print(f"A triangle CANNOT be made because {legs[0]} + {legs[1]} < {longestLeg}")



















