'''
Created on Dec 1, 2021

@author: barrda

A, Rock win Scissors
B, Papper win rock
C, Scissors win papper
X  loose
Y  draw
Z  win

'''

DEBUG = 0

def convertDraw(adv, me):
    if   ( me == 'X'):
        if (adv == 'A'):
            return 'C'
        elif (adv == 'B'):
            return 'A'
        else:
            return 'B'        
    elif ( me == 'Y'):
        return adv
    elif ( me == 'Z'):
        if (adv == 'A'):
            return 'B'
        elif (adv == 'B'):
            return 'C'
        else:
            return 'A'        
    else:
        print("ERROR!")

def gameRules( adv, me ):
    print("round ", adv, me)
    if (me == adv):
        win = 3
    elif (me == 'A' and adv == 'C'):
        win = 6
    elif (me == 'B' and adv == 'A'):
        win = 6
    elif (me == 'C' and adv == 'B'):
        win = 6
    else:
        win = 0    
    return win
            
def getScore( me, win ):
    score = win
    if   ( me == 'A'):
        score += 1
    elif ( me == 'B'):
        score += 2
    elif ( me == 'C'):
        score += 3

    return score


if __name__ == '__main__':
    if DEBUG:
        input = "../data/test"
    else:
        input = "../data/input_data_2"   
    with open(input) as f:
        datalines = f.readlines()
        totalScore = 0        
        for r in datalines:
            advDraw = r.split()[0]
            myDraw  = r.split()[1]
            print("adv=", advDraw, " me=", myDraw)
            myDraw = convertDraw(advDraw, myDraw)
            win = gameRules(advDraw, myDraw)
            totalScore += getScore(myDraw, win)
            print("adv=", advDraw, " me=", myDraw, " -> ", win, totalScore)

print("Total =", totalScore)

pass
    