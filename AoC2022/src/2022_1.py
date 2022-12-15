'''
Created on Dec 1, 2021

@author: barrda
'''



if __name__ == '__main__':
    with open("../data/input_data_1") as f:
#    with open("../data/test") as f:
        datalines = f.readlines()
        calorieSumList = []
        elfeSum = 0
        for meal in datalines:
            if meal == "\n":
                calorieSumList.append(elfeSum)
#                print(elfeSum, calorieSumList)
                elfeSum = 0
            else:
                elfeSum += int(meal)

calorieSumList.sort(key=int, reverse=True)
print("sorted list is ", calorieSumList[:3])
print("Total =", sum(calorieSumList[0:3]))

pass
    