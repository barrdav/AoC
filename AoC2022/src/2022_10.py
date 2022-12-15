'''
Created on Dec 1, 2021

@author: barrda

'''

DEBUG = 0

#-------------------------------------
cl = [20, 60, 100, 140, 180, 220]

def calcStrength(c, r, result):
    if c in cl:
        result += (c * r)
    display(c, r)    
    return result
        
def display(c, r):
    x = (c % 40)-1
    y = int((c-1) / 40)
    if x in range(r-1, r+2):
        D[y].append('#')
    else:
        D[y].append('.')        
    print(c, x, y, r)
            
def part1(input):
    r = 1       # register
    result = 0
    with open(input) as f:
        datalines = f.readlines()
        c = 0   #cycles
        for cmd in datalines:
            if 'noop' in cmd:
                c += 1
                result = calcStrength(c, r, result)
            else:   #ADDR
                c += 1
                result = calcStrength(c, r, result)
                a = int(cmd.split('addx ')[1])
                c += 1
                result = calcStrength(c, r, result)
                r += a
                print('addx ', a , ' ->', r)
    return result

def part2(input):
    for i in range(0,6):
        print(D[i])
    return


if __name__ == '__main__':
    D = [[]]    
    for i in range(0,6):
        D.append([])
    if DEBUG:
        input = "../data/test"
    else:
        input = "../data/input_data_10"   

print("Part 1 =", part1(input))
print("Part 2 =", part2(input))

pass
    