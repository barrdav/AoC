'''
Created on Dec 1, 2021

@author: barrda

'''

DEBUG = 0

#-------------------------------------
if DEBUG:
    X_MAX = int(30)
    X_OFFSET = 485
    Y_MAX = 20
else:
    X_MAX = int(700)
    X_OFFSET = 0
    Y_MAX = 180

X = 0
Y = 1

def printCave():
    for i in range(0,Y_MAX):
        print(cave[i])
    print()
    return

# draw a line with "#" from beging to end
def drawLine(beg, end, ymax):
    a = beg.split(',')
    b = end.split(',')
    ax = int(a[X]) - X_OFFSET
    bx = int(b[X]) - X_OFFSET 
    ay = int(a[Y])
    by = int(b[Y]) 
    if ay > ymax:
        ymax = ay
    if by > ymax:
        ymax = by
        
    print(ax, ay, '->', bx, by)
    if bx > ax:
        for x in range(ax, bx+1):
            cave[ay][x] = '#'
    elif ax > bx:
        for x in range(bx, ax+1):
            cave[ay][x] = '#'
    else:
        if by > ay:
            for y in range(ay, by+1):
                cave[y][ax] = '#'
        else:
            for y in range(by, ay+1):
                cave[y][ax] = '#'
        
    return ymax           

def checkEndCondition(part, y, ymax):
    end = False
    if part == 1:
        if y > ymax:
            end = True
    else:
        if y == 0:
            end = True
    return end
        
def fallingSand(ymax, part):
    nbUnit = 0
    end = False
    while(not end):
        x = 500 - X_OFFSET
        y = 0  
        resting = False
        while(not resting):
            if cave[y+1][x] == '.':
                y += 1            
            elif cave[y+1][x-1] == '.':
                y += 1
                x -= 1
            elif cave[y+1][x+1] == '.':
                y += 1
                x += 1
            else:
                resting = True
                nbUnit += 1
            end = checkEndCondition(part, y, ymax)
            if end:
                break
        cave[y][x] = 'o'                    
#        printCave()
    
    return nbUnit    
        
def part1(input):
    ymax = int(0)
    # Draw the rock structure
    with open(input) as f:
        datalines = f.readlines()
        for line in datalines:
            lines = line.split(' -> ')
            for i in range(1,len(lines)):
                ymax = drawLine(lines[i-1], lines[i], ymax)

#    printCave()
    
    # simuate the sand
    result = fallingSand(ymax, 1)

#    printCave()
    
    return result

def part2(input):
    ymax = int(0)
    # Draw the rock structure
    with open(input) as f:
        datalines = f.readlines()
        for line in datalines:
            lines = line.split(' -> ')
            for i in range(1,len(lines)):
                ymax = drawLine(lines[i-1], lines[i], ymax)

    # add the ground
    for x in range(0,X_MAX):
        cave[ymax+2][x] = '#'
        
    # simuate the sand
    result = fallingSand(ymax, 2)

    printCave()
    
    return result


if __name__ == '__main__':
    if DEBUG:
        input = "../data/test"
    else:
        input = "../data/input_data_14"   

    cave = [[]]
    for i in range(0,Y_MAX):
        cave.append([])
        for j in range(0,X_MAX):
            cave[i].append('.')

    print("Part 1 =", part1(input))

    cave = [[]]
    for i in range(0,Y_MAX):
        cave.append([])
        for j in range(0,X_MAX):
            cave[i].append('.')

    print("Part 2 =", part2(input))

pass
    