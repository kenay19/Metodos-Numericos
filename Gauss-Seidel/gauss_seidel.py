import numpy as np
from numpy import linalg 
import math
import os
import aux as aj 
os.system("clear")
print("===========================")
print("Metodo de Gauss-Seidel")
print("==========================")
it = int(input("De el numero de iteraciones: "))
A = np.loadtxt("matA.dat")
ren,col = np.shape(A)
print("==========================")
print(A)
print("==========================")
B = np.loadtxt("vecB.dat")
print("==========================")
print(B)
print("==========================")
T = np.zeros((ren,col),dtype=float)
T = (-1)*A
k = 0 
X0 = np.zeros((ren,1),dtype = float)
X1 = np.zeros((ren,1),dtype = float)
b = np.zeros((ren,1),dtype = float)
tol = pow(10,-5)
err = 1.0 
print("=========Verificacion Dominancia==========")
if(aj.domina(A)):
	T,b = aj.const(T,A,B,b)
	print("==========================")
	print(T)
	print("==========================")
	print(b)
	print("==========================")
	print("Ejecutando iteraciones")
	while k < it and err > tol:
		for i in range(ren):
			Xp = T[i,:]@X0
			X1[i] = b[i]+Xp
			err = linalg.norm(X1-X0)
			X0[i] = X1[i]
		k += 1
	print("===Se llego a la solucion===")
	print("====En la iteracion: ",k,"====")
	print("== y un error de: ",err,"===")
	print(X0)
else:
	print("El sistema no converge")