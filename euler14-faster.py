# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:39:25 2019

@author: Tommy
"""

import time


def recurse(i, chains, count):
    if i in chains:
        return chains[i] + count

    if(i>1):
        #even
        if (i%2 == 0):
            chains[i] = recurse(i/2, chains, 1)
            return chains[i] + count
        #odd
        else:
            chains[i] = recurse(3*i+1, chains, 1)
            return chains[i] + count
    return count
    




def main():
    
    start = time.time()
    
    chains = {}
    final = 0
    num = 0
    
    maxNum = 1000000
        
    for i in range(maxNum):
        recurse(i, chains, 0)
        
    for x in chains:
        if((chains[x] > final) and x <= maxNum):
            final = chains[x]
            num = x
    end = time.time()
    print(num)
    print(final)
    print(end-start)
    
if __name__ == "__main__":
    main()
    
    
#Answer is 837799, with a chain of 524