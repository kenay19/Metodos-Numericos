import numpy as np 
import os
import fun as f
os.system("clear")
print("==========================================")
print("======== Metodo de Newton-Rhapson ========")
print("==========================================")
tol = pow(10,-5)
err = float(1.0)
j = 0
pi = float(input("De el numero de partida: "))
i = int(input("De el numero de iteraciones: "))
print("Iteracion \t x0  \t err")
while j < i and err > tol:
	pivote = pi
	x = pi - (f.fo(pi)/f.fd1(pi))
	j+=1
	print(j,"\t",pi,"\t",err)
	err = abs(x-pivote)
	pi = x
print("La raiz de f(x)es x = ",x)