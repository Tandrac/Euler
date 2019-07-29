# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:57:28 2019

@author: Tommy
"""
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


#If I understand this correctly, I need a+b+c =1000, and a^2+b^2=c^2, and a<b<c

import math

#Make sure the summation of squares a and b is a perfect square, c
def perfectSquare(n):
    num = int(math.sqrt(n))
    if(num*num == n):
        return True
    else: return False
    
def main():
    powers = []
    for i in range(1,1001):
        powers.append(i*i)
    for i in powers:
        for j in powers:
            cSquare = i+j
            if(perfectSquare(cSquare)):
                a = int(math.sqrt(i))
                b = int(math.sqrt(j))
                c = int(math.sqrt(cSquare))
                if(a+b+c == 1000):
                    print("Product: ",a*b*c," With numbers ",a,b,c)
#                   

if __name__ == "__main__":
    main()
    
    
#Answer: Product is 31875000  With numbers  200 375 425