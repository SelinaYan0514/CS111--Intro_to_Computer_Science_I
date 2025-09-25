#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:18:37 2023

@author: yansitong
"""

#function 1
def compare(s1, s2):
    """ returns the string that comes later in the dictionary
        inputs s1 and s2: two string values 
    """
    if s1 >= s2:
        return s1
    else:
        return s2

    
#function 2
def combine(s1, s2, n):
    """ returns a new string in which the last n characters of s1 are followed
    by the first n characters of s2
        inputs s1, s2, and n: two strings s1 and s2 and an integer n
    """
    return s1[-n:] + s2[:n]


#function 3
def reverse_n(vals,n):
    """ returns a new list in which the first n values of vals are reversed
    and all other values from vals remain in their original positions.
        inputs vals and n : a list vals and an integer n
    """
    vals[:n] = vals[n-1::-1]
    return vals


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("compare('program', 'code') returns", compare('program', 'code'))
    
    #function 2
    print("combine('go', 'terriers', 5) returns", combine('go', 'terriers', 5))
    
    #function 3
    print("reverse_n([10, 20, 30, 40], 6) returns", reverse_n([10, 20, 30, 40], 6))
    