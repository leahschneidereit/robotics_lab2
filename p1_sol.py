import math
import numpy as np

def rot_roll(psi):
	'''
        This function returns a matrix for a roll rotation (about the x-axis)
	'''
	
	rot = np.array([[1.0, 0.0, 0.0], [0.0, math.cos(psi), -math.sin(psi)],[0.0, math.sin(psi), math.cos(psi)]])
	
	return rot
	
def rot_pitch(theta):
	'''
        This function returns a matrix for a pitch rotation (about the y axis)
	'''
	
	rot = np.array([[math.cos(theta), 0.0, math.sin(theta)],[0.0,1.0,0.0],[-math.sin(theta), 0.0, math.cos(theta)]])
	
	return rot

def rot_yaw(phi):
	'''
        This function returns a matrix for a yaw rotation (about the z-axis)
	'''
	
	rot = np.array([[math.cos(phi), -math.cos(phi), 0.0], [math.sin(phi), math.cos(phi), 0.0],[0.0, 0.0, 1.0]])
	
	return rot

def vec(x, y, z):
        '''
        This function initializes the vector orientation as an array of its
        x, y, and z positioning
        '''
	vec = np.array([[x,y,z]]).T
	return vec
