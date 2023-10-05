# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:56:33 2023

@author: m1davis
"""

num = int(input("Enter a positive integer: "))
factors = []
for i in range(2,11): # check all posible factors from 0-10
    if num % i == 0:
        factors.append(i)
        
if len(factors) == 0: #if prime
    print("This number has no factors between 2 and 10")
else:
    outputString = f"The factors of {num} between 2 and 10 are: "

    for f in factors:
        outputString += f"{f}, "
    outputString = outputString[0:-2] ##Cuts off end

    print(outputString)
        
