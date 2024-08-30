# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:44:53 2024

@author: VanAnh
"""

hour = int(input("Nhập giờ: "))
minute = int(input("Nhập phút: "))
second = int(input("Nhập giây: "))
if 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60:
    print("Thời gian hợp lệ.")
else:
    print("Thời gian không hợp lệ.")