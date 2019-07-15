# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:40:50 2019

@author: Tommy
"""

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.



def main():
    multiples = set()
    for i in range(334):
        if (i*3 < 1000):
            multiples.add(i*3)
        if(i*5<1000):
            multiples.add(i*5)
    sum = 0
    for j in multiples:
        sum += j
    print(sum)

if __name__ == "__main__":
    main()