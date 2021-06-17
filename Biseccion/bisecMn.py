import numpy as np 
import matplotlib.pyplot as mp 
import time 
import math 
import os 
import fun as f

os.system("clear")
print("===========================================")
print("=========== Metodo de Biseccion ===========")
print("===========================================")

Ii = float(input("De el intervalo izquierdo a: "))
Id = float(input("De el intervalo derecho b: "))

s = Ii
b = Id

if Ii > Id :
	Ii = b
	Id = s
	print("Los extremos se han invertido")

i = int(input("De el numero de iteraciones: "))
j = 0
tol = float(pow(10,-5))
err = float(1.0)

fa = f.fd1(Ii)
fb = f.fd1(Id)

print("f(a) = ",fa)
print("f(b) = ",fb)

if fa * fb >= 0 :
	if fa == 0 or fb == 0:
		print("Hay unar raiz en a o b")
	else:
		print("En este intervalo no hay una raiz")
else : 
	print("Calculando la raiz")
	print("Iteracion \t  a \t b \t c \t fc \t error")
	while j < i and err > tol: 
		j +=1 
		Ic = float(Ii +Id)/2
		fc = f.fo(Ic)
		print(j,"\t",Ii,"\t",Id,"\t",Ic,"\t",fc,"\t", err)
		time.sleep(0.2)
		if fa*fc > 0:
			Ii = Ic
			fa = fc
		else: 
			Id = Ic
			fb = fc
		err = abs((Id-Ii)/2)
	print("La raiz de f'(x) es x = ",Ic)
	if f.fd2(Ic) > 0 :
		print("La segunda derivada es positiva")
	else: 
		print("La segunda derivada es negativa")

x = np.linspace(s,b,50)
y = f.fo(x)
z = f.fd1(x)
v = f.fd2(x)
figure, ax = mp.subplots()
ax.plot(x,y)
ax.plot(x,z)
ax.plot(x,v)
ax.grid()
mp.show()