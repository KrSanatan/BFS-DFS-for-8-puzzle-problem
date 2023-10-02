import copy
import os
from collections import deque
import time

#user input list <declaration>
userInputList =[]

#input and target matrix <declaration>
mainInputMatrix=[]
targetMatrix=[[1,2,3],[4,5,6],[7,8,0]]

#for storing explored matrix combinations for duplicacy check
det=set()

#variable declarations
zeroRow = 0
zeroCol = 0
flagMatch = True
treeQueue = deque()
treeList = []
comparisionsDone = 0

'''**********************Function declaration STARTS***************************'''
#initialization function: taking inputs from user
def init():
    print("Enter Elements for the 3x3 Matrix in row major order\n",)
    print("Range should be from 0 to 8 , integers only, and use 0 to denote blank space without repeatition.\n")
    for i in range(9):
        userInput = int(input("Enter element "+str(i)+"\n"))
        if (userInput < 0 or userInput > 8):
                print("Please only enter states which are [0-8], terminate and run code again")
                exit(0)
        elif userInput in userInputList:
                print("Please only unique elements, terminate and run code again")
                exit(0)
        else:
                userInputList.append(userInput)       
    createMatrixFromInput()  

#defining initial user input matrix
def createMatrixFromInput():
    j=0
    global mainInputMatrix
    mainInputMatrix.append(userInputList[0:3])
    mainInputMatrix.append(userInputList[3:6])
    mainInputMatrix.append(userInputList[6:9])         
    findBlankIndex(mainInputMatrix) 
    global treeQueue   
    treeQueue.append(mainInputMatrix) 

#find index of 0<blank space>   
def findBlankIndex(matrix):
    i = 0
    for i in range(matrix.__len__()):
       row =[]
       row = list(matrix[i])
       if(0 in row):
        global zeroCol
        zeroCol = row.index(0)
        global zeroRow
        zeroRow = i
        i = i+1                     

#printing matrix on terminal
def print_matrix(matrix):
    for i,j,k in matrix:
        print(i,j,k)

#perform movements/combinations
def performCombinations(matrix):
    moveUp(matrix)       

#move up call
def moveUp(myMatrix):
    if((int(zeroRow) - 1)>-1):
        tempMatrix = []
        tempMatrix = copy.deepcopy(myMatrix)
        row = []
        row = tempMatrix[zeroRow - 1]
        data = row[zeroCol]
        tempMatrix[zeroRow - 1][zeroCol]=0
        tempMatrix[zeroRow][zeroCol] = data
        global treeQueue
        treeQueue.append(tempMatrix)
    moveDown(myMatrix)

#move down call
def moveDown(myMatrix):
    if((int(zeroRow) + 1)<3):
        tempMatrix = []
        tempMatrix = copy.deepcopy(myMatrix)
        row = []
        row = tempMatrix[zeroRow + 1]
        data = row[zeroCol]
        tempMatrix[zeroRow + 1][zeroCol]=0
        tempMatrix[zeroRow][zeroCol] = data 
        global treeQueue
        treeQueue.append(tempMatrix)
    moveLeft(myMatrix)

#move left call
def moveLeft(myMatrix):
    if((int(zeroCol) - 1)>-1):
        tempMatrix = []
        tempMatrix = copy.deepcopy(myMatrix)
        data = tempMatrix[zeroRow][zeroCol-1]
        tempMatrix[zeroRow][zeroCol - 1]=0
        tempMatrix[zeroRow][zeroCol] = data
        global treeQueue
        treeQueue.append(tempMatrix)
    moveRight(myMatrix)

#move right call
def moveRight(myMatrix):
    if((int(zeroCol) + 1)<3):
        tempMatrix = []
        tempMatrix = copy.deepcopy(myMatrix)
        data = tempMatrix[zeroRow][zeroCol+1]
        tempMatrix[zeroRow][zeroCol + 1]=0
        tempMatrix[zeroRow][zeroCol] = data 
        global treeQueue
        treeQueue.append(tempMatrix) 
 
#compare with target matrix
def compareWithTarget(matrix,targetMatrix): 
    global comparisionsDone
    comparisionsDone  = comparisionsDone + 1
    if(matrix==targetMatrix):
        print("comparision done="+str(comparisionsDone))
        print(len(det))
        exit(0)         
    
'''***************Function declaration ENDS'******************''' 


#main code execution BFS <uncomment this and comment DFS code below to run >
# init()
# tempMatrix = treeQueue.popleft()
# compareWithTarget(tempMatrix,targetMatrix)
# performCombinations(tempMatrix)
# while(True):
#      matrixFromTreeQueue = treeQueue.popleft()
#      findBlankIndex(matrixFromTreeQueue)
#      if(str(matrixFromTreeQueue) not in det):
#           compareWithTarget(matrixFromTreeQueue,targetMatrix)
#           det.add(str(matrixFromTreeQueue))
#           performCombinations(matrixFromTreeQueue)
          
   
#main code for DFS 
init()
tempMatrix = treeQueue.pop()
compareWithTarget(tempMatrix,targetMatrix)
performCombinations(tempMatrix)
while(True):
     matrixFromTreeQueue = treeQueue.pop()
     findBlankIndex(matrixFromTreeQueue)
     if(str(matrixFromTreeQueue) not in det):
          compareWithTarget(matrixFromTreeQueue,targetMatrix)
          det.add(str(matrixFromTreeQueue))
          performCombinations(matrixFromTreeQueue)



