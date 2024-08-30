# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:02:43 2024

@author: VanAnh
"""

a=int(input("Nhap so thu nhat:"))
b=int(input("Nhap so thu hai:"))
c=int(input("Nhap so thu ba:"))
d=int(input("Nhap so thu tu:"))
somin = a
if b < somin:
    somin = b
if c < somin:
    somin = c
if d < somin:
    somin = d
    somin = d
print("So co gia tri nho nhat:",somin)