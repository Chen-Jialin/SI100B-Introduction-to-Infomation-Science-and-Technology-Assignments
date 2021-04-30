import sys
string = sys.stdin.read()
string = string.split('\n')
label_1 = string[0]
label_1 = label_1.split(' ')
for i in range(len(label_1)):
    label_1[i] = float(label_1[i])
label_2 = string[1]
label_2 = label_2.split(' ')
for i in range(len(label_2)):
    label_2[i] = float(label_2[i])

geometricError = ((label_1[0] - label_2[0]) ** 2 + (label_1[1] - label_2[1]) ** 2 + (label_1[2] - label_2[2]) ** 2) ** 0.5

print('{:.8f}'.format(geometricError))
