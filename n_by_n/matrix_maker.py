#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:15:48 2018

@author: caranix

Used after running minichainfinal.py in order to take each districting plan
and reshape eachrow into 18by18. This becomes input for "Cleaned up Ising Playground" (ask Marshall) 
"""

file_to_check = "run5_18x18_unique_districtings.csv"
file_to_write_to = "output_matrix.csv" 

# Every line in the file represents one map, so split each line and sum the 
# number of members of each district, ultimately the sum in each plan of the 
# members of each district is stored in an array inside the totals array
file = open(file_to_check, 'r')
ofile= open(file_to_write_to, 'w')
for line in file: #list as csv
    values = line.split(',')
    for j in range(0,323,18):
        #print(list(range(0,343,18)))
        ofile.write( ','.join(values[j: j+18]) + '\n')    
ofile.close() 
file.close()
    

