# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:00:17 2023

@author: 64mda
"""
import math

def checkPrime(num):
    upperBound = math.floor(math.sqrt(num))
    if num < 3: return True #1 and 2 are prime
    if num % 2 == 0: return False
    
    for i in range(3, upperBound+1, 2): #Checking odd numbers from 3 to root (inclusive)
        if num % i == 0: return False
    return True
        