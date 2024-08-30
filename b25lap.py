# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:54:52 2024

@author: Van Anh
"""
a = input("Nhập một chữ cái: ")

if a.islower():
    print(a.upper())
elif a.isupper():
    print(a.lower())
else:
    print("Đây không phải là một chữ cái.")
