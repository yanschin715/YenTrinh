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
    b= 3*13+ (a-3)*12
    print("Tiền taxi là ",b,"k")
if a>8:
    b= 3*13+ (a-3)*12+ (a-8)*10
    print("Tiền taxi là ",b,"k")
if b>100:
    b=b*92/100
    print("Tiền taxi sau khi được giảm là ",b,"k")
