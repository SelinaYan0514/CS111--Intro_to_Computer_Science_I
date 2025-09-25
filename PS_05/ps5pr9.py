#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:27:16 2023

@author: yansitong
"""

#function 1
def sum_squares(vals):
    """
    return the sum of the squares of the individual numbers in the list
    input vals: a list of numbers 
    """
    total = 0
    
    for x in vals:
        total += x**2

    return total 


#function 2
def double(s, target):
    """
    return a new string in which all occurrences of target in s are doubled/repeated
    inputs s and target: an arbitrary string s and and a single-character string target
    """
    result = ''
    
    for c in s:
        if c == target:
            result += 2*c
        else:
            result += c
            
    return result


#function 3
def process(vals, x):
    """
    return a new list in which each element of the original list that is larger
 than x is replaced with a 0
     inputs vals and x: a list of 0 or more integers vals and a single integer x
    """
    result = []
    
    for c in vals:
        if c > x:
            result += [0]
        else:
            result += [c]
        
    return result


#function 4
def diff(vals1, vals2) :
    """
    return a new list in which each element is the the absolute value of the  
difference of the corresponding elements from the original lists
    inputs vals1 and vals2: two arbitrary lists of non-negative integers 
    """
    result = []
    
    len_shorter = min(len(vals1),len(vals2))
    for i in range(len_shorter):
        result += [abs(vals1[i] - vals2[i])]
        
    if len(vals1) > len_shorter:
        result += vals1[len_shorter:]
        
    elif len(vals2) > len_shorter:
        result += vals2[len_shorter:]

    return result

    

    


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print(" sum_squares([1, 2, 3, 4]) returns", sum_squares([1, 2, 3, 4])) 
    
    #function 2
    print("double('banana', 'a') returns", double('banana', 'a'))
    
    #function 3
    print("process([5, 8, 3, 12], 15) returns", process([5, 8, 3, 12], 15))
    
    #function 4
    print("diff([3, 1, 9], [2, 4, 5, 7]) returns", diff([3, 1, 9], [2, 4, 5, 7]))
