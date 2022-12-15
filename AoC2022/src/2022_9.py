'''
Created on Dec 1, 2021

@author: barrda

'''

DEBUG = 0

if DEBUG:
    B_SIZE = int(40)
else:
    B_SIZE = int(800)
B_SIZE_HALF = int(B_SIZE/2)
# index in rope
X = 0
Y = 1

def markTail():
    B[pos[TAIL][Y]][pos[TAIL][X]] = '#'
    print(pos)
#    if DEBUG:
#        for i in range(0,B_SIZE):
#            print(B[i]) 

def moveR(steps):
    for i in range(0, steps):
        pos[HEAD][X] += 1
        for k in range (HEAD, TAIL):
            if pos[k+1][Y] == pos[k][Y]:
                if pos[k][X] > pos[k+1][X]:
                    pos[k+1][X] = pos[k][X]-1
            else:
                if pos[k][X] > pos[k+1][X]+1:
                    pos[k+1][X] += 1
                    pos[k+1][Y] = pos[k][Y]
        markTail()
        
def moveL(steps):
    for i in range(0, steps):
        pos[HEAD][X] -= 1
        for k in range (HEAD, TAIL):
            if pos[k+1][Y] == pos[k][Y]:
                if pos[k][X] < pos[k+1][X]:
                    pos[k+1][X] = pos[k][X]+1
            else:
                if pos[k][X] < pos[k+1][X]-1:
                    pos[k+1][X] = pos[k][X]+1
                    pos[k+1][Y] = pos[k][Y]
        markTail()
        
def moveU(steps):
    for i in range(0, steps):
        pos[HEAD][Y] += 1
        for k in range (HEAD, TAIL):
            if pos[k+1][X] == pos[k][X]:
                if pos[k][Y] > pos[k+1][Y]:
                    pos[k+1][Y] = pos[k][Y]-1
            else:
                if pos[k][Y] > pos[k+1][Y]+1:
                    pos[k+1][Y] = pos[k][Y]-1
                    pos[k+1][X] = pos[k][X]            
        markTail()

def moveD(steps):
    for i in range(0, steps):
        pos[HEAD][Y] -= 1
        for k in range (HEAD, TAIL):
            if pos[k+1][X] == pos[k][X]:
                if pos[k][Y] < pos[k+1][Y]:
                    pos[k+1][Y] = pos[k][Y]+1
            else:
                if pos[k][Y] < pos[k+1][Y]-1:
                    pos[k+1][Y] = pos[k][Y]+1
                    pos[k+1][X] = pos[k][X]            
        markTail()            
    
def inContact(k):
    if abs(pos[k][X] - pos[k+1][X]) > 1 \
    or abs(pos[k][Y] - pos[k+1][Y]) > 1:
        return False
    else:
        return True 
    
def moveTail(k):
    if not inContact(k):        
        if pos[k][X] > pos[k+1][X]+1:
            pos[k+1][X] += 1
            if pos[k+1][Y] < pos[k][Y]:
                pos[k+1][Y] += 1
            elif pos[k+1][Y] > pos[k][Y]:
                pos[k+1][Y] -= 1
            return
        elif pos[k][X] < pos[k+1][X]-1:
            pos[k+1][X] -= 1
            if pos[k+1][Y] < pos[k][Y]:
                pos[k+1][Y] += 1
            elif pos[k+1][Y] > pos[k][Y]:
                pos[k+1][Y] -= 1
            return
        if pos[k][Y] > pos[k+1][Y]+1:
            pos[k+1][Y] += 1
            if pos[k+1][X] < pos[k][X]:
                pos[k+1][X] += 1
            elif pos[k+1][X] > pos[k][X]:
                pos[k+1][X] -= 1
            return
        elif pos[k][Y] < pos[k+1][Y]-1:
            pos[k+1][Y] -= 1
            if pos[k+1][X] < pos[k][X]:
                pos[k+1][X] += 1
            elif pos[k+1][X] > pos[k][X]:
                pos[k+1][X] -= 1
            return
                
def moveR2(steps):
    for i in range(0, steps):
        pos[HEAD][X] += 1
        for k in range (HEAD, TAIL):
            moveTail(k)
        markTail()
        
def moveL2(steps):
    for i in range(0, steps):
        pos[HEAD][X] -= 1
        for k in range (HEAD, TAIL):
            moveTail(k)
        markTail()
        
def moveU2(steps):
    for i in range(0, steps):
        pos[HEAD][Y] -= 1
        for k in range (HEAD, TAIL):
            moveTail(k)
        markTail()

def moveD2(steps):
    for i in range(0, steps):
        pos[HEAD][Y] += 1
        for k in range (HEAD, TAIL):
            moveTail(k)
        markTail()            
    
             

def part1(input):
    nbPosVisited = 0 
    with open(input) as f:
        moves = f.readlines()
        for m in moves:
            mvt = m.split()
            s = int(mvt[1])
            if mvt[0] == 'R':
                moveR(s)
            elif mvt[0] == 'L':
                    moveL(s)
            elif mvt[0] == 'U':
                    moveU(s)
            elif mvt[0] == 'D':
                    moveD(s)
            else:
                print('EROR')
                return                        

    for i in range(0,B_SIZE):
        for j in range(0,B_SIZE):
            if B[i][j] == '#':
                nbPosVisited += 1

    return nbPosVisited

def part2(input):
    nbPosVisited = 0 
    with open(input) as f:
        moves = f.readlines()
        for m in moves:
            mvt = m.split()
            s = int(mvt[1])
            print(mvt[0], ' ', s)
            if mvt[0] == 'R':
                moveR2(s)
            elif mvt[0] == 'L':
                    moveL2(s)
            elif mvt[0] == 'U':
                    moveU2(s)
            elif mvt[0] == 'D':
                    moveD2(s)
            else:
                print('ERROR')
                return                        

    for i in range(0,B_SIZE):
        for j in range(0,B_SIZE):
            if B[i][j] == '#':
                nbPosVisited += 1

    return nbPosVisited


if __name__ == '__main__':
    if DEBUG:
        input = "../data/test"
    else:
        input = "../data/input_data_9"   

    B = [[]]
    for i in range(0,B_SIZE):
        B.append([])
        for j in range(0,B_SIZE):
            B[i].append('.')
    HEAD = 0
    TAIL = 1
    pos = []    
    for i in range(HEAD, TAIL+1):
        pos.append([B_SIZE_HALF,B_SIZE_HALF])
        print(pos)    
    markTail()
    print("Part 1 =", part1(input))
    
    B = [[]]
    for i in range(0,B_SIZE):
        B.append([])
        for j in range(0,B_SIZE):
            B[i].append('.')
    HEAD = 0
    TAIL = 9
    pos = []    
    for i in range(HEAD, TAIL+1):
        pos.append([B_SIZE_HALF,B_SIZE_HALF])
        print(pos)    
    markTail()
    print("Part 2 =", part2(input))    

pass
    