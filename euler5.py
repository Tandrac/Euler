# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:46:31 2019

@author: Tommy
"""

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10
#without any remainder. What is the smallest positive number that is evenly
#divisible by all of the numbers from 1 to 20?


def main():
    i = 1
    while(1):
        if(divCheck(i)):
            print(i)
            break
        i += 1

def divCheck(num):
    for i in range(1,21):
        if(num%i != 0):
            return False
    return True

if __name__ == "__main__":
    main()