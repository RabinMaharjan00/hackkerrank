# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:59:11 2019

@author: Rabin maharjan
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from statistics import median

n=int(input("Enter the value"))
value = [int(x) for x in input().split()]
value.sort()
valuelen = int(len(value)/2)

if len(value)%2==0:
    L=value[:valuelen]
  
    U = value[valuelen:]
    
else:
    L=value[:valuelen]
    
    U=value[valuelen+1:]
   

print(int(median(L)))
print(int(median(value)))
print(int(median(U)))