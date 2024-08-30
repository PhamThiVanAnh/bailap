# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:23:05 2024

@author: VanAnh
"""
so = int(input("Nhap 4 so xe:"))
nguyen1 = so // 1000
du1 = so %1000
nguyen2 = so //100
du2 = so % 100
nguyen3 = so //10
du3 = so %10
nguyen4 = du3
tinh = nguyen1 + nguyen2 + nguyen3 + nguyen4
cuoi = tinh %10 + tinh//10
print("So nut 4 chu so =",cuoi)

