#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 15:38:00 2023

@author: yansitong
"""

def dec_to_bin(n):
    """ returning a string version of the binary representation of that number
        input n: an integer 
    """
    if n == 1:
        return '1'
    elif n == 0:
        return '0'
    else:
        bin_rest = dec_to_bin(n // 2)
        if n % 2 == 1:
            return bin_rest + '1'
        else:
            return bin_rest + '0'
        

def bin_to_dec(b):
    """ returning the resulting integer
        input b: a string b that represents a binary number 
    """
    if b == '1':
        return 1
    elif b == '0':
        return 0
    else:
        bin_rest = bin_to_dec(b[:-1])
        if b[-1] == '1':
            return bin_rest * 2 + 1
        elif b[-1] == '0':
            return bin_rest * 2


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("dec_to_bin(0) returns", dec_to_bin(0))
    
    #function 2
    print("bin_to_dec('1100') returns", bin_to_dec('1100'))
