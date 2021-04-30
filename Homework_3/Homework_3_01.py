import numpy as np

n = 1
f = 2
r = 1
l = -1
t = 1
b = -1

P_1 = np.zeros((4,1))
P_1[0][0] = 0
P_1[1][0] = 0
P_1[2][0] = -2
P_1[3][0] = 1

P_2 = np.zeros((4,1))
P_2[0][0] = 1
P_2[1][0] = 1
P_2[2][0] = -2
P_2[3][0] = 1

def position(P):
    position = []
    for i in range(3):
        if P[i][0] < -1:
            position.append(-1)
        elif P[i][0] > 1:
            position.append(1)
        else:
            position.append(0)
    return position

M = np.zeros((4,4))
M[0][0] = 2 * n / (r - l)
M[0][2] = (r + l) / (r - l)
M[1][1] = 2 * n / (t - b)
M[1][2] = (t + b) / (t - b)
M[2][2] = -(f + n) / (f - n)
M[2][3] = -2 * f * n / (f - n)
M[3][2] = -1

P_1 = np.dot(M,P_1)
P_1 = P_1 / P_1[3][0]
P_2 = np.dot(M,P_2)
P_2 = P_2 / P_2[3][0]

print(P_1)
print(P_2)

position_1 = position(P_1)
position_2 = position(P_2)
if position_1 == [0,0,0] and position_2 == [0,0,0]:
    pass
elif position_1 != [0,0,0] and position_2 != [0,0,0]:
    P_1 = None
    P_2 = None
else:
    line3D = []
    line3D.append(P_2[0][0] - P_1[0][0])
    line3D.append(P_2[1][0] - P_1[1][0])
    line3D.append(P_2[2][0] - P_1[2][0])
    P_ = np.array([[float('inf')],[float('inf')],[float('inf')],[1]])
    if position_1 != [0,0,0]:
        for k in range(3):
            if position_1[k] != 0:
                for m in range(3):
                    if m == k:
                        P_[m][0] = position_1[m]
                    else:
                        P_[m][0] = (position_1[k] - P_1[k][0]) * line3D[m] / line3D[k] + P_1[m][0]
            else:
                pass
            if position(P_) == [0,0,0]:
                break
        P_1 = P_
    else:
        for k in range(3):
            if position_2[k] != 0:
                for m in range(3):
                    if m == k:
                        P_[m][0] = position_2[m]
                    else:
                        P_[m][0] = (position_2[k] - P_2[k][0]) * line3D[m] / line3D[k] + P_2[m][0]
            else:
                pass
            if position(P_) == [0,0,0]:
                break
        P_2 = P_

print(P_1)
print(P_2)

def printLine2D(P_1,P_2):
    if type(P_1) != np.array and type(P_2) != np.array:
        pass
    elif (P_1 == P_2).all():
        pass
    else:
        pass

printLine2D(P_1,P_2)