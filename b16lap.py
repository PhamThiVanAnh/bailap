# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:08:29 2024

@author: VanAnh
"""
import math
h= int(input("Nhap gio:"))
p= int(input("Nhap phut:"))
s=int(input("Nhap giay:"))
print(f"{h}h{p}p{s}s")
tonggiay= h*3600 + p*60 + s
print("Tong giay: ", tonggiay)
