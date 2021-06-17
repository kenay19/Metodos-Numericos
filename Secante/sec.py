import numpy as np
import os
import fun as f 

os.system("clear")

print("========================================")
print("========= Metodo de la Secante =========")
print("========================================")

tol = pow(10,-5)
err = float(1.0)
j = 0 

Ii = float(input("De el intervalo izquierdo: "))
Id = float(input("De el intervalo derecho: "))

i = int(input("De el numero iteraciones: "))

print("Iteraciones \t a \t b \t f(a) \t f(b) \t error \t raiz")
while j < i and err > tol:
	j += 1
	fa = f.fo(Id)
	fb = f.fo(Ii)
	x = Id- (fa*(Ii-Id)/(fb-fa))
	print(j," \t ",Ii," \t ",Id," \t ",fb, " \t ",fa ," \t ",err," \t ",x)
	if (Id-x) < (x-Ii):
		err = abs(Id-x)
		Ii = x
	else:
		err = abs(x-Ii)
		Id = x 
print("La raiz de f(x) es x = ",x)