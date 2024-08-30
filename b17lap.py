# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:52:22 2024

@author: 
"""

a=int(input("Nhap so thu nhat:"))
b=int(input("Nhap so thu hai:"))
c=int(input("Nhap so thu ba:"))
solonnhat = max(a,b,c)
sonhonhat= min(a,b,c)
solonnhat = a if a > b and a > c else b if b > c else c
sonhonhat = a if a < b and a < c else b if b < c else c
print("Số lớn nhất:",solonnhat)
print("Số nhỏ nhất:",sonhonhat)