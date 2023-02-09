import p1_sol
import math
import numpy as np

if __name__ == "__main__":
	theta = math.pi / 2
	phi = math.pi/2
	psi = math.pi/2
	
	np.set_printoptions(precision = 2, suppress = True)
	v0 = p1_sol.vec(0,1,1)
	Rx = p1_sol.rot_roll(psi)
	Ry = p1_sol.rot_pitch(theta)
	Rz = p1_sol.rot_yaw(phi)
	R = np.matmul(Ry, Rz)
	v01 = R.dot(v0)
	R = np.matmul(Rz, Ry)
	v01 = R.dot(v0)
	R = np.matmul(Rz, Ry)
	v01 = R.dot(v0)
	print('The transformed vector is:\n', v01)
