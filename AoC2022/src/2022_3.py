'''
Created on Dec 1, 2021

@author: barrda

'''

DEBUG = 0

def PRT(s):
    if DEBUG:
        print(s)

def getPrio (c):
    if c > 'a':
        prio = ord(c) - ord('a') + 1
    else:
        prio = ord(c) - ord('A') + 27 
    return prio
        
def findError (partA, partB):
    for item in partA:
        if item in partB:
            prio =  getPrio(item)
            print("error found ", item, prio)            
            return prio

def findBadge (A, B, C):
    for item in A:
        if (item in B) and (item in C):
            prio = getPrio(item)
            PRT("badge found: " + item + " = " + str(prio))
            return prio

def part1(input):    
    with open(input) as f:
        datalines = f.readlines()
        totalScore = 0        
        for s in datalines:
            l = len(s.rstrip())
            PRT("length = " + str(l))
            partSize = int(l/2)
            PRT(partSize)
            partA = s[:partSize]
            partB = s[partSize:]
            totalScore += findError(partA, partB)
    return totalScore

def part2(input):
    with open(input) as f:
        datalines = f.readlines()
        totalScore = 0        
        A = ''
        B = ''
        C = ''
        for s in datalines:
            PRT(s)
            if not A:
                A = s
            elif not B:
                B = s
            else:
                C = s
                totalScore += findBadge(A, B, C)
                A = ''
                B = ''
                C = ''
                
    return totalScore

    
if __name__ == '__main__':
    if DEBUG:
        input = "../data/test"
    else:
        input = "../data/input_data_3"   

#print("Part 1 =", part1(input))
print("Part 2 =", part2(input))

pass
    