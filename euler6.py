# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 15:13:47 2019

@author: Tommy
"""



def main():
    squared = 0
    sums = 0
    for i in range (1,101):
        squared += i**2
        sums += i
    sums = sums**2
    final = sums - squared
    print(final)




if __name__ == "__main__":
    main()
    
    
#Answer is 25164150