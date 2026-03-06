# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

a = float(input("Kerem az a valtozot\n"))
b = float(input("Kerem a b valtozot\n"))
delta = int(input('delta: '))

if math.fmod(a, b) == 0:
    print("A oszthato b-vel")

try:
    print(a/b)
    
except ZeroDivisionError:
    print("Nullaval nem osztunk!")
    

c = math.sqrt(a **2 + b**2)


print(f"c = {c}")
print((a**2 + b**2)**0.5)

print(f"Kerulet: {2*(a+b)}")

print('terület1=',a*b*math.sin(math.radians(delta)))

