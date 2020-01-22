# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:52:28 2019

@author: Tommy
"""
#
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
#there are exactly 6 routes to the bottom right corner.
#
#How many such routes are there through a 20×20 grid?


def goRight(pos, count, paths, path):
    num = 2
    if(pos[0] < num):
        pos[0] += 1
        newPath = (path, (pos[0],pos[1]))
        goRight(pos, count, paths, newPath)
        goDown(pos, count, paths, newPath)
    elif(pos[1] < num):
        goDown(pos, count, paths, path)
    if(pos[0] == num and pos [1] == num):
        count.append(1)
        paths.append(path)
    
def goDown(pos, count, paths, path):
    num = 2
    if(pos[1] < num):
        pos[1] += 1
        newPath = (path, (pos[0],pos[1]))
        goRight(pos, count, paths, newPath)
        goDown(pos, count, paths, newPath)
    elif(pos[0] < num):
        goRight(pos, count, paths, path)
    if(pos[0] == num and pos [1] == num):
        count.append(1)
        paths.append(path)


def main():
    #pos[0] = right to left
    #pos[1] = up and down
    count = []
    paths = []
    pos = [0,0]
    goRight(pos, count, paths, (0,0))
    goDown(pos, count, paths, (0,0))
    print(len(count))
    for x in paths:
        print(x)
    
    
    
    
if __name__ == "__main__":
    main()