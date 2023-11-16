# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:59:03 2023

@author: 64mda
"""

def next_item(it):
    try:
        return next(it)
    except:
        return None