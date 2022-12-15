'''
Created on Dec 1, 2021

@author: barrda
'''
import sys
import numpy as np

def part1():
    result = 0
    print("RESULT part 1 = ",result)
        
    
def part2():
    result = 0
    print("RESULT part 2 = ",result)

    

    
if __name__ == '__main__':
    print(sys.version)
#    with open("../data/input_data_4") as f:
    with open("../data/test") as f:
        listNumbers = f.readline().split(',')
        print( listNumbers, "\n" );
        # Create empty boarss
        boards = np.zeros((3,5,5),int)
        for a in range(0,3):
            print("---------------")
            #jump empty line
            f.readline()
            for b in range(0,5):
                line = f.readline()
                line = line[:-1]        #remove eol
                line = line.split()     
                boards[a,b] = line
        
        print(boards)
    pass