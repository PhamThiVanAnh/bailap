# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:34:40 2024

@author: VanAnh
"""

N = int(input("Nhập số nguyên dương N (có 2 chữ số): "))
if  10 <= N<= 99:
    hangchuc = N // 10
    hangdonvi = N % 10
    tong = hangchuc + hangdonvi
    print("Tổng các chữ số của N là:",tong)
else:
    print("Số nhập vào không hợp lệ.")