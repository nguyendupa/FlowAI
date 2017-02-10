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


for i in range(0,len(l)):
    print(l[i])

print (l[1][2])

class State:
    def __init__(self):
        self.board = l

    def getScore(self):
        self.score = 0
        for i in range(0,len(self.board)):
            for j in self.board[i]:
                if (j == 'x'):
                    self.score -= 10
        return self.score
        
    def nextState(self):
        nextState = State()
        #while (nextState.getScore()<=self.getScore()):
        i1 = randint(0, r-1)
        i2 = randint(0, c-1)
            #if (self.board[i1][i2] == 'x'):
        nextState.board[i1][i2] = 'b'
        
        return nextState
        




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
        
        if (countTime == 10):
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
print(bestState.board)
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

