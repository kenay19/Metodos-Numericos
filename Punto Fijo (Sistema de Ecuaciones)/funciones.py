from numpy import *

f1 = lambda x: x[0]+2*x[1]-2
f2 = lambda x: x[0]**2+4*x[1]**2-4

xf1 = lambda x: 1+0*x[0]+0*x[1]
yf1 = lambda x: 0*x[0]+2+0*x[1]

xf2 = lambda x: 2*x[0]+0*x[1]
yf2 = lambda x:0*x[0]+8*x[1]

g1 = lambda x: (-cos(x[1]*x[2])/3)+(1/6)
g2 = lambda x: (1/9)*sqrt(pow(x[0],2)+sin(x[2])+1.06) +0.1
g3 = lambda x: -(exp(-x[0]*x[1])/20)-((10*pi-3)/20)