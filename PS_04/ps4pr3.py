#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:40:57 2023

@author: yansitong
"""

#function 1
def num_odds_rec(binvals):
    """ return the number of bitstrings in the list that represent an odd number
        input binvals:  a list of 0 or more strings
    """
    if len(binvals) == 0:
        return 0
    else:
        rest_num_odds_rec = num_odds_rec(binvals[1:])
        if binvals[0][-1] == '0':
            return rest_num_odds_rec + 0
        else:
            return rest_num_odds_rec + 1
        

#function 2
def  num_odds_lc(binvals):
    """ return the number of bitstrings in the list that represent an odd number
        input binvals: a list of 0 or more strings
    """
    return sum([1 for x in binvals if x[-1] == '1'])


#function 3
def add_bitwise(b1, b2):
    """ return the result of the addition of two binary numbers
        inputs b1 and b2: two binary numbers represented by strings
    """
    if b1 == '':
        return b2
    elif b2 == '':
        return b1 
    else:
        rest_add_bitwise = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            return add_bitwise(rest_add_bitwise, '1') + '0'
        if b1[-1] == '0' and b2[-1] == '0':
            return rest_add_bitwise + '0'
        else:
            return rest_add_bitwise + '1'
        

# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("num_odds_rec(['1100', '10011', '101', '010', '110']) returns", num_odds_rec(['1100', '10011', '101', '010', '110']))
    
    #function 2
    print("num_odds_lc(['1100', '10011', '101', '010', '110']) returns", num_odds_lc(['1100', '10011', '101', '010', '110']))
    
    #function 3
    print("add_bitwise('11100', '11110') returns", add_bitwise('11100', '11110'))