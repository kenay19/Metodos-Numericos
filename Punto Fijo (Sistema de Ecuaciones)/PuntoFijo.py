from numpy import *
import os
import funciones as f                               
os.system("clear")
print("======================================================")
print("================ Metodo de Punto Fijo ================")
print("================== Varias Variables ==================")
print("======================================================")
tol = pow(10,-5)
err = 1
k = 0 
it = int(input("De el numero de iteraciones: "))
print("================ Vector Inicial ================")
X0 = loadtxt("vecX.dat")
print(X0)
print("================ Ejecutando Iteraciones ================")
print("k\t\t x\t\t\t y\t\t z\t\t error")
while k < it and err > tol:
	k+=1
	X1 = array(([f.g1(X0),f.g2(X0),f.g3(X0)]),dtype = float)
	err = linalg.norm(X1-X0)
	print(k,"[",X1[0],",",X1[1],",",X1[2],"]",err)
	X0 = X1
print("======================================================")
print("================ Vector Resultado ================",X0)