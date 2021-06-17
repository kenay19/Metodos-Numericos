import numpy as np
import matplotlib.pyplot as plt 
import fun as f
import math 

def graf():
	x1 = np.linspace(1,5,100)
	x2 = np.linspace(1,5,100)
	y = f.gt(x1)
	z = f.ld(x1)
	v = f.fa(x1)

	plt.subplot(2,1,1)
	plt.plot(x1,y,color = "blue")
	plt.plot(x1,z,color = "green")

	plt.grid()

	plt.subplot(2,1,2)
	plt.plot(x1,v,color = "red")
	plt.grid()

	plt.show()