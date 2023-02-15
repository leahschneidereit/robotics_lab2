# Here we write some functions that help us analayze the motions of a rigid body

# import the required modules
import math
import numpy as np


# use lecture slides for the mathematical equations 
def rot_x(psi):
	rot = np.array([[1.0,  0.0, 0.0],
				    [0.0, math.cos(psi), -math.sin(psi)],
					[0.0, math.sin(psi), math.cos(psi)]])
	return rot
	
def rot_y(theta):
	rot = np.array([[math.cos(theta),  0.0, math.sin(theta)],
				    [0.0, 1.0, 0.0],
					[-math.sin(theta), 0.0, math.cos(theta)]])
	return rot
	
def rot_z(phi):
	rot = np.array([[math.cos(phi),  -math.sin(phi), 0.0],
					[math.sin(phi),   math.cos(phi), 0.0],
				    [0.0, 0.0, 1.0]])
	return rot
	
