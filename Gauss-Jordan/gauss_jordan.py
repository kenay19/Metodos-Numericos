import numpy as np 
import os
os.system("clear")
print("===============================")
print("====Metodo de Gauss-Jordan=====")
print("===============================")
ren = int(input("De el numero de Renglones: "))
col = int(input("De el numero de Columnas: "))
Au = np.loadtxt("matAu.dat")
print("========================================")
print("Sistema de ecuaciones ",ren," x ",col,"")
print("========================================")
print(Au)
print("============================")
print("ELiminacion hacia adelante")
print("============================")
for i in range(0,ren-1,1):
	Au[i,:] = Au[i,:]/Au[i,i]
	for j in range(i+1,ren,1):
		Au[j,:] = Au[j,:] - (Au[i,:]*Au[j,i])
print(Au)	
print("========================")
print("Eliminacion hacia atras")
print("========================")
for i in range(ren-1,0,-1) :
	Au[i,:] = Au[i,:]/Au[i,i]
	for j in  range(i-1,-1,-1):
		Au[j,:] = Au[j,:] - (Au[i,:]*Au[j,i])
print(Au)
print("========================")
print("Vector Solucion")
print("========================")
print(Au[:,col-1])