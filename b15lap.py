# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:47:26 2024

@author: Van Anh
"""
a = float(input("nhap so a:"))
b = float(input("nhap so b:"))
A = ((a+b)/(a**1/3-b**1/3)-(((a*b)**1/3)/(a**1/3+b**1/3)*2))
print("Gia tri bieu thuc la:", A)