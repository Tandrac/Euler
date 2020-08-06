# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:03:11 2020

@author: Tommy
"""

def main():
    count = 0
    for i in range(1,1001):
        #rounding temp probably unnessicary, but might speed up larger values?
        temp = (i**i)%10000000000
        count += temp
    print(count%10000000000)

#Answer is 9110846700

if __name__ == "__main__":
    main()
    