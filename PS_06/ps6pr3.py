#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:30:11 2023

@author: yansitong
"""

#function 1
def repeat(s,n):
    """
    uses a loop to create and return a string in which n copies of s have been 
concatenated together
    inputs s and n:  a string s and an integer n
    """
    result = ''
    for i in range(n):
        result += s
        
    return result


#function 2
def contains(s, c):
    """
    uses a loop to determine if s contains the character c, returning True if 
it does and False if it does not
    inputs s and c: an arbitrary string s and a single-character c
    """
    for x in s:
        if x == c:
            return True
    
    return False


#function 3
def add(vals1, vals2):
    """
    uses a loop to construct and return a new list in which each element is the 
sum of the elements at the corresponding positions in the original lists
    inputs vals1 and vals2: two lists of numbers
    """
    result = []
    if len(vals1) > len(vals2):
        vals2 = [0] * (len(vals1) - len(vals2)) + vals2
    else:
        vals1 = [0] * (len(vals2) - len(vals1)) + vals1
    
    for i in range(len(vals1)):
        result += [vals1[i] + vals2[i]]
        
    return result


#function 4
def replace(vals, old, new):
    """
    modifies the list so that all occurrences of old are replaced with new, and
all other elements are left unchanged. Note that this function should not 
return a value. 
    inputs vals, old, and new: a list of integers called vals and two integers old and new
    """
    for i in range(len(vals)):
        if vals[i] == old:
            vals[i] = new
        
        
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("repeat('Go BU!', 4) returns", repeat('Go BU!', 4)) 
    
    #function 2
    print("contains('hello', 'x') returns", contains('hello', 'x')) 
    
    #function 3
    print("add([7, 5, 3], [6]) returns", add([7, 5, 3], [6])) 
    
    