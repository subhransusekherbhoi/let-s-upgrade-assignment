# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:55:20 2021

@author:subhransu
"""


data = data2 = "" 
with open('file1.txt') as fp: 
    data = fp.read() 
with open('file2.txt') as fp: 
    data2 = fp.read() 
data += "\n"
data += data2 
with open ('file3.txt', 'w') as fp: 
    fp.write(data)