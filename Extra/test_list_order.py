# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 12:10:17 2018

@author: rajar
"""

# Check how to find two consecutive items in a list

v = [1,2,3,4,3,1,2]

m = any([2,3,3] == v[i:i+3] for i in range(len(v) - 1))

print(m)
