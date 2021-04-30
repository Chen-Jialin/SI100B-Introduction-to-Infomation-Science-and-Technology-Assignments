import numpy as np
import matplotlib.pyplot as plt
import sys
#if your computer doesn't have matplotlib,you should install it on cmd by using following code.
#python -mpip install -U matplotlib


#Assuming near plane is the image plane
class Camera:
    '''
    define a class named "camera" with the parameters saved in it
    '''
    def __init__(self,fov,focal_length,far,near,left,right,bottom,top):#initialization: save the parameters in it once an example of the class is created
        self.fov=fov#field of version, not necessarily useful
        self.focal_length=focal_length#focal length, not necessarily useful
        self.far=far#the absolute of the z-coordinate of the far plane
        self.near=near#the abs of the z of the near plane(the image plane)
        self.left=left#the x-coordinate of the left side of the image plane
        self.right=right#the x of the right side of the image plane
        self.bottom=bottom#the y-coordinate of the bottom side of the image plane
        self.top=top#the y of the top side of the image plane

def dot(x,y,z):
    '''
    a function that transforms the coordinate of a 3D-dot into the form of homogeneous coordinate
    '''
    coordinate = np.ones((4,1))#define a null matrix sized 4*1 to save the homogeneous coordinte later
    coordinate[0][0] = x#get the x-coordinate
    coordinate[1][0] = y#get y
    coordinate[2][0] = z#get z
    return coordinate

def position(P):
    '''
    a function that judge the position of the 3D-dot relative to the cube in NDC
    '''
    position = []#define a empty list to save the information later
    for i in range(3):
        if P[i][0] < -1:#if the x,y,z-coordinate of the 3D-dot < -1
            position.append(-1)#the dot is on the right side of, above, in front of the cube
        elif P[i][0] > 1:#if x,y,z > 1
            position.append(1)#the dot is on the left side of, below, behind the cube
        else:#if -1 < x,y,z < 1
            position.append(0)#the dot is in the cube
    return position

def projection(P,camera,M):
    #input camera_settings and a point(homogeneous) in real world
    #project it into image plane
    #computing projection matrix
    if type(P) == type(None):#if the 3D-dot has been abandoned
        return None
    P = np.dot(np.linalg.inv(M),P)#get the dot product of the inverse of the perspective matrix and the homogeneous coordinate of the dot, to reget the coordinate in Perspective Frustum
    P = P * camera.near / P[2][0]#project the 3D-dot onto the image plane and get the its 2D-coordinate
    #return 2d point
    return P

def perspectiveMatrix(camera):
    '''
    a function to produce the perspective matrix according to the parameters of the camera
    '''
    M = np.zeros((4,4))#define a null matrix sized 4*4 to save the perspective matrix later
    M[0][0] = 2 * camera.near / (camera.right - camera.left)
    M[0][2] = (camera.right + camera.left) / (camera.right - camera.left)
    M[1][1] = 2 * camera.near / (camera.top - camera.bottom)
    M[1][2] = (camera.top + camera.bottom) / (camera.top - camera.bottom)
    M[2][2] = (camera.far + camera.near) / (camera.near - camera.far)
    M[2][3] = 2 * camera.far * camera.near / (camera.near - camera.far)
    M[3][2] = -1
    return M

def getline3D(P1,P2):
    '''
    a fuction to get the three parameters of the 3D-line according to its two endpoint
    '''
    line3D = []#define a empty list to save the parameters later
    line3D.append(P2[0][0] - P1[0][0])
    line3D.append(P2[1][0] - P1[1][0])
    line3D.append(P2[2][0] - P1[2][0])
    return line3D


