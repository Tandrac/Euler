# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:16:18 2019

@author: Tommy
"""

#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#
#What is the value of the first triangle number to have over five hundred divisors?


import math

def factor(triangle):
    #how many factors a number has
    count = 0
    # only have to go to square root to find half the factors
    for i in range(1,int(math.sqrt(triangle))):
        if(triangle%i == 0):
            count += 1
    #multiply count by 2 to include factors complement to already found factors
    count = count*2
    #a check so that the square root of the triangle isnt counted twice
    if(triangle/math.sqrt(triangle) == math.sqrt(triangle)):
        count-=1
    return count

def main():
    i = 1
    triangle = 0
    count = 0
    while(count < 500):
        triangle = i+triangle
        count = factor(triangle)
        i=i+1
    print(triangle)
    
if __name__ == "__main__":
    main()
    
    
#Answer: 76576500