import sys
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
    #print(string[i][0])
    string[i][0] = float(string[i][0])
    string[i][1] = float(string[i][1])
byDot = 0#附近的点的个数
byDotBest = 0#此次SANSAC以来得到的最多的附近的点的个数
lineBest = []#此次SANSAC以来得到的最多附近的点的直线的参数
lineList = []#最终输出的直线参数的列表
byDotList = []#附近的点在string列表中的序列号
byDotListBest = []#到目前为止最优情况的点的序列的集合
popTime = 0#此次RANSAC以来pop掉的点的个数

import random

for i in range(n):
    for j in range(T):#
        x = len(string) - 1#
        k = random.randint(0,x)
        l = random.randint(0,x)
        if k == l:
            break
    #for k in range(len(string)):#
    #    for l in range((k + 1),len(string)):#
        if string[k][0] == string[l][0] and string[k][1] == string[l][1]:
            break
        elif string[k][0] == string[l][0]:
            line = [1,0,-string[k][0]]
        elif string[k][1] == string[l][1]:
            line = [0,1,-string[k][1]]
        else:
            line = [1,
                    (string[l][0] - string[k][0]) / (string[k][1] - string[l][1]),
                    (string[k][0] * string[l][1] - string[l][0] * string[k][1]) / (string[k][1] - string[l][1])]
        for m in range(len(string)):
            if (abs(line[0] * string[m][0] + line[1] * string[m][1] + line[2]) / ((line[0] ** 2 + line[1] ** 2) ** 0.5)) < eps:
                byDot += 1
                byDotList.append(m)
        if byDot > byDotBest:
            byDotBest = byDot
            byDotListBest = byDotList
            lineBest = line
        else:
            pass
        byDot = 0
        byDotList = []
    lineList.append(lineBest)
    for o in byDotListBest:#
        string.pop(o - popTime)
        popTime += 1
    byDotBest = 0
    lineBest = []
    byDotListBest = []
    popTime = 0
    if lineList[-1] == []:
        lineList.pop(-1)

for q in range(len(lineList)):
    if lineList[q][0] < 0:
        linelist[q][0] = -lineList[q][0]
        if lineList[q][1] != 0:
            lineList[q][1] = -lineList[q][1]
        if lineList[q][2] != 0:
            lineList[q][2] = -lineList[q][2]
    elif lineList[q][0] == 0 and lineList[q][1] < 0:
        lineList[q][1] = -lineList[q][1]
        if lineList[q][2] != 0:
            lineList[q][2] = -lineList[q][2]
    lineList[q] = [(lineList[q][0] / ((lineList[q][0] ** 2 + lineList[q][1] ** 2 + lineList[q][2] ** 2) ** 0.5)),
                   (lineList[q][1] / ((lineList[q][0] ** 2 + lineList[q][1] ** 2 + lineList[q][2] ** 2) ** 0.5)),
                   (lineList[q][2] / ((lineList[q][0] ** 2 + lineList[q][1] ** 2 + lineList[q][2] ** 2) ** 0.5))]
lineList.sort()
for r in range(len(lineList)):
    for s in range(3):
        lineList[r][s] = round(lineList[r][s],8)
        lineList[r][s] = list(str(lineList[r][s]))
        if lineList[r][s] == ['0']:
            lineList[r][s] = '0.00000000'
        elif (len(lineList[r][s]) - lineList[r][s].index('.') - 1) < 8:
            lineList[r][s].append('0' * (8 - len(lineList[r][s]) + lineList[r][s].index('.') + 1))
            lineList[r][s] = ''.join(lineList[r][s])
        else:
            lineList[r][s] = ''.join(lineList[r][s])
for s in lineList:
    print(s[0],s[1],s[2])
