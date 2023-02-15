import rbm
import math
import numpy as np

if __name__ == "__main__":
	theta = math.pi / 2
	phi = math.pi/2
	psi = math.pi/2
	
	np.set_printoptions(precision = 2, suppress = True)
	Rx = p1_sol.rot_roll(psi)
	Ry = p1_sol.rot_pitch(theta)
	Rz = p1_sol.rot_yaw(phi)
	R1 = np.matmul(Rx, Ry)
	R = np.matmul(R1, Rz)

	print("The results of the Roll-Pitch-Yaw rotation for the given angles is: ", R)
    
