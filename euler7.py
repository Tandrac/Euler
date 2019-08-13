# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 15:19:19 2019

@author: Tommy
"""

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10,001st prime number?


import math
import sys
sys.path.append('../CSCI6230-Final')
import primality


def main():
    prime = 0
    p = 0
    i = 1
    test = []
    while(p<10001):
        #Had to modify to handle psuedoprimes
        if(primality.millerRobin(i)):
            test.append(i)
            p += 1
            prime = i
        i+=1
    print(prime)
    print(primality.millerRobin(2047))
    #print(test)




if __name__ == "__main__":
    main()
    
    
#Real answer is 104743
#My answer is 104593
#TODO like problem 10, might need to rework my miller rabin