# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:54:47 2024

@author: YenTrinh
"""
print("Giải phương trình ax + b = 0")
a=float(input("Nhap a = "))
b=float(input("Nhap b = "))
if (a==0) and (b!=0):
    print("Phương trình vô nghiệm")
if (a==0) and (b==0):        
    print("Phương trình thỏa mãn với mọi x")
if a!=0:
    x=-b/a
    print("Phương trình có nghiệm x = ", x)
