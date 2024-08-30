# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:36:44 2024

@author: VanAnh
"""
a=int(input("nhap ngay sinh:"))
b=int(input("nhap thang sinh:"))
c=int(input("nhap nam sinh:"))
caua = "{}/{}/{}".format(a,b,c)
print(caua)
caub= "{}/{}/{}".format(a,b,c%100)
print(caub)
cauc= "{}/{}/{}".format(c,b,a)
print(cauc)