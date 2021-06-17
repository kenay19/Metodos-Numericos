import numpy as np 
import matplotlib.pyplot as mp 
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
fa = f.fo(Ii)
fb = f.fo(Id)
print("f(a) = ",fa)
print("f(b) = ",fb)
if fa * fb >= 0 :
	if fa == 0 or fb == 0:
		print("Hay unar raiz en a o b")
	else:
		print("En este intervalo no hay una raiz")
else : 
	print("Calculando la raiz")
	print("Iteracion \t  a \t b \t c \t fc")
	while j < i : 
		j +=1 
		Ic = float(Ii +Id)/2
		fa = f.fo(Ii)
		fc = f.fo(Ic)
		print(j,"\t",Ii,"\t",Id,"\t",Ic,"\t",fc)
		if fa*fc > 0:
			Ii = Ic
		else: 
			Id = Ic
	print("La raiz de f(x) es x = ",Ic)
x = np.linspace(s,b,50)
y = f.fo(x)
figure, ax = mp.subplots()
ax.plot(x,y)
ax.grid()
mp.show()