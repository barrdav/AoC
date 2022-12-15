'''
Created on Dec 1, 2021

@author: barrda

Use of numpy for 2 dim array.
Convert byte to ascii char with chr()

'''
import numpy as np
from email.header import UTF8
from numpy import byte
from curses.ascii import ascii

DEBUG = 0

nbStacks     = 9
maxStackSize = 60

def PRT(s):
    if DEBUG:
        print(s)
        
#-------------------------------------
def findHead(stack):
    i = maxStackSize - 1
    while (stk[stack][i] == 0) and (i >= 0):
        i -= 1
    print("head of ", stack, " = ", i)
    return i
    
def crane9000(stackFrom, stackTo):
    sf = int(stackFrom) - 1
    st = int(stackTo)   - 1
    headFrom = findHead(sf)
    headTo   = findHead(st)
    stk[st][headTo+1] = stk[sf][headFrom]
    stk[sf][headFrom] = 0    

def crane9001(nb, stackFrom, stackTo):
    sf = int(stackFrom) - 1
    st = int(stackTo)   - 1
    nb = int(nb)
    headFrom = findHead(sf)
    headTo   = findHead(st)
    PRT("head from " + str(headFrom) + " head to " + str(headTo))
    stk[st][headTo+1:headTo+nb+1] = stk[sf][headFrom-nb+1:headFrom+1]
    stk[sf][headFrom-nb+1:headFrom+1] = np.zeros(nb)  

def getResult():
    r = ""
    for i in range(0,nbStacks):
         r += chr(int(stk[i][findHead(i)]))
    return r

def part1(input):    
    with open(input) as f:
        datalines = f.readlines()
        for instruct in datalines:
            if not "move" in instruct:
                continue
            PRT(instruct)
            l = instruct.split()
            print("Move ", l[1], " crane ")
            for nb in range(0,int(l[1])):
                crane9000(l[3], l[5])
                PRT(stk)

        return getResult()

def part2(input):
    with open(input) as f:
        datalines = f.readlines()
        for instruct in datalines:
            if not "move" in instruct:
                continue
            PRT(instruct)
            l = instruct.split()
            print("Move ", l[1], " crane ")
            crane9001(l[1], l[3], l[5])
            PRT(stk)

        return getResult()

    return


    

'''
[P]     [C]         [M]            
[D]     [P] [B]     [V] [S]        
[Q] [V] [R] [V]     [G] [B]        
[R] [W] [G] [J]     [T] [M]     [V]
[V] [Q] [Q] [F] [C] [N] [V]     [W]
[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
[H] [D] [L] [D] [W] [R] [R] [P] [C]
[F] [L] [H] [R] [Z] [J] [J] [D] [D]
 1   2   3   4   5   6   7   8   9 
'''
if __name__ == '__main__':
    if DEBUG:
        stk = np.zeros((3,maxStackSize),dtype=int)
        stk[0][0:2] = [ord('Z'), ord('N')]
        stk[1][0:3] = [ord('M'), ord('C'), ord('D')]
        stk[2][0:1] = [ord('P')]
    else:
        stk = np.zeros((nbStacks,maxStackSize))
        stk[0][0:8] = [ord('F'), ord('H'), ord('B'), ord('V'), ord('R'), ord('Q'), ord('D'), ord('P')]
        stk[1][0:6] = [ord('L'), ord('D'), ord('Z'), ord('Q'), ord('W'), ord('V')]
        stk[2][0:8] = [ord('H'), ord('L'), ord('Z'), ord('Q'), ord('G'), ord('R'), ord('P'), ord('C')]
        stk[3][0:7] = [ord('R'), ord('D'), ord('H'), ord('F'), ord('J'), ord('V'), ord('B')]
        stk[4][0:4] = [ord('Z'), ord('W'), ord('L'), ord('C')]
        stk[5][0:8] = [ord('J'), ord('R'), ord('P'), ord('N'), ord('T'), ord('G'), ord('V'), ord('M')]
        stk[6][0:7] = [ord('J'), ord('R'), ord('L'), ord('V'), ord('M'), ord('B'), ord('S')]
        stk[7][0:3] = [ord('D'), ord('P'), ord('J')]
        stk[8][0:5] = [ord('D'), ord('C'), ord('N'), ord('W'), ord('V')]
    PRT(stk)
    if DEBUG:
        input = "../data/test"
    else:
        input = "../data/input_data_5"   

#print("Part 1 =", part1(input))
print("Part 2 =", part2(input))

pass
    