# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:20:39 2023

@author: m1davis
"""
"""
Read in a temperature from the user in Celsius. Calculate and print the temperature in
Fahrenheit, and Kelvin. Think about what type seems most appropriate for representing
temperature, and why. Read the value using the input() function, but don’t forget that
input() returns string! You will have to convert accordingly
"""

def GetInputCelsius():
    

celsius = input("Degrees Celsius: ")
try:
    celsius = float(celsius)
except:
    print("Invalid Input")
    celsius = input("Degrees Celsius: ")
    
fahrenheit = celsius*(9/5) + 32
kelvin = celsius + 273.15

print(f"{fahrenheit}°F \n{kelvin} Kelvin")