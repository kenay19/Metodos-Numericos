import numpy as np
from numpy import linalg,sum
import math
def domina(A):
    ren,col=np.shape(A)
    cont=0.0
    S=0.0
    for i in range(ren):
        S=A.sum(axis=1)
        if (math.fabs(A[i][i]) >=(S[i]-A[i][i])):
            cont +=1
    if(cont != ren):
      print("La matriz no es diagonal dominante")
      return False
    
    else:
      print("La matriz es diagonal dominante")
      return True
    return
    
def const(T,A,B,b):
    ren,col = np.shape(T)
    for i in range(ren):
        T[i,:]=T[i,:]/A[i,i]
        b[i]=B[i]/A[i,i]
        T[i,i]=0.0
    return T, b
        
def jacobi_it(i,X0,T,b,arr):
    Xp = T[i,:] @ X0
    arr[i]=b[i]+Xp