from numpy import *
import math
import funciones
import gauss
import os
os.system("clear")
print("=======================================================================")
print("========================== Metodo de Newton ===========================")
print("================== Sistema de Ecuaniones no Lineales ==================")
print("=======================================================================")
it = int(input("De el numero de iteraciones: "))
k = 0
error = pow(10,-5)
e = 1
X0 = loadtxt("vecX.dat")
print("========================== Vector Inicial ===========================")
print(X0)
print("iteracion\tX1\tX2\terror")
while(k < it and e > error):
	k+=1
	J = array(([funciones.xf1(X0),funciones.yf1(X0)],[funciones.xf2(X0),funciones.yf2(X0)]),dtype = float)
	B = array(([-funciones.f1(X0)],[-funciones.f2(X0)]))
	Z = column_stack((J,B))
	h = gauss.gauss(Z)
	X1 = X0 + h
	print(k,"[",X1[0],",",X1[1],"]",e)
	e = linalg.norm(X1-X0)
	X0 = X1