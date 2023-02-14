# import necessary modules
import math
import numpy as np
# import homogeneous transformation module
import p2_sol




if __name__ == "__main__":

    #set print formatting
    np.set_printoptions(precision = 2, suppress = True)
    
    ## TRANSFORMATION 1
    # set values of x, y, and z translations
    Tx = p2_sol.trans_x(2.5)
    Tz = p2_sol.trans_z(0.5)
    Ty = p2_sol.trans_y(-1.5)
    #multiply first two matrices
    H = np.matmul(Tx,Tz)
    #multiply result and final matrix to get final composite H_1
    H_1 = np.matmul(H,Ty)
    print("The H_1 transformation matrix is:\n",H_1)

    # TRANSFORMATION 2
    # set values of x, y, and z translations
    Tz = p2_sol.trans_z(0.5)
    Tx = p2_sol.trans_x(2.5)
    Ty = p2_sol.trans_y(-1.5)
    #multiply first two matrices
    H = np.matmul(Tz,Tx)
    #multiply result and final matrix to get final composite H_2
    H_2 = np.matmul(H,Ty)
    print("The H_2 transformation matrix is:\n ",H_2)

    # TRANSFORMATION 3 - fixed frame of transformation 1
    # set values of x, y, and z translations
    Tx = p2_sol.trans_x(2.5)
    Tz = p2_sol.trans_z(.5)
    Ty = p2_sol.trans_y(-1.5)
    # left multiply to calculate first matrix
    T = np.matmul(Tz, Tx)
    # multiply result with Ty array to get final H_3
    H_3 = np.matmul(T,Ty)
    print("The H_3 transformation matrix is:\n ",H_3)

    # Transformation 4 - fixed frame of transformation 2
    # set values of x, y, and z translations
    Tz = p2_sol.trans_z(0.5)
    Tx = p2_sol.trans_x(2.5)
    Ty = p2_sol.trans_y(-1.5)
    # left multiply to calculate composite of first two matices
    H = np.matmul(Ty,Tx)
    #multiply result with Ty to get final H_4
    H_4 = np.matmul(H,Tz)
    print("The H_4 transformation matrix is:\n ",H_4)

    #Transformation 5
    # set values for rotations and translations
    Rx = p2_sol.rot_x(math.pi / 2)
    Tx = p2_sol.trans_x(3.0)
    Tz = p2_sol.trans_z(-3.0)
    Rz = p2_sol.rot_z(-math.pi / 2)
    # right multiply first two arrays
    H = np.matmul(Rx,Tx)
    # right multiple the result by Tz
    H1 = np.matmul(H,Tz)
    # right multiply result H1 by Rz to get final H_5 matrix  
    H_5 = np.matmul(H1,Rz)
    print("The H_5 transformation matrix is:\n ",H_5)



