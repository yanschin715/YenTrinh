# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:56:07 2024

@author: YenTrinh
"""
print("Kiểm tra abc có phải là ba cạnh của một tam giác")
a=float(input("Nhập a = "))
b=float(input("Nhập b = "))
c=float(input("Nhập  c = "))
if (a+b)>c and (a+c)>b and (b+c)>a :
      if (a**2==b**2+c**2) or (b**2==a**2+c**2) or (c**2==a**2+b**2) :
          print("{}, {}, {} là ba cạnh của một tam giác vuông".format(a, b, c))
      if a==b==c :
          print("{}, {}, {} là ba cạnh của một tam giác đều".format(a, b, c))
      if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
          print("{}, {}, {} là ba cạnh của một tam giác cân".format(a, b, c))
else:
      print("{}, {}, {} không là ba cạnh của một tam giác".format(a, b, c))
    