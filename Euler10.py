# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:41:13 2019

@author: Tommy
"""

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.


#TODO: try rewriting miller rabin, also maybe recheck problem 7

import math
import sys
sys.path.append('../CSCI6230-Final')
import primality

def main():
    sums = (0)
    for i in range(2000000):
        #slow, even when using Miller Rabin
        if(primality.millerRobin(i)):
            print(i)
            sums += i
    print(sums)
        


if __name__ == "__main__":
    main()
    
    
    #Im getting 142,969,196,269 for my answer
    #The real answer is 142,913,828,922
    #I feel like my issue might be that my miller rabin cant handle very large numbers
