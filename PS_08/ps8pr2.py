#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 18:31:29 2023

@author: yansitong
"""
import random 

#function 1
def create_dictionary(filename):
    """ returns a dictionary of key-value pairs in which:
        1. each key is a word encountered in the text file
        2. the corresponding value is a list of words that follow the key word
        in the text file.
    """
    file = open(filename,'r')
    text = file.read()
    file.close()
    words = text.split()
    
    d = {}
    w = '$'
    
    for next_word in words:
        if w not in d:
            d[w] = [next_word]
        else:
            d[w] += [next_word]
        
        if next_word[-1] not in '.?!':  # check if the word is a sentence-ending word
           w = next_word
        else:
           w = '$'
    
    return d


#function 2
def generate_text(word_dict, num_words):
    """ use word_dict to generate and print num_words words, with a space after
        each word. The function must print the words that it generates. It must 
        not return a value.
    """
    
    current_word = '$'
    for i in range(num_words):
        wordlist = word_dict.get(current_word, ['$'])
        next_word = random.choice(wordlist)
        print(next_word, end=' ')
        if next_word[-1] in '.?!':
            current_word = '$'
        else:
            current_word = next_word
    print()
