#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:08:54 2023

@author: yansitong
"""

#function 1
def rem_first(c, s):
    """ return a version of s in which only the first occurrence of c (if any) 
    has been removed
        inputs c and s: a single character c and an arbitrary string s
    """
    if s == '':
        return ''
    else:
        rem_rest = rem_first(c, s[1:])
        if s[0] == c:
            return s[1:]
        else:
            return s[0] + rem_rest
        

#function 2
def jscore(s1, s2):
    """ return the Jotto score of s1 compared with s2. i.e., the number of 
    characters in s1 that are shared by s2. The positions and the order of the 
    shared characters within each string do not matter. Repeated letters are 
    counted multiple times, as long as they appear multiple times in both strings.
        inputs s1 and s2: two strings s1 and s2
    """ 
    if len(s1) == 0 or len(s2) == 0:
        return 0
    else:
        if s1[0] in s2:
            jscore_rest = jscore(s1[1:], rem_first(s1[0], s2))
            return 1 +  jscore_rest
        else:
            jscore_rest = jscore(s1[1:], s2 )
            return jscore_rest
     
        
#function 3
def locate_first(elem, seq):
    """ return the index of the first occurrence of elem in seq
        inputs elem and seq: inputs an element elem and a sequence seq
    """
    if len(seq) == 0:
        return -1
    elif seq[0] == elem:
        return 0
    else:
        locate_first_rest = locate_first(elem, seq[1:])
        if locate_first_rest == -1:
           return -1
        else:
            return 1 + locate_first_rest
          

#function 4
def double_final(n, values):
    """ return a version of values in which only the final occurrence of n 
    (if any) has been doubled
        inputs n and values: an integer n and an arbitrary list of integers values
    """
    if values == []:
        return [] 
    else:
        double_final_rest = double_final(n, values[0:-1])
        if values[-1] == n:
            return values[0:-1] + [2*n]
        else:
            return double_final_rest + [values[-1]]
        
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("rem_first('x', 'bananas') returns", rem_first('x', 'bananas')) 

    #function 2
    print("jscore('recursion', 'excursion') returns", jscore('recursion', 'excursion'))   
    
    #function 3
    print("locate_first('hi', ['hello', 111, True]) returns", locate_first('hi', ['hello', 111, True]))
    
    #function 4
    print("double_final(2, [2, 3, 1, 2, 3, 5]) returns", double_final(2, [2, 3, 1, 2, 3, 5]))
    
    
    
    
    

   
    