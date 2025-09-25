#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:53:29 2023

@author: yansitong
"""

from ps4pr1 import bin_to_dec
from ps4pr1 import dec_to_bin

#function 1
def  div_bin(b1, b2):
    """ return the result in the form of a string that represents a binary number
        inputs b1 and b2: two strings that represent binary integers
    """
    d1 = bin_to_dec(b1)
    d2 = bin_to_dec(b2)
    result = dec_to_bin(d1 // d2)
    return result


#function 2
def largest(binvals):
    """ returns the string in binvals that represents the largest binary number
        input binvals:  a list of one or more strings 
    """
    list = [[bin_to_dec(x),x] for x in binvals]
    largepair = max(list)
    return largepair[1]


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print ("div_bin('1001', '10') returns", div_bin('1001', '10'))
    
    #function 2
    print("largest(['1100', '110', '101', '10000']) returns", largest(['1100', '110', '101', '10000']))