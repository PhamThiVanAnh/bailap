# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:03:10 2024

@author: VanAnh
"""
namsinh= int(input("Nhap nam sinh:"))
namhientai= 2023
if 0 < namsinh <= 2023:
    tuoi= namhientai - namsinh
    print(" Ban sinh nam ",namsinh,"vay ban", tuoi,"tuoi")
else:
    print("Nam sinh khong hop ")
