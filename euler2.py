# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:14:54 2019

@author: Tommy
"""

#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.


def main():
    i = 1
    old_i = 1
    evens = 0
    while(i<4000000):
        temp = i
        i = i+old_i
        old_i = temp
        if(i%2==0):
            evens+=i
    print(evens)
if __name__ == "__main__":
    main()
    
    
    
#Answer = 4613732