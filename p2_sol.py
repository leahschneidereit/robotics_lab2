# problem 2: develop a module that contains basic homogeneous transormations
# use equations in slides for 6 basic motions
import math
import numpy as np

#def trans_one(a,b,d,theta):
a = 2.5
b = 0.5
d = -1.5
theta = math.pi/2
transform = np.array([[math.cos(theta), -math.sin(theta), 0, b], [math.cos(a)*math.sin(theta), math.cos(a)*math.cos(theta), -math.sin(a),-d*math.sin(a)], [math.sin(a)*math.sin(theta), math.sin(a)*math.cos(theta), math.cos(a), d*math.cos(a)],[0.0,0.0,0.0,1.0]])
	
print (transform)
