# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 00:33:40 2024

@author: YenTrinh
"""
print("Tính tiền taxi")
a=float(input("Số km đi được là "))
if a==1:
    print("Tiền taxi là 20k")
if a==2 or a==3:
    b=a*13
    print("Tiền taxi là ",b,"k")
if a>=4 and a<=8:
    b=a*12
    print("Tiền taxi là ",b,"k")
if a>8 and a<=100:
    b=a*10
    print("Tiền taxi là ",b,"k")
if a>100:
    b=(a*10)-(a*10*8/100)
    print("Tiền taxi là ",b,"k")
