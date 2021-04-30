import random

n = random.randint(1,10)
line = []
for i in range(n):
    line.append([0,0,0])
    while line[i] == [0,0,0] or (line[i][0] == 0 and line[i][1] == 0):
        for k in range(3):
            line[i][k] = random.random()
    if line[i][0] < 0:
        line[i][0] = -line[i][0]
        if line[i][1] != 0:
            line[i][1] = -line[i][1]
        else:
            pass
        if line[i][2] != 0:
            line[i][2] = -line[i][2]
    if line[i][0] == 0:
        line[i][1] = -line[i][1]
        if line[i][2] != 0:
            line[i][2] = -line[i][2]
    line[i] = [line[i][0] / (line[i][0] ** 2 + line[i][1] ** 2 + line[i][2] ** 2) ** 0.5,
               line[i][1] / (line[i][0] ** 2 + line[i][1] ** 2 + line[i][2] ** 2) ** 0.5,
               line[i][2] / (line[i][0] ** 2 + line[i][1] ** 2 + line[i][2] ** 2) ** 0.5]

eps = random.uniform(0.001,0.01)
T = 499500
inliers = random.randint(500,999)
outliers = 1000 - inliers
w = inliers / 1000
p = random.uniform(0.99,1)

dots = []
for j in range(n):
    for k in range(inliers // n):
        if line[j][1] == 0:
            x = -line[j][2] / line[j][0] + random.uniform(-eps,eps)
            y = random.uniform(-50,-50)
        else:
            x = random.uniform(-50,50)
            y = -(line[j][0] * x + line[j][2]) / line[j][1]
        dots.append([x,y])

for l in range(outliers):
    dots.append([random.uniform(-50,50),random.uniform(-50,50)])

random.shuffle(dots)

testcase = open('testcase.in','w')
testcase.write(str(n) + ' ' + str(eps) + ' ' + str(T) + ' ' + str(p) + ' ' + str(w) + '\n')
for m in range(len(dots)):
    testcase.write(str(dots[m][0]) + ' ' + str(dots[m][1]) + '\n')
testcase.close()

key = open('answer.out','w')
for o in range(len(line)):
    key.write(str(line[o][0]) + ' ' + str(line[o][1]) + ' ' + str(line[o][2]))
    if o != (len(line) - 1):
        key.write('\n')
key.close()

print('#You can use the code below to measure your runtime and the correctness of your output:\n\
\n\
#Runtime measurement code:\n\
\n\
#Add the code below to the front of the beginning of your code:\n\
\n\
import time\n\
time.clock()\n\
\n\
#And add the code below to the behind of the end of your code:\n\
\n\
runtime = time.clock()\n\
print("Your runtime is ",runtime,"s.")\n\
if runtime > 10:\n\
    print("TimeLimitExceed.")\n\
else:\n\
    print("Runtime is OK.")\n\
\n\
#Output checking code:\n\
\n\
#Input the stuff you want to output(print) in the form of two-dimension list to the funtion below:\n\
def check(answer):\n\
    if len(answer) < n:#Here the n is the number of the lines,you should assign correct value to it or it is possible to raise error.\n\
        print("WrongNumbrOfTheLine:The number of the lines you get",len(answer),"is not enough.")\n\
    elif len(answer) > n:#Here the n is the number of the lines,you should assign correct value to it or it is possible to raise error.\n\
        print("WrongNumbrOfTheLine:The number of the lines you get",len(answer),"is more than required.")\n\
    else:\n\
        parameterNumber = True\n\
        for s in range(len(answer)):\n\
            if len(answer[s]) < 3:\n\
                print("WrongNumberOfParameter:The parameter of line",s,"is not enough.")\n\
                parameterNumber = False\n\
            elif len(answer[s]) > 3:\n\
                print("WrongNumberOfParameter:The parameter of line",s,"is more than required.")\n\
                parameterNumber = False\n\
    for t in range(len(answer)):\n\
        if (float(answer[t][0]) ** 2 + float(answer[t][1]) ** 2 + float(answer[t][2]) ** 2 - 1) > 1e-6:\n\
            print("WrongNormalization:",answer[t][0],"^2 +",answer[t][1],"^2 +",answer[t][2],"^2 != 1.")\n\
    for u in range(len(answer)):\n\
        if float(answer[u][0]) < 0:\n\
            print("WrongSign:The parameter \\"a\\" of line",u + 1,"< 0")\n\
        elif float(answer[u][0]) <= 0 and float(answer[u][1]) < 0:\n\
            print("WrongSign:The parameter \\"b\\" of line",u + 1,"< 0")\n\
    for v in range(1,len(answer)):\n\
        if float(answer[v][0]) < float(answer[v - 1][0]):\n\
            print("WrongOrderOfOutput:Not ascending order.")\n\
            break\n\
        elif float(answer[v][0]) == float(answer[v - 1][0]) and float(answer[v][1]) < float(answer[v - 1][1]):\n\
            print("WrongOrderOfOutput:Not ascending order.")\n\
            break\n\
    if parameterNumber == True:\n\
        key = open("answer.out","r")\n\
        keys = key.read().split("\\n")\n\
        key.close()\n\
        for z in range(len(keys)):\n\
            keys[z] = keys[z].split(' ')\n\
        for a in range(len(answer)):\n\
            print("The line",a + 1,"\'s geometric error is",((float(answer[a][0]) - float(keys[a][0])) ** 2 + (float(answer[a][1]) - float(keys[a][1])) ** 2 + (float(answer[a][2]) - float(keys[a][2])) ** 2) ** 0.5)\n\
check(answer)')

input('Press "Enter" to quit.')
