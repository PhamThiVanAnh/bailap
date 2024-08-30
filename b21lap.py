# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:35:59 2024

@author: VanAnh
"""

n = int(input("Nhập số nguyên: "))

chuoi = ["Khong doc duoc", "Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin"]

if 0 <= n <= 9:
    print(chuoi[n])
else:
    print(chuoi[0])