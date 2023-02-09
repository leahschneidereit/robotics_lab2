import math
import numpy as np

def rot_roll(psi):
	'''
	'''
	
	rot = np.array([[1.0, 0.0, 0.0], [0.0, math.cos(psi), -math.sin(psi)],[0.0, math.sin(psi), math.cos(psi)]])
	
	return rot
	
def rot_pitch(theta):
	'''
	'''
	
	rot = np.array([[math.cos(theta), 0.0, math.sin(theta)],[0.0,1.0,0.0],[-math.sin(theta), 0.0, math.cos(theta)]])
	
	return rot

def rot_yaw(phi):
	'''
	'''
	
	rot = np.array([[math.cos(phi), -math.cos(phi), 0.0], [math.sin(phi), math.cos(phi), 0.0],[0.0, 0.0, 1.0]])
	
	return rot

def vec(x, y, z):
	vec = np.array([[x,y,z]]).T
	return vec
