#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:01:16 2023

@author: m1davis
"""

def faroShuffle(lst, outShuffle):
    secondHalf = lst[len(lst)//2:]
    firstHalf = lst[:len(lst)//2]
    
    shuffledList = []
    for i in range(len(lst)):
        if outShuffle:
            if i % 2 == 0: shuffledList.append(firstHalf[i//2])
            else: shuffledList.append(secondHalf[i//2])
        else:
            if i % 2 == 0: shuffledList.append(secondHalf[i//2])
            else: shuffledList.append(firstHalf[i//2])
    return shuffledList
            