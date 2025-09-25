#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:51:49 2023

@author: yansitong
"""

#function 1
def letter_score(letter) :
    """ returns the value of that letter as a scrabble tile
        input letter:  a lowercase letter
    """
    assert(len(letter) == 1)
    if letter in ['a','e','i','l','n','o','r','s','t','u']:
        return 1
    elif letter in ['d','g']:
        return 2
    elif letter in ['b','c','m','p']:
        return 3
    elif letter in ['f','h','v','w','y']:
        return 4
    elif letter in ['k']:
        return 5
    elif letter in ['j','x']:
        return 8
    elif letter in ['q','z']:
        return 10
    else:
        return 0


#function 2
def scrabble_score(word):
    """ return the scrabble score of that string – i.e., the sum of the 
    scrabble scores of its letters
        input word: a string contains only lowercase letters
    """
    if word == '':
        return 0
    else:
        scrabble_rest = scrabble_score(word[1:])
        return letter_score(word[0]) + scrabble_rest
    
    
#function 3
def BUtify(s):
    """ return a new string in which all lower-case bs are replaced by 
    upper-case Bs and all lower-case us are replaced by upper-case Us
        input s: an arbitrary string
    """
    if s == '':
        return ''
    else:
        BUtify_rest = BUtify(s[1:])
        if s[0] in 'b':
            return 'B' + BUtify_rest
        elif s[0] in 'u':
            return 'U' + BUtify_rest
        else:
            return s[0] + BUtify_rest
        

#function 4
def diff(vals1, vals2):
    """ return a new list in which each element is the the absolute value of 
    the difference of the corresponding elements from the original lists
        inputs vals1 and vals2: two arbitrary lists of non-negative integers 
    """
    if vals1 == []:
        return vals2
    elif vals2 == []:
        return vals1
    else:
        diff_rest = diff(vals1[1:],vals2[1:])
        if vals1[0] >= vals2[0]:
            return [vals1[0]-vals2[0]] + diff_rest
        else:
            return [-1*(vals1[0]-vals2[0])] + diff_rest

        
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("letter_score('q') returns", letter_score('q'))
    
    #function 2
    print("scrabble_score('quetzal') returns", scrabble_score('quetzal'))
    
    #function 3
    print("BUtify('beautiful') returns", BUtify('beautiful'))
    
    #function 4
    print("diff([3, 1, 9], [2, 4, 5, 7]) returns", diff([3, 1, 9], [2, 4, 5, 7]))
   
    
    
    
    