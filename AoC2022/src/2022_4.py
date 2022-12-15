'''
Created on Dec 1, 2021

@author: barrda
'''

DEBUG = 0

def PRT(s):
    if DEBUG:
        print(s)
        
#-------------------------------------
def getRange(data):
    r = data.split('-')
    r[0] = int(r[0])
    r[1] = int(r[1])
    PRT("range " + str(r))
    return r
    
def part1(input):    
    with open(input) as f:
        datalines = f.readlines()
        totalScore = 0      
        for pair in datalines:
            pair = pair.rstrip().split(',')
            PRT(pair)
            A = getRange(pair[0])
            B = getRange(pair[1])
            PRT(A)
            PRT(B)
            if (A[0] <= B[0]) and (A[1] >= B[1]):
                totalScore += 1
                PRT("+1")
            elif (B[0] <= A[0]) and (B[1] >= A[1]):
                totalScore += 1
                PRT("+1")

    return totalScore

def part2(input):
    with open(input) as f:
        datalines = f.readlines()
        totalScore = 0        
        for pair in datalines:
            pair = pair.rstrip().split(',')
            PRT(pair)
            A = getRange(pair[0])
            B = getRange(pair[1])
            PRT(A)
            PRT(B)
            if (A[1] >= B[0]) and (A[0] <= B[1]):
                totalScore += 1
                PRT("+1")
            elif (B[1] >= A[0]) and (B[0] <= A[1]):
                totalScore += 1
                PRT("+1")
                 
    return totalScore

    
if __name__ == '__main__':
    if DEBUG:
        input = "../data/test"
    else:
        input = "../data/input_data_4"   

print("Part 1 =", part1(input))
print("Part 2 =", part2(input))

pass
    