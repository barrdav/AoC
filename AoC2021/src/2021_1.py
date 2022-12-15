'''
Created on Dec 1, 2021

@author: barrda
'''
    
if __name__ == '__main__':
    with open("../data/input_data_1") as f:
#    with open("../data/test") as f:
        datalines = f.readlines()
        previous_deep = int(datalines[0])
        total = 0
        for deep in datalines:
            if int(deep) > previous_deep:
                total += 1
            previous_deep = int(deep)
        print("RESULT part 1 = ",total)
        
            
    pass