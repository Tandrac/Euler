# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:26:30 2019

@author: Tommy
"""
import math
import sys
sys.path.append('../CSCI6230-Final')
import primality
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def main():
    num = 600851475143
    #only need the complement up to the square
    for i in range(int(math.sqrt(num)),0,-1):
        #check if i is actually a multiple of num
        if(num%i == 0):
            com1 = 0
            com2 = 0
            #use the miller rabin (I know its spelled wrong) function from crypto class
            if(primality.millerRobin(i)):
                com1 = i
            #have to check complement
            #by this step num/i should be an int, but need to "force" it to be for miller rabin
            if(primality.millerRobin(int(num/i))):
                com2 = num/i
            #have to check that the complement isnt a bigger prime than the found number
            #ex: 22 -> 2 and 11, need to make sure that the algorythm is finding 11
            if(com1+com2 != 0):
                if(com1>com2):
                    print(com1)
                else:
                    print(com2)
                break
    
if __name__ == "__main__":
    main()
    
    
    
#Answer = 6857