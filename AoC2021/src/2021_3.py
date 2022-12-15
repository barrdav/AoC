'''
Created on Dec 1, 2021

@author: barrda
'''


def part1(input, debug):
    g = 0
    e = 0
    nbBits = len(input[0]) - 1
    NbLines = len(input)
    bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if debug: 
        print("nb bits and lines",nbBits, NbLines)
    for b in input:
        for i in range(0,nbBits):
            if int(b[i]) == 1:
                bits[i] = bits[i] + 1
    
    for i in range(0,nbBits):
        if bits[i] > (NbLines/2):
            if debug:
                print("*")
            g = g + ( 2**(nbBits - i - 1) )
        else:
            e = e + ( 2**(nbBits - i - 1) ) 
        if debug:
            print(bits[i], (NbLines/2),g)
    result = g * e
    print("RESULT part 1 = ",result)
        
    
def part2(input, invert):
    NbLines = len(input)
    currentBit = 0
    # while there is more than one number left in the input list
    while NbLines > 1:   
        print("=========================================")
        print ( "nbLines = ",NbLines," current bit = ", currentBit)     
        # count the number of 1 for a bit
        if invert:
            bit = 1
        else:
            bit = 0    
        bitCounter = 0
        for line in input:
            if int(line[currentBit]) == 1:
                bitCounter = bitCounter + 1
                if bitCounter >= (NbLines/2):  
                    if invert:
                        bit = 0
                    else:
                        bit = 1    
                    break
                
        print("bit is ", bit)

        # remove lines
        i = 0
        while i < NbLines:
            print("nb lines ", NbLines)
            line = input[i]
            while int(line[currentBit]) != bit:
                print("line removed: ", i, line)
                del input[i]
                NbLines = NbLines - 1
                print("NEW LIST--------------")
                print(input)
                if i >= NbLines:
                    break
                line = input[i]
            i = i + 1
            
        currentBit = currentBit + 1
    
    return input[0]

def convertBinToInt (binaryInput):
    output = 0
    bitValue = 2048
    for i in range(0,12):
        output = output + int(binaryInput[i]) * bitValue
        bitValue = int(bitValue / 2)
        print(output)
    return output
        
    
    
if __name__ == '__main__':
    with open("../data/input_data_3") as f:
#    with open("../data/test") as f:
        datalines = f.readlines()

        part1(datalines, False)
        
        o2 = part2(datalines, False)
        f.seek(0)
        datalines = f.readlines()
        print("INPUT FOR CO2:",datalines)
        co2 = part2(datalines, True)
        print("O2=",o2," CO2=",co2)
        O2dec = convertBinToInt(o2[0:12])
        CO2dec = convertBinToInt(co2[0:12])

        result = O2dec * CO2dec

        print("RESULT part 2 = ",result)
    
    pass


