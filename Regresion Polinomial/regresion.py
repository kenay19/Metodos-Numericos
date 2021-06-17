import numpy as np 
from pylab import *
import os 

os.system("clear")
print("===============================================================")
print("================ Metodo de Regresion No Lineal ================")
print("===============================================================")

n = int(input("Da el grado de la funcion deseada: "))

X = np.loadtxt("vecX.dat")
print("================ Vector X ================")
print(X)
Y = np.loadtxt("vecY.dat")
print("================ Vector Y ================")
print(Y)
A = np.zeros((len(X),n+1),dtype = float)
for i in range(0,n+1,1):
	A[:,i] = X**i
print("================ Matriz A ================")
print(A)
At = A.transpose()
print("================ Matriz Traspuesta de A ================")
print(At)
M = At@A
print("================ Matriz M ================")
print(M)
print("================ Matriz Aumentada ================")
Z = np.column_stack((M,At@Y))
print(Z)
for i in range(0,n,1):
	for j in range(i+1,n+1,1):
		Z[j,:] = Z[j,:] - (Z[j,i]*(Z[i,:]/Z[i,i]))
print("================ Eliminacion Gaussiana ================")
print(Z)
P = Z[:,n+1]
K = n
for i in range(n,-1,-1):
	for j in range(n,-1,-1):
		if j >= i :
			if j == i:
				P[i] = P[i]/Z[i,i]
			else:
				P[i] = P[i] - (Z[i,j]*P[K])
				K += -1
	K = n
print("================ Vector solucion ================")
print(P)
yc = 0
for i in range(0,n+1,1):
	yc = yc +P[i]*(A[:,i])
print("================ Vector Residual ================")
R = Y-yc.transpose()
err = np.linalg.norm(R)/np.sqrt(len(X))
print(R)
print("================ Error Medio Cuadratico ================")
print(err)
sn =input("Desea hacer pronosticos? S,N: ")
if sn == 'S':
	print("================ Vector Pronostrico ================")
	XP = np.loadtxt("vecXP.dat")
	print(XP)
	e = 0
	print("================ Valores Pronosticados ================")
	for i in range(0,n+1,1):
		e = e + P[i]*(XP**i)
	print(e)
	plot(XP,e,'o')
plot(X,Y)
plot(X,yc)	
grid()
show()