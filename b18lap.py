# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:24:04 2024

@author: VanAnh
"""
import math
h1=int(input("nhap gio thu nhat:"))
p1=int(input("nhap phut thu nhat:"))
s1=int(input("nhap giay thu nhat:"))
T1= h1*3600 + p1*60 +s1
h2=int(input("nhap gio thu hai:"))
p2=int(input("nhap phut thu hai:"))
s2=int(input("nhap giay thu hai:"))
T2=h2*3600 + p2*60 + s2
Cong= T1+T2
Tru= T1-T2
print("Tong 2 khung gio qua giay:",Cong)
print("Hieu 2 khung gio qua giay:",Tru)