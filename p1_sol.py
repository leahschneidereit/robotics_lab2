# import necessary modules
import rbm
import math
import numpy as np

if __name__ == "__main__":
        #initialize angles to pi/2 radians (from problem statement)
	theta = math.pi / 2
	phi = math.pi/2
	psi = math.pi/2
	
	#set print options
	np.set_printoptions(precision = 2, suppress = True)

	# call methods from rbm to calculate matrix for each rotation
	Rx = rbm.rot_x(psi)
	Ry = rbm.rot_y(theta)
	Rz = rbm.rot_z(phi)
	
	# matrix multiplication to determine result of Roll-Pitch-Yaw rotation
	R1 = np.matmul(Rx, Ry)
	R = np.matmul(R1, Rz)

        #print result
	print("The results of the Roll-Pitch-Yaw rotation for the given angles is: \n", R)
    
