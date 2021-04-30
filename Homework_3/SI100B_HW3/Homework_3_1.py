import numpy as np
import matplotlib.pyplot as plt
import sys
#if your computer doesn't have matplotlib,you should install it on cmd by using following code.
#python -mpip install -U matplotlib


#Assuming near plane is the image plane
class Camera:
    def __init__(self,fov,focal_length,far,near,left,right,bottom,top):
        self.fov=fov
        self.focal_length=focal_length
        self.far=far
        self.near=near
        self.left=left
        self.right=right
        self.bottom=bottom
        self.top=top

def dot(x,y,z):
    coordinate = np.ones((4,1))
    coordinate[0][0] = x
    coordinate[1][0] = y
    coordinate[2][0] = z
    return coordinate

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

def projection(P,camera,M):
    #input camera_settings and a point(homogeneous) in real world
    #project it into image plane
    #computing projection matrix
    if type(P) == type(None):
        return None
    P = np.dot(np.linalg.inv(M),P)
    P = P * camera.near / P[2][0]
    #return 2d point
    return P

def perspectiveMatrix(camera):
    M = np.zeros((4,4))
    M[0][0] = 2 * camera.near / (camera.right - camera.left)
    M[0][2] = (camera.right + camera.left) / (camera.right - camera.left)
    M[1][1] = 2 * camera.near / (camera.top - camera.bottom)
    M[1][2] = (camera.top + camera.bottom) / (camera.top - camera.bottom)
    M[2][2] = (camera.far + camera.near) / (camera.near - camera.far)
    M[2][3] = 2 * camera.far * camera.near / (camera.near - camera.far)
    M[3][2] = -1
    return M

def getline3D(P1,P2):
    line3D = []
    line3D.append(P2[0][0] - P1[0][0])
    line3D.append(P2[1][0] - P1[1][0])
    line3D.append(P2[2][0] - P1[2][0])
    return line3D


def clipping_perspective(P1,P2,M):
    P1 = np.dot(M,P1)
    P2 = np.dot(M,P2)
    if P1[3][0] == 0:
        P1[3][0] = 1
    if P2[3][0] == 0:
        P2[3][0] = 1
    P1 = P1 / abs(P1[3][0])
    P2 = P2 / abs(P2[3][0])
    position1 = position(P1)
    position2 = position(P2)

    if position1 == [0,0,0] and position2 == [0,0,0]:
        pass

    else:
        line3D = getline3D(P1,P2)
        P_ = np.array([[float('inf')],[float('inf')],[float('inf')],[1]])
        for i in range(3):
            if (position1[i] == -1 < position2[i]) or (position1[i] == 1 > position2[i]):
                for k in range(3):
                    if k == i:
                        P_[k][0] = position1[k]
                    else:
                        P_[k][0] = (position1[i] - P1[i][0]) * line3D[k] / line3D[i] + P1[k][0]
            if position(P_) == [0,0,0]:
                break
        if not((P_ == float('inf')).any()):
            P1 = P_

        P_ = np.array([[float('inf')],[float('inf')],[float('inf')],[1]])
        for i in range(3):
            if (position2[i] == -1 < position1[i]) or (position2[i] == 1 > position1[i]):
                for k in range(3):
                    if k == i:
                        P_[k][0] = position2[k]
                    else:
                        P_[k][0] = (position2[i] - P2[i][0]) * line3D[k] / line3D[i] + P2[k][0]
            if position(P_) == [0,0,0]:
                break
        if not((P_ == float('inf')).any()):
            P2 = P_

        if position(P1) != [0,0,0] or position(P2) != [0,0,0]:
            P1 = None
            P2 = None

    return P1,P2

'''
def clipping_3d(x1,x2,camera):
    #x1 is numpy arrary in homogeneous [x,y,z,1]
    

def encode(x1):
    #x is 2d point 
    #output binary embedding code
    if(x1[0]<=1 and x1[0]>=-1 and x1[1]<=1 and x1[1]>=-1):
        return int('0000',2)
    if((x1[0]>=1 and x1[1]>=1)):
        return int('1010',2)
    if((x1[0]>-1 and x1[0]<1) and x1[1]>1):
        return int('1000',2)
    if(x1[0]<=-1 and x1[1]>=1):
        return int('1001',2)
    if(x1[0]<-1 and (x1[1]>-1 and x1[1]<1)):
        return int('0001',2)
    if(x1[0]<=-1 and x1[1]<=-1):
        return int('0101',2)
    if(x1[0]>-1 and x1[0]<1 and x1[1]<-1):
        return int('0100',2)
    if(x1[0]>=1 and x1[1]<=-1):
        return int('0110',2)

def clipping_2d(x1,x2,camera):
    #x1,x2 are 2d points in homogeneous coordinate e.g. [x,y,1]
'''









