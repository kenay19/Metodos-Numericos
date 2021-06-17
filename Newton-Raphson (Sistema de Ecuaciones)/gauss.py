import numpy as np 

def gauss(Au):
	ren,col = np.shape(Au)
	for i in range(0,ren-1,1):
		for j in range(i+1,ren,1):
			Au[j,:] = Au[j,:] - (Au[j,i]*(Au[i,:]/Au[i,i])) 
	X = Au[:,col-1]
	K = ren-1
	for i in range(ren-1,-1,-1):
		for j in range(ren-1,-1,-1):
			if j >= i :
				if j == i:
					X[i] = X[i]/Au[i,i]
				else:
					X[i] = X[i] - (Au[i,j]*X[K])
					K += -1
		K = ren-1	
	return X