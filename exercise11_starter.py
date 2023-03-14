#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
w = len(Belgium)
x = int(Belgium[8:16])
y = int(Belgium[26:32])
z = (x + y)

print(w)
print("-"*w)
print(Belgium.replace(',', ':'))
print(x+y)
print(Belgium.count('e'))
print(Belgium[0:25])
print(Belgium.swapcase())
print(Belgium.upper())
