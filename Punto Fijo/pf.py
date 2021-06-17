import numpy as np 
import fun as f
import graf
import os
import math
os.system("clear")
print("==================================")
print("====== Metodo de Punto Fijo ======")
print("==================================")
xo = float(input("De el punto inicial: "))
i = int(input("De el numero de iteraciones: "))
k = int(0)
tol = float(pow(10,-5))
err = float(5.0)
fc1 = float(125)
print("Calculando la raiz")
print("Iteracion \t  x0 \t fx \t error")
while k < i and err > tol:
	fc = f.gt(xo)
	err = abs((fc-xo)/fc)
	if abs(fc1 < fc):
		print("Esta divirgiendo u oscilando")
		k = 100
	k += 1
	print(k," \t ",xo," \t ",fc," \t ",err)
	xo = fc
if err < tol:
	print("La raiz es x = ",xo)
elif abs(fc1 < fc):
	print("Esta divirgiendo u oscilando")
graf.graf()