def clipping_perspective(P1,P2,M):
    '''
    a function that transforms the coordinate of the two 3D-dots into the form of coordinate in NDC and clip
    '''
    P1 = np.dot(M,P1)#get the dot product of the perspective matrix and the 3D-dot P1, to transform the coordinate of the dot from the Perspective Frustum into a NDC
    P2 = np.dot(M,P2)#do the same things to P2
    if P1[3][0] == 0:#in case that dots' t-coordinat = 0 to raise ZeroDivisionError
        P1[3][0] = 1
    if P2[3][0] == 0:
        P2[3][0] = 1
    P1 = P1 / abs(P1[3][0])#make the t to be 1
    P2 = P2 / abs(P2[3][0])
    position1 = position(P1)#judge the position of the dots relative to the cube in NDC
    position2 = position(P2)

    if position1 == [0,0,0] and position2 == [0,0,0]:#if both two dots is in the cube
        pass#do nothing

    else:#if at least one dot is out of the cube, need to get the new dot that is the intersection of the 3D-line whose endpoint are the two dots with the cube
        line3D = getline3D(P1,P2)#get the 3D-line whose endpoints are the two dots
        P_ = np.array([[float('inf')],[float('inf')],[float('inf')],[1]])#define the homogeneous coordinate of the new dot P_ which is at infinity
        for i in range(3):
            if (position1[i] == -1 < position2[i]) or (position1[i] == 1 > position2[i]):#if the coorinate of P1 is not in the range of the cube, and the 3D-line has intersection with the cube
                for k in range(3):
                    if k == i:#make the corresponding coordinate of P_ equal the coordinate of corresponding plane of cube which is more close to the dot
                        P_[k][0] = position1[k]
                    else:#get the rest of the coordinate of P_
                        P_[k][0] = (position1[i] - P1[i][0]) * line3D[k] / line3D[i] + P1[k][0]
            if position(P_) == [0,0,0]:#when P_ is the real intersection of the 3D-line and the cube
                break#leave the loop
        if not((P_ == float('inf')).any()):#if P_ is not changed since defined, which means that P1 is in the cube, do not change P1
            P1 = P_#otherwise, update P1

        P_ = np.array([[float('inf')],[float('inf')],[float('inf')],[1]])#do the similar things if P2 is out of the cube
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

        if position(P1) != [0,0,0] or position(P2) != [0,0,0]:#if the (new) P1 and (new) P2 are still out of the cube after operations above
            P1 = None#abandon them
            P2 = None

    return P1,P2

def rasterization_dda(P1, P2, camera,w,h):
    #x1,x2 are 2d points in homogeneous coordinate e.g. [x,y,1]
    #plt.scatter(round(x), round(y), c='r'), use this function to draw a point
	#the size of image plane is (2*2) and here we must project the image plane to a window (w*h)
    if type(P1) != type(None):
        xa = w / (camera.left - camera.right)#because the window has different size and coordinate from the image, need transform the coordinate, and now get the parameters needed in transformation first
        xb = w * camera.right / (camera.right - camera.left)
        ya = h / (camera.bottom - camera.top)
        yb = h *camera.top / (camera.top - camera.bottom)

        x1 = int(xa * P1[0][0] + xb + 0.5)#transform the coordinate of the dots on image plane to the coordinates of their corresponding pixel in the window
        y1 = int(ya * P1[1][0] + yb + 0.5)
        x2 = int(xa * P2[0][0] + xb + 0.5)
        y2 = int(ya * P2[1][0] + yb + 0.5)

        dx = x2 - x1#the difference of x-coordinate of the two dots
        dy = y2 - y1#the difference of y

        if dx < 0:#if the x of P1 < x of P2
            dx = -dx#make the difference of x positive
            stepx = -1#the step of x's change is negative
        else:#if the x of P1 > x of P2
            stepx = 1#the step of x's change is positive
        if dy < 0:#do the similar thing to dy
            dy = -dy
            stepy = -1
        else:
            stepy = 1

        dx <<= 1#dx multiply 2 by left shift to avoid calculation on float
        dy <<= 1#do the same things to dy

        plt.scatter(x1,y1,c = 'r')#print the start in the window

        if dx > dy:#if the slope of the line < 1
            fraction = dy - (dx >> 1)#a variable that control when the y1 need + stepy
            while x1 != x2:#if reach the end point, leave the loop
                if fraction >= 0:
                    y1 += stepy
                    fraction -= dx
                x1 += stepx#get the x-coordinate for next dot
                fraction += dy
                plt.scatter(x1,y1,c = 'r')#print the dot in the window
        else:#do similar things if dx < dy
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
    plt.axis([0,w,0,h])#set the width and the height of the window
    frame=plt.gca()#define the window
    frame.axes.get_yaxis().set_visible(False)#set the x-axis is not visible
    frame.axes.get_xaxis().set_visible(False)#set the y-axis is not visible
    plt.show()#draw the line(s) on the window

if __name__ == '__main__':
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

        P1 = dot(m[0],m[1],m[2])#get the homogeneous coordinate of 3D-dot P1
        P2 = dot(m[3],m[4],m[5])#get the homogeneous coordinate of P2

        P1,P2 = clipping_perspective(P1,P2,M)#use perspective matrix to transform the 3D-dots P1 & P2 from Perspective Frustum to normalized device coordinates(NDC)

        P1 = projection(P1,cam,M)#use the inverse of perspective matrix M to transform the 3D-dots P1 from NDC back to perspective frustum and then project it to the image plane
        P2 = projection(P2,cam,M)#use M^(-1) to transform the P2 from NDC back to Perspective Frustum and then project it to the image plane

        rasterization_dda(P1,P2,cam,w,h)#use the coordinates of projected 2D-dots P1 & P2 to draw the corresponding line in the window
    drawline()#draw the lines