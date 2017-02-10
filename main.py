#!/usr/bin/env python3
import argparse
from random import randint

#parsing option from users
parser = argparse.ArgumentParser(description='we trust in probability')
parser.add_argument('filename', help='state to take in')
args = parser.parse_args()

#read the file and turn into array
f = open(args.filename)
l = [] #all the information about the terrain
r = 0 #row of the terrain
c = 0 #column of the terrain
for line in f.readlines():
    cols = line.split()
    l.append(cols)
    r += 1
    c = len(cols)
f.close()

colorlist = ('b', 'x');
for i in range(0,len(l)):
    print(l[i])

print (l[1][2])

class State:
    def __init__(self, board = []):
        self.board = board
        
        if (board == []):
            self.board = []
            for i in range(0, len(l)):
                for j in range(0, len(l[0])):
                    newNode = Node(j,i,l[i][j])
                    self.board.append(newNode)
        self.uneditNode = []
        for i in range(0, len(self.board)):
            if (not self.board[i].editable):
                self.uneditNode.append(self.board[i])
        
        
    def getScore(self):
        self.score = 0
        
        if self.isTwoNodeConnected(self.uneditNode[0],self.uneditNode[1]):
            self.score +=1000
        self.score += 20*len(self.checkedList)
         
#         if self.isTwoNodeConnected(self.uneditNode[1],self.uneditNode[3]):
#             self.score +=1000
#         self.score += 20*len(self.checkedList)
#         
#         if self.isTwoNodeConnected(self.uneditNode[0],self.uneditNode[2]):
#             self.score +=1000
#         self.score += 20*len(self.checkedList)
#          
#         if self.isTwoNodeConnected(self.uneditNode[1],self.uneditNode[3]):
#             self.score +=1000
#         self.score += 20*len(self.checkedList)
        
        for i in range(0,len(self.board)):
            if (self.getColorNode(i) == 'x'):
                self.score -= 50
            if (not (i+1)%(c+1) == 0):
                if (self.getColorNode(i) == self.getColorNode(i-1)):
                    self.score += 1
            if (not (i+1)%(c+1) == c)&(not i == len(self.board)-1):
                if (self.getColorNode(i) == self.getColorNode(i+1)):
                    self.score += 1
            
            if (i>c):
                if (self.getColorNode(i) == self.getColorNode(i-c)):
                    self.score += 1
            if (i<len(self.board)-c-1):
                if (self.getColorNode(i) == self.getColorNode(i+c)):
                    self.score += 1
        return self.score
        
    def nextState(self):
        nextState = State(self.board)
        #while (nextState.getScore()<=self.getScore()):
        i1 = randint(0, len(self.board)-1)
        while (self.board[i1].editable == False):
            i1 = randint(0, len(self.board)-1)
            #if (self.board[i1][i2] == 'x'):
        i2 = randint(0, len(colorlist)-1)
        randomColor = colorlist[i2]
        nextState.changeColorOfNode(i1, randomColor)
        
        return nextState
    
    def isTwoNodeConnected(self,node1, node2):
        result = False
        checkedList = []
        self.checkedList = []
        for i in range(0, len(self.board)):
            if (self.board[i].isEqual(node1)):
                checkedList.append(self.board[i]) #Loop starts
                j = 0
                currentNode = self.board[i]
                while (j<len(checkedList)):
                    currentNode = checkedList.pop()
                    dummy = self.getNode(currentNode)
                    if (not (dummy+1)%(c+1) == c)&(not dummy == len(self.board)-1):
                        if (self.board[dummy+1].color == currentNode.color):
                            checkedList.append(self.board[dummy+1])
                            #currentNode = self.board[dummy+1]
                    if (not (dummy+1)%(c+1) == 0):
                        if (self.board[dummy-1].color == currentNode.color):
                            checkedList.append(self.board[dummy-1])
                            #currentNode = self.board[dummy-1]
                    if (dummy>c):
                        if (self.board[dummy-c].color == currentNode.color):
                            checkedList.append(self.board[dummy-c])
                            #currentNode = self.board[dummy-c]
                            
                    if (dummy<len(self.board)-c-1):
                        if (self.board[dummy+c].color == currentNode.color):
                            checkedList.append(self.board[dummy+c])
                            #currentNode = self.board[dummy+c]
                    j +=1
                    if(j>30):
                        break
        
        for i in range(0,len(checkedList)):
            if (checkedList[i].isEqual(node2)):
                result = True
        self.checkedList = checkedList
        return result
    
    def changeColorOfNode(self, x,changedColor):
        self.board[x].changeColorTo(changedColor)
        return 0
    
    def getNode(self, node):
        result = None
        for i in range(0, len(self.board)):
            if (self.board[i].x == node.x)&(self.board[i].y == node.y)&(self.board[i].color == node.color):
                result = i
        
        return result
        
    def getColorNode(self, x):
        return self.board[x].color
        
    def getList(self):
        listToPrint = []
        for i in range(0, len(self.board)):
            listToPrint.append(self.board[i].color)
        
        return listToPrint


class Node:
    def __init__(self, x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.editable = False
        if (self.color == 'x'):
            self.editable = True
        
    def changeColorTo(self, changedColor):
        if (self.editable):
            self.color = changedColor
        
    def isEqual(self,node):
        return (self.x == node.x)&(self.y == node.y)&(self.color == node.color)
    
    def createNeighbor(self):
        neighborList =[]
        neighborList.append(Node(self.x - 1, self.y, self.color))
        neighborList.append(Node(self.x + 1, self.y, self.color))
        neighborList.append(Node(self.x    , self.y - 1, self.color))
        neighborList.append(Node(self.x - 1, self.y + 1, self.color))
        return neighborList

def hillclimb(state):
    potentialState = []
    countState = 0
    countTime = 0
    currentState = state
    potentialState.append(currentState)
    while (countState < 10):
        currentState = potentialState.pop()
        nextState = currentState.nextState()
        if (nextState.getScore()>currentState.getScore()):
            currentState = nextState
            countTime = 0
        else:
            countTime +=1
        
        potentialState.append(currentState)
        
        if (countTime > 10):
            countTime = 0
            countState +=1
            currentState = state
            potentialState.append(currentState)
    
    bestState = potentialState[0]
    for i in range(0, len(potentialState)):
        if (potentialState[i].getScore() > bestState.getScore()):
            bestState = potentialState[i]

    return bestState




initialState = State();

print(initialState.getScore())
bestState = hillclimb(initialState)
for i in range(0,r):
    print(bestState.getList()[i*(r):i*(r)+r])
    
print(bestState.getList())
print(len(bestState.uneditNode))
print(bestState.getScore())
# print(test.bin1)
# print(test.bin2)
# print(test.bin3)
# print(test.isLegal())
# print(test.score())
# for i in range(1,20):
#     test = test.newState()
#     print(test.bin1)
#     print(test.bin2)
#     print(test.bin3)
#     print(test.isLegal())
#     print(test.score())

