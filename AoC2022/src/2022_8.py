'''
Created on Dec 1, 2021

@author: barrda

Use of numpy for 2 dim array.

'''
import numpy as np
from numpy import byte

DEBUG = 0

def seeFromTop(forest, i, j):
    for k in range (0, i):
        if forest[i][j] <= forest[k][j]:
            return False
    print('can see ', i, ' ', j, ' from T')
    return True

def seeFromBottom(forest, i, j, end):
    for k in range (i+1, end):
        if forest[i][j] <= forest[k][j]:
            return False
    print('can see ', i, ' ', j, ' from B')
    return True

def seeFromLeft(forest, i, j):
    for k in range (0, j):
        if forest[i][j] <= forest[i][k]:
            return False
    print('can see ', i, ' ', j, ' from L')
    return True

def seeFromRight(forest, i, j, end):
    for k in range (j+1, end):
        if forest[i][j] <= forest[i][k]:
            return False
    print('can see! ', i, ' ', j, ' from R')
    return True

def lookAtTop(forest, i, j):
    for k in range (i-1, 0, -1):
        if forest[i][j] <= forest[k][j]:
            return i-k
    return i    # reach border

def lookAtBottom(forest, i, j, end):
    for k in range (i+1, end):
        if forest[i][j] <= forest[k][j]:
            return k-i
    return end-i-1    # reach border

def lookAtLeft(forest, i, j):
    for k in range (j-1, 0, -1):
        if forest[i][j] <= forest[i][k]:
            return j-k
    return j

def lookAtRight(forest, i, j, end):
    for k in range (j+1, end):
        if forest[i][j] <= forest[i][k]:
            return k-j
    return end-j-1



def part1(input):
    nbTree = 0    
    with open(input) as f:
        theForest = f.readlines()
        nbTreeH = len(theForest[0].strip('\n'))
        nbTreeV = len(theForest)
        for i in range(0, nbTreeV):
            for j in range(0, nbTreeH):
                print(theForest[i][j])
                if seeFromLeft(theForest, i, j) \
                or seeFromRight(theForest, i, j, nbTreeH) \
                or seeFromTop(theForest, i, j) \
                or seeFromBottom(theForest, i, j, nbTreeV):
                    nbTree += 1
    return nbTree

def part2(input):
    scenicScoreMax = 0    
    with open(input) as f:
        theForest = f.readlines()
        nbTreeH = len(theForest[0].strip('\n'))
        nbTreeV = len(theForest)
        for i in range(0, nbTreeV):
            for j in range(0, nbTreeH):
                l = lookAtLeft(theForest, i, j) 
                r = lookAtRight(theForest, i, j, nbTreeH) 
                t = lookAtTop(theForest, i, j) 
                b = lookAtBottom(theForest, i, j, nbTreeV)
                scenicScore = l * r * t * b
                print('score for ', i, '|', j, ' = ', l, ' ', r, ' ', t, ' ', b, ' = ', scenicScore)
                if scenicScore > scenicScoreMax:
                    scenicScoreMax = scenicScore
    return scenicScoreMax


if __name__ == '__main__':
    if DEBUG:
        input = "../data/test"
    else:
        input = "../data/input_data_8"   

print("Part 1 =", part1(input))
print("Part 2 =", part2(input))

pass
    