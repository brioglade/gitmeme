#!/usr/bin/python 
l = []
for a in range (100,1000):
    if (a/100%10)**3 + (a/10%10)**3 + (a%10)**3 == a:
        l.append(a)

print l