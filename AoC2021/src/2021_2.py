'''
Created on Dec 1, 2021

@author: barrda
'''
    
if __name__ == '__main__':
    with open("../data/input_data_2") as f:
#    with open("../data/test") as f:
        datalines = f.readlines()
        d = 0
        f = 0
        aim = 0
        for mvt in datalines:
            print(mvt)
            v = int(mvt.split()[1])
            if ( "forward" in mvt):
                f = f + v
                d = d + (aim * v)
            elif("down" in mvt):
                aim = aim + v
            elif("up" in mvt):
                aim = aim - v
            else:
                print("ERROR with ", mvt)
                exit()
        result = d * f
        print("RESULT part 1 = ",result)
        
            
    pass