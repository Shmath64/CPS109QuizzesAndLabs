# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:58:44 2023

@author: m1davis
"""

N = int(input("Enter N: "))


def FizzBuzz(N):
    if N < 1:
        print("N Must be greater than 1")
        return
    if N > 100:
        print("Too much work, no thanks")
        return
    
    
    for i in range(1,N+1):
        stringToPrint = ""
        if i % 3 != 0 and i % 5 != 0:
            print(i)
        else: 
            if i % 3 == 0: 
                stringToPrint += "Fizz"
            if i % 5 == 0:
                stringToPrint += "Buzz"
            print(stringToPrint)
            
FizzBuzz(N)