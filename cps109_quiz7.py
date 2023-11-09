# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 12:52:56 2023

@author: 64mda
"""

def rlen(items):
    #NO LEN
    #NO LOOPS
    #Recursion!
    
    try:
        items.pop(0)
        return 1 + rlen(items)
    except:
        return 0
    
    
    #Matthew Davis