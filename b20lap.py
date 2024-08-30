# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:21:13 2024

@author: VanAnh
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

gtln = a

if b > gtln:
    gtln = b
if c > gtln:
    gtln = c

print("Số lớn nhất là:", gtln)
