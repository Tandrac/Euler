# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:39:25 2019

@author: Tommy
"""


def recurse(i, chains, count):
    if i in chains:
        return chains[i] + count

    if(i>1):
        #even
        if (i%2 == 0):
            count = recurse(i/2, chains, count+1)
        #odd
        else:
            count = recurse(3*i+1, chains, count+1)
    return count
    




def main():
    chains = {}
    final = 0
    num = 0
    
    maxNum = 999999
    
    for i in range(maxNum):
        chains[i] = recurse(i, chains, 0)
        
    for x in chains:
        if((chains[x] > final) and x <= maxNum):
            final = chains[x]
            num = x
    print(num)
    print(final)
if __name__ == "__main__":
    main()
    
    
#Answer is 837799, with a chain of 524