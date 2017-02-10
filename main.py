#!/usr/bin/env python3
import argparse

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
            for j in l[i]:
                if (j == 'x'):
                    self.score -= 10
        return self.score
        

initialState = State();
print(initialState.getScore())
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

