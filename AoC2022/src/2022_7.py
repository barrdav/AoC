'''
Created on Dec 1, 2021

@author: barrda

Tree structured data done with list

'''

DEBUG = 0

FILE_SIZE_LIMIT = 100000

NAME   = 0
SUBDIR = 1
SIZE   = 2

def PRT(s):
    if DEBUG:
        print(s)
        
#-------------------------------------
filesys = [['/',[],0]]    # name, sub-dir list, size  

def cmdChangeDir(newDir):
    return 

def cmdListDir(thisDir):
    TotalDirSize = 0
    return TotalDirSize

def searchDirIndex(name):   
    PRT('search for' + name)
    if name == '/':
        return 0
    for i in range(1,len(filesys)):
        fullName = filesys[i][NAME] + '/'
        if fullName == name:
            print("Found!", name, i)
            return i
    return -1      

def getSubDirSize(path,totalSize):
    i = searchDirIndex(path)    
    for name in filesys[i][SUBDIR]:
        searchName = name + '/'
        j = searchDirIndex(searchName)
        PRT('look at ' + searchName)
        thisSize = filesys[j][SIZE] 
        if filesys[j][SUBDIR] == []:
            PRT('no subdir for '+ searchName)
        else:
            thisSize = getSubDirSize(searchName, thisSize)
        if  thisSize < FILE_SIZE_LIMIT:
            print('add ', thisSize)
            totalSize += thisSize
        else:
            print('too big:', thisSize)  
    return totalSize  
    
def fsAddDir(rootDir, name):
    # check if already created
    if searchDirIndex(rootDir + name + '/') >= 0:
        print("dir already exist")
        return
    root = searchDirIndex(rootDir)
    filesys[root][SUBDIR].append(rootDir + name)
    filesys.append([(rootDir + name), [], 0])
    print(filesys)

def fsAddFile(rootDir, size):
    root = searchDirIndex(rootDir)
    filesys[root][SIZE] += size 
    print(filesys)
        
def part1(input):
    # 1 Build the file structure   
    currentPath = '' 
    with open(input) as f:
        datalines = f.readlines()
        for cmd in datalines:
            cmd = cmd.strip('\n')
            if '$ ' in cmd:
                print("this is a command", cmd.split('$ ')[1])
                if 'cd ' in cmd:
                    newDir= cmd.split('cd ')[1]
                    if '..' in newDir:
                        currentPath = currentPath.rsplit('/', maxsplit=2)[0] + '/'
                    elif '/' in cmd:
                        currentPath = '/'
                    else:
                        currentPath += newDir + '/'
                    PRT('>' + currentPath)
            elif 'dir ' in cmd:
                print("this is a directory", cmd.split('dir ')[1])
                fsAddDir(currentPath, cmd.split('dir ')[1])
            else:
                print("this is a file", cmd, ' = ', int(cmd.split()[0]))
                fsAddFile(currentPath, int(cmd.split()[0]))
    
    PRT('============================================================================')
    # 2 Navigate the file structure
    currentPath = '/' 
    totalSize = 0
    totalSize = getSubDirSize(currentPath,totalSize)                            
    return totalSize

def part2(input):
    with open(input) as f:
        datalines = f.readlines()
        for instruct in datalines:
            break
    return


if __name__ == '__main__':
    if DEBUG:
        input = "../data/test"
    else:
        input = "../data/input_data_7"   

print("Part 1 =", part1(input))
print("Part 2 =", part2(input))

pass
    