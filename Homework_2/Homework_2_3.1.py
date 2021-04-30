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
time = min(T,int(math.log((1 - p),(1 - w ** 2))) + 1)

for i in range(n):
    byDotBest = 0
    byDotListBest = []
    lineBest = 0
    dotLeft = len(string) - 1
    popTime = 0
    for k in range(time):
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
        if lineList[s][2] != 0:
            lineList[s][2] = -lineList[s][2]
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
        lineList[t][u] = round(lineList[t][u],8)
        lineList[t][u] = list(str(lineList[t][u]))
        if lineList[t][u] == ['0']:
            lineList[t][u] = '0.00000000'
        elif (len(lineList[t][u]) - lineList[t][u].index('.') - 1) < 8:
            lineList[t][u].append('0' * (8 - len(lineList[t][u]) + lineList[t][u].index('.') + 1))
            lineList[t][u] = ''.join(lineList[t][u])
        else:
            lineList[t][u] = ''.join(lineList[t][u])

for v in lineList:
    print(v[0],v[1],v[2])
