import time
time.clock()

import sys
import random
import math

string = sys.stdin.read()

string = string.split('\n')
parameters = string[0].split(' ')
n = int(parameters[0])
eps = float(parameters[1])
T = int(parameters[2])
p = float(parameters[3])
w = float(parameters[4])
string = string[1:-2]
for i in range(len(string)):
    string[i] = string[i].split(' ')
    string[i][0] = float(string[i][0])
    string[i][1] = float(string[i][1])

lineList = []
times = min(T,int(math.log((1 - p),(1 - w ** 2))) + 1)

for i in range(n):
    byDotBest = 0
    byDotListBest = []
    lineBest = 0
    dotLeft = len(string) - 1
    popTime = 0
    for k in range(times):
        byDot = 0
        byDotList = []
        k = random.randint(0,dotLeft)
        m = random.randint(0,dotLeft)
        if string[k][0] == string[m][0] and string[k][1] == string[m][1]:
            break
        elif string[k][0] == string[m][0]:
            line = [1,0,-string[k][0]]
        elif string[k][1] == string[m][1]:
            line = [0,1,-string[k][1]]
        else:
            line = [1,
                    (string[m][0] - string[k][0]) / (string[k][1] - string[m][1]),
                    (string[k][0] * string[m][1] - string[m][0] * string[k][1]) / (string[k][1] - string[m][1])]
        for q in range(len(string)):
            if (abs(line[0] * string[q][0] + line[1] * string[q][1] + line[2]) / ((line[0] ** 2 + line[1] ** 2) ** 0.5)) < eps:
                byDot += 1
                byDotList.append(q)
        if byDot > byDotBest:
            byDotBest = byDot
            byDotListBest = byDotList
            lineBest = line
    if lineBest != []:
        lineList.append(lineBest)
    for r in byDotListBest:
        string.pop(r - popTime)
        popTime += 1

for s in range(len(lineList)):
    if lineList[s][0] < 0:
        linelist[s][0] = -lineList[s][0]
        if lineList[s][1] != 0:
            lineList[s][1] = -lineList[s][1]
        else:
            pass
        if lineList[s][2] != 0:
            lineList[s][2] = -lineList[s][2]
        else:
            pass
    elif lineList[s][0] == 0 and lineList[s][1] < 0:
        lineList[s][1] = -lineList[s][1]
        if lineList[s][2] != 0:
            lineList[s][2] = -lineList[s][2]
    lineList[s] = [(lineList[s][0] / ((lineList[s][0] ** 2 + lineList[s][1] ** 2 + lineList[s][2] ** 2) ** 0.5)),
                   (lineList[s][1] / ((lineList[s][0] ** 2 + lineList[s][1] ** 2 + lineList[s][2] ** 2) ** 0.5)),
                   (lineList[s][2] / ((lineList[s][0] ** 2 + lineList[s][1] ** 2 + lineList[s][2] ** 2) ** 0.5))]
lineList.sort()
for t in range(len(lineList)):
    for u in range(3):
        lineList[t][u] = '{:.8f}'.format(lineList[t][u])

for v in lineList:
    print(v[0],v[1],v[2])

runtime = time.clock()
print("Your runtime is ",runtime,"s.")
if runtime > 10:
    print("TimeLimitExceed.")
else:
    print("Runtime is OK.")
answer = []
for z in range(len(lineList)):
    answer.append(lineList[z])
def check(answer):
    if len(answer) < n:#Here the n is the number of the lines,you should assign correct value to it or it is possible to raise error.
        print("WrongNumbrOfTheLine:The number of the lines you get",len(answer),"is not enough.")
    elif len(answer) > n:#Here the n is the number of the lines,you should assign correct value to it or it is possible to raise error.
        print("WrongNumbrOfTheLine:The number of the lines you get",len(answer),"is more than required.")
    else:
        parameterNumber = True
        for s in range(len(answer)):
            if len(answer[s]) < 3:
                print("WrongNumberOfParameter:The parameter of line",s,"is not enough.")
                parameterNumber = False
            elif len(answer[s]) > 3:
                print("WrongNumberOfParameter:The parameter of line",s,"is more than required.")
                parameterNumber = False
    for t in range(len(answer)):
        if (float(answer[t][0]) ** 2 + float(answer[t][1]) ** 2 + float(answer[t][2]) ** 2 - 1) > 1e-6:
            print("WrongNormalization:",answer[t][0],"^2 +",answer[t][1],"^2 +",answer[t][2],"^2 != 1.")
    for u in range(len(answer)):
        if float(answer[u][0]) < 0:
            print("WrongSign:The parameter \"a\" of line",u + 1,"< 0")
        elif float(answer[u][0]) <= 0 and float(answer[u][1]) < 0:
            print("WrongSign:The parameter \"b\" of line",u + 1,"< 0")
    for v in range(1,len(answer)):
        if float(answer[v][0]) < float(answer[v - 1][0]):
            print("WrongOrderOfOutput:Not ascending order.")
            break
        elif float(answer[v][0]) == float(answer[v - 1][0]) and float(answer[v][1]) < float(answer[v - 1][1]):
            print("WrongOrderOfOutput:Not ascending order.")
            break
    if parameterNumber == True:
        key = open("answer.txt","r")
        keys = key.read().split("\n")
        key.close()
        for z in range(len(keys)):
            keys[z] = keys[z].split(' ')
        for a in range(len(answer)):
            print("The line",a + 1,"'s geometric error is",((float(answer[a][0]) - float(keys[a][0])) ** 2 + (float(answer[a][1]) - float(keys[a][1])) ** 2 + (float(answer[a][2]) - float(keys[a][2])) ** 2) ** 0.5)
check(answer)
