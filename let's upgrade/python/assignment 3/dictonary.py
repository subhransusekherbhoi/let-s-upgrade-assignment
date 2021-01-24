# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:55:20 2021

@author:subhransu
"""

list1 = [1,2,3,4,5] 
list2 = ["a", "b", "c", "d", "e"] 
merge={list1[i]:list2[i] for i in range(len(list2))}
print(merge)