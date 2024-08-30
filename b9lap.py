# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:17:59 2024

@author: Admin
"""
print("=========== MENU ===========")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("============================")
choice = int(input( "Moi nhap lua chon:"))
print("============================")
if choice == 1:
    print("Ban chon Hu tieu")
elif choice == 2:
    print("Ban chon Chao long")
elif choice == 3:
    print("Ban chon Banh canh")
elif choice == 4:
    print("Ban chon Bun rieu")
elif choice == 5:
    print("Ban chon Pho bo")
else:
    print("Lua chon khong co trong menu")           