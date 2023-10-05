# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:50:41 2023

@author: m1davis
"""

#conditions:
#   8 Characters, one lower case letter, one upper case letter, one digit (0-9)

initialEntry = input("Enter your new password: ")
secondEntry = input("Re-enter your new password: ")

def isSuitablePassword(password: str):
    hasUpper = False
    hasLower = False
    hasDigit = False
    for c in password:
        if c.isnumeric(): hasDigit = True
        elif c.isupper(): hasUpper = True
        elif c.islower(): hasLower = True
            
    if hasUpper and hasLower and hasDigit and len(password) > 8:
        return True
    return False

if initialEntry != secondEntry:
    print("Passwords must match")
    
elif not isSuitablePassword(initialEntry):
    print("Password not complex enough")
    
else:
    print("Password changed successfuly")

#"Password changed successfully"