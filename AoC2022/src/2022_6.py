'''
Created on Dec 1, 2021

@author: barrda

'''
import numpy as np
from email.header import UTF8
from numpy import byte
from curses.ascii import ascii

DEBUG = 0

packetLength = 14

def PRT(s):
    if DEBUG:
        print(s)
        
#-------------------------------------

def compareToRestOfPacket(i, j, data):
    for k in range(j+1,i+packetLength):
        PRT('  k='+str(k))
        if data[j] == data[k]:
            PRT('same ' + data[j] + ' at ' + str(j) + str(k))
            return False
    return True 


def part1(input):
    f = open(input)
    data = f.readline()    
    l = len(data)
    for i in range(0,l-packetLength+1):
        a = data[i]
        b = data[i+1]
        c = data[i+2]
        d = data[i+3]
        if (a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d):
            return i+packetLength
    return 0 

def part2(input):
    f = open(input)
    data = f.readline()    
    l = len(data)
    for i in range(0,l-packetLength):
        PRT('i='+str(i)+'-------------')            
        isDiff = True
        for j in range(i,i+packetLength-1):
            PRT(' j='+str(j))            
            if not compareToRestOfPacket(i, j, data):
                isDiff = False
        if isDiff:
            return i+packetLength    
    return 0

    
if __name__ == '__main__':
    if DEBUG:
        input = "../data/test"
#        input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    else:
        input = "../data/input_data_6"   

print("Part 1 =", part1(input))
print("Part 2 =", part2(input))

pass
    