def rasterization_dda(P1, P2, camera,w,h):
    #x1,x2 are 2d points in homogeneous coordinate e.g. [x,y,1]
    #plt.scatter(round(x), round(y), c='r'), use this function to draw a point
	#the size of image plane is (2*2) and here we must project the image plane to a window (w*h)
    if type(P1) != type(None):
        xa = w / (camera.left - camera.right)
        xb = w * camera.right / (camera.right - camera.left)
        ya = h / (camera.bottom - camera.top)
        yb = h *camera.top / (camera.top - camera.bottom)

        x1 = int(xa * P1[0][0] + xb + 0.5)
        y1 = int(ya * P1[1][0] + yb + 0.5)
        x2 = int(xa * P2[0][0] + xb + 0.5)
        y2 = int(ya * P2[1][0] + yb + 0.5)

        dx = x2 - x1
        dy = y2 - y1

        if dx < 0:
            dx = -dx
            stepx = -1
        else:
            stepx = 1
        if dy < 0:
            dy = -dy
            stepy = -1
        else:
            stepy = 1

        dx <<= 1
        dy <<= 1

        plt.scatter(x1,y1,c = 'r')

        if dx > dy:
            fraction = dy - (dx >> 1)
            while x1 != x2:
                if fraction >= 0:
                    y1 += stepy
                    fraction -= dx
                x1 += stepx
                fraction += dy
                plt.scatter(x1,y1,c = 'r')
        else:
            fraction = dx - (dy >> 1)
            while y1 != y2:
                if fraction >= 0:
                    x1 += stepx
                    fraction -= dy
                y1 += stepy
                fraction += dx
                plt.scatter(x1,y1,c = 'r')

def drawline():
    #set plot attribute
    plt.axis([0,w,0,h])
    frame=plt.gca()
    frame.axes.get_yaxis().set_visible(False)
    frame.axes.get_xaxis().set_visible(False)
    plt.show()

if __name__ == '__main__':
    #x=np.array([-0.75,-0.25,-1.3,1])
    #y=np.array([10,10,-1.4,1])
	#groudtruth: Figure_1.png

    #x=np.array([-0.75,-0.25,-1.3,1])
    #y=np.array([-0.75,0.75,-1.3,1])
	#groudtruth: Figure_2.png

    #x=np.array([-0.75,0.75,-1.3,1])
    #y=np.array([0.25,0.75,-1.3,1])
	#groudtruth: Figure_3.png

    #x=np.array([-1.1,0,-1,1])
    #y=np.array([0,1.1,-1,1])
	#groudtruth: Figure_4.png
	#You can use above groundtruth to demonstrate your program.
	#Write a function to read the data.txt. We will use other data to test your program and our test data will be the same format as we give you this time.



    cam=Camera(fov=90,focal_length=1,far=10,near=1,left=-1,right=1,bottom=-1,top=1)#define the parameters of the camera
    w=320 # w (width) and h(height) are the window size.
    h=240 # Here we need to project the image plane to the window in order to see the line more clearly. 

	# run your pipeline

    dots = sys.stdin.read()#get the input
    dots = dots.split('\n')#separate each pair of 3D-dots
    for l in range(len(dots)):#separate the six coordinates of each pair of 3D-dots
        dots[l] = dots[l].split()

    M = perspectiveMatrix(cam)#get the perspective matrix

    for m in dots:
        if m == []:#if there does not exist any coordinates
            continue#skip the loop
        for n in m:#transform the coordinates of the 3D-dots from the form of string to the form of the float for convenience of further operation
            n = float(n)

        P1 = dot(m[0],m[1],m[2])#get the homogeneous coordinates of 3D-dot P1
        P2 = dot(m[3],m[4],m[5])#get the homogeneous coordinates of 3D-dot P2

        P1,P2 = clipping_perspective(P1,P2,M)#use perspective matrix to transform the 3D-dots P1 & P2 from perspective frustum to normalized device coordinates(NDC)

        P1 = projection(P1,cam,M)#use the inverse of perspective matrix M to transform the 3D-dots P1 from NDC back to perspective frustum and then project it to the screen
        P2 = projection(P2,cam,M)#use the inverse of perspective matrix M to transform the 3D-dots P2 from NDC back to perspective frustum and then project it to the screen

        rasterization_dda(P1,P2,cam,w,h)#use the coordinates of projected 2D-dots P1 & P2 to draw the dorresponding line on the screen
    drawline()#draw the lines