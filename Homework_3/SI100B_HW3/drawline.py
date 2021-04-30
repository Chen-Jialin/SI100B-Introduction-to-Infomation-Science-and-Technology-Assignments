import numpy as np
import matplotlib.pyplot as plt
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

def projection(x_3d,camera):
    #input camera_settings and a point(homogeneous) in real world
    #project it into image plane
    #computing projection matrix
   
    #return 2d point

    return 




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
   
   
   
   
   
   
   
   
   

def rasterization_dda(x1, x2, camera,w,h):
    #x1,x2 are 2d points in homogeneous coordinate e.g. [x,y,1]
    #plt.scatter(round(x), round(y), c='r'), use this function to draw a point
	#the size of image plane is (2*2) and here we must project the image plane to a window (w*h)

	
	
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
	
    x=np.array([-1.1,0,-1,1])
    y=np.array([0,1.1,-1,1])
	#groudtruth: Figure_4.png
	#You can use above groundtruth to demonstrate your program.
	#Write a function to read the data.txt. We will use other data to test your program and our test data will be the same format as we give you this time.
	
	
	
    cam=Camera(fov=90,focal_length=1,far=10,near=1,left=-1,right=1,bottom=-1,top=1)
    w=320 # w (width) and h(height) are the window size.
    h=240 # Here we need to project the image plane to the window in order to see the line more clearly. 
	
    
	# run your pipeline
	

            







  