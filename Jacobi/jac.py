import numpy as np
from numpy import linalg
import math
import os
import aux as aj
os.system("clear")
print('===========================================')
print('================ METODO DE JACOBI =========')
print('======= FUNCIONES EN EL MODO AUX JAC ======')
ren=int(input("De el numero de ecuaciones: "))
it=int(input("De el numero de iteraciones: "))
A=np.zeros((ren,ren),dtype = float)
print('================ Matriz A ================')
A=np.loadtxt("matA.dat")
print(A)
B=np.zeros((ren,1),dtype = float)
print('================ Vector B ================')
B=np.loadtxt("vecB.dat")
print(B)
T=np.zeros((ren,ren),dtype = float)
print('================ Matriz T ================')
T=(-1)*A
print(T)
k=0
cont=0
X0=np.zeros((ren,1),dtype = float)
X1=np.zeros((ren,1),dtype = float)
b=np.zeros((ren,1),dtype = float)
t=np.zeros((ren,1),dtype = float)
tol=pow(10,-5)
err=1.0
if __name__=="__main__":
    print("=========VERIFICANDO DOMINANCIA=====")
    if(aj.domina(A)):
        T,b=aj.const(T,A,B,b)
        print(T)
        print("========================================")
        print(b)
        print('================================')
        print("Ejecutando iteraciones")
        print('================================')
        while(k<it and err> tol):
            t=T@X0
            X1=b+t
            err=np.linalg.norm(X1-X0)
            X0=X1        
            r2=A@X0
            r=B-r2    
            print("====Se llego a la solucion===")
            print("====en la iteracion=========",k)
            print("====y un error de===========",err)
            print(X0)
            print("===El vector residual es========")
            print(r) 
            k +=1
    else:
        print("El sistema no converge")