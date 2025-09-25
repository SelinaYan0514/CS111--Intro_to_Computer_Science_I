#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:47:20 2023

@author: yansitong
"""
#function 1
def abs_list_lc(values):
    """ return a list containing the absolute values of the numbers in values
        input values: a list of numbers
    """
    return [abs(x) for x in values]


#function 2
def abs_list_rec(values):
    """ return a list containing the absolute values of the numbers in values
        input values: a list of numbers 
    """
    if values == []:
        return []
    else:
        rest_list = abs_list_rec(values[1:])
        if values[0] < 0:
            return [-values[0]] + rest_list
        else:
            return [values[0]] + rest_list
        
        
#function 3
def num_mult_lc(m, values):
    """ return the number of integers in values that are multiples of m
        input m and values: an integer m and a list of integers values 
    """

    return len([x for x in values if x % m == 0])


#function 4
def num_mult_rec(m, values):
    """ return the number of integers in values that are multiples of m
        input m and values:  an integer m and a list of integers values
    """
    if values == []:
        return 0
    else:
        rest_list = num_mult_rec(m, values[1:])
        if values[0] % m == 0:
            return 1 + rest_list
        else:
            return 0 + rest_list
        
        
#function 5
def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

def most_vowels(words):
    """ returns the string in the list with the most vowels
        input words: a list of one or more strings called 
    """
    scored_vowels = [[num_vowels(x),x] for x in words]
    max_vowels = max(scored_vowels)
    return  max_vowels[1]


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("abs_list_lc([-2, 5, 8, -3]) returns", abs_list_lc([-2, 5, 8, -3]))
    
    #function 2
    print("abs_list_rec([-2, 5, 8, -3]) returns", abs_list_rec([-2, 5, 8, -3]))
    
    #function 3
    print("num_mult_lc(5, [2, 15, 10]) returns", num_mult_lc(5, [2, 15, 10]))
    
    #function 4
    print("num_mult_rec(5, [2, 15, 10]) returns", num_mult_rec(5, [2, 15, 10]))
    
    #function 5
    print("most_vowels(['obama', 'bush', 'clinton']) returns", most_vowels(['obama', 'bush', 'clinton']))