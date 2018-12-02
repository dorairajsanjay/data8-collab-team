# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:50:45 2018

@author: sjmcuser
"""

s = 'a2b3c'
temp = 0
count = 0
alphabets = "abcdefghijklmnopqrstuvwxyz"
for letter in s:
    if type(s) == int:
        temp += letter
print(temp)