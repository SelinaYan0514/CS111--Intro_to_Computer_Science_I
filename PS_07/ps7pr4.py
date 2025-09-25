#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 18:16:20 2023

@author: yansitong
"""

def file_processing(filename, cityname, state):
    file = open(filename, 'r')
    
    count = 0
    
    for line in file:
        line = line[:-1]
        
        fields = line.split(',')
        
        if fields[2] == cityname and fields[3] == state:
            pop = int(float(fields[4]) * 1000)           
            print(fields[0] + '\t' + fields[1] + '\t' + format(pop, '10,d'))
            count += 1
    if count == 0:
             print("no result found for", cityname, ',', state)
            
    file.close()
    
    
def main():
    filename = input("Enter the name of data file:")
    
    while True:
        
        cityname = input("city:")
    
        if cityname == 'quit':
            break
        
        state = input("state abbreviation:")
    
        file_processing(filename, cityname, state)
    