# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:53:06 2024

@author: YT
"""
print("Giải phương trình ax^2 + bx + c")
import cmath
a=float(input("Nhập a = "))
b=float(input("Nhập b = "))
c=float(input("Nhập c = "))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình có vô số nghiệm")
        else:
            x=-c/b
            print("Phương trình có nghiệm x= ", x)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    if delta > 0: 
        sqrt_delta = cmath.sqrt(delta)
        x1=(-b+math_sqrt(delta))/2*a
        x2=(-b-math_sqrt(delta))/2*a
        print("Phương trình có nghiệm x1 = ", x1)
        print("Phương trình có nghiệm x2 = ", x2)
    if delta==0:
        x=-b/2*a
        print("Phương trình có nghiệm kép x1 = x2 = ",x)
