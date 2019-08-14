# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:50:35 2019

@author: Tommy
"""

#The following iterative sequence is defined for the set of positive integers:
#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.



#probably gonna be a recursion problem

#to speed up, index found "chains" so it doesnt have to recalculate
#maybe a massive array (size 1 million?) and have the index be length of chain so far

def countDown(i, count):
    if(i > 1):
        #if even
        if(i%2 == 0):
            count = countDown(i/2, count+1)
        #if odd
        else:
            count = countDown(3*i+1, count+1)
    return count
def main():
    final = 0
    num = 0
    for i in range(1000000):
        count = countDown(i,0)
        if(count > final):
            final = count
            num = i
    print(final)
    print(num)

if __name__ == "__main__":
    main()
    
#Answer is 837799, with a chain of 524