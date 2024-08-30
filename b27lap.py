# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:57:06 2024

@author: Admin
"""

import math

a = input("Nhập hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ")

if a == 'v':
    b = float(input("Nhập cạnh hình vuông: "))
    P = 4 * b
    S = b*b

elif a == 'n':
    c = float(input("Nhập chiều rộng: "))
    d = float(input("Nhập chiều dài: "))
    P = 2 * (c + d)
    S = c * d

elif a == 't':
    r = float(input("Nhập bán kính hình tròn: "))
    P = 2 * math.pi * r
    S = math.pi * r * r

else:
    print("Hình không hợp lệ")
    P = S = None

if P is not None and S is not None:
    print("Kết quả P =",P ," S = ",S)
