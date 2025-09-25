#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 23:18:56 2023

@author: yansitong
"""

#function 1
def get_even_val():
    """
    obtain an even integer from the user
    inputs: No inputs
    """
    var = int(input('Enter an even integer:'))
    
    while var % 2 == 1:
        var = int(input('The input must be even. Try again:'))
    
    return var


#function 2
def add_powers(m, n):
    """ 
    add together the first m powers of n (from n**0 up to and including n**(m-1)
power) and that returns the resulting sum
    inputs m and n:  a positive integer m and an arbitrary integer n,
    """
    result = 0
    
    for i in range(m):
        print(n, "**", i,"=", n ** i)
        result += n ** i
    
    return result


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("get_even_val() returns", get_even_val()) 
    
    #function 2
    print("add_powers(6, 3) returns", add_powers(6, 3))
