# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:24:03 2019

@author: Tommy
"""

#A palindromic number reads the same both ways. The largest palindrome made from
#the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    product = 0
    palin = []
    #go through all 3 digit #s (ew n^2)
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            product = i*j
            #check if product is a palindrome
            if (palindromeCheck(str(product))):
                #print(product)
                palin.append(product)
    palin.sort(reverse=True)
    print(palin[0])           

#this functon just checks if one of the digits in a number is
#the same as the "opposite" digit to make a palindrome
def palindromeCheck(word):
    length = len(word)
    for i in range(length):
        if(word[i] != word[length-i-1]):
            return False
    return True

if __name__ == "__main__":
    main()
    
    
#Fianl answer is 906609