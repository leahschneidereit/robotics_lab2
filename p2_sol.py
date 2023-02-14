# import necessary modules
import math
import numpy as np

# this is a module containing methods that calculate the standard matrix for the
# 6 homogeneous transformations
def trans_x(a):
    '''This function builds the standard array for a translation along the
    x-axis
    '''
    transform = np.array([[1.0,0.0,0.0,a],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],
                      [0.0,0.0,0.0,1.0]])
    return transform
def trans_y(b):
    '''This function builds the standard array for translation along the y-axis
    '''
    transform = np.array([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,b],[0.0,0.0,1.0,0.0],
                          [0.0,0.0,0.0,1.0]])
    return transform

def trans_z(c):
    '''This function builds the standard array for translation along the z-axis
    '''
    transform = np.array([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,c],
                          [0.0,0.0,0.0,1.0]])
    return transform

def rot_x(a):
    ''' This function builds the standard array for rotation along the x-axis
    '''
    rot_x = np.array([[1.0,0.0,0.0,0.0],[0.0,math.cos(a),-math.sin(a),0.0],
                      [0.0,math.sin(a),math.cos(a),0.0],[0.0,0.0,0.0,1.0]])
    
    return rot_x

def rot_y(b):
    '''This function builds the standard array for rotation along the y-axis
    '''
    rot_y = np.attay([[math.cos(b),0.0,math.sin(b),0.0],[0.0,1.0,0.0,0.0],
                      [-math.sin(b),0.0,math.cos(b),0.0],[0.0,0.0,0.0,1.0]])
    return rot_y

def rot_z(gamma):
    '''This function builds the standard array for rotation along the z-axis
    '''
    rot_z = np.array([[math.cos(gamma), -math.sin(gamma), 0.0,0.0],
                      [math.sin(gamma),math.cos(gamma),0.0,0.0],[0.0,0.0,1.0,0.0],
                      [0.0,0.0,0.0,1.0]])
    return rot_z
