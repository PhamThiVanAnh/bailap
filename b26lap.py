# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:32:26 2024

@author: VanAnh
"""
a=float(input("nhap a:"))
b=float(input("nhap b:"))
c=float(input("nhap c:"))
if a>b:
    a, b = b, a
if a>c:
    a,c = c, a
if b>c:
    b, c = c, b
print("Thu tu tang dan cua ba so la :", a, b, c)   
