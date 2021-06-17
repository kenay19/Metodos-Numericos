import numpy as np
from numpy import *
import math

# Secante, Newton-Rapshon, Biseccion
fo = lambda x: 2*x**3-11*x**2+17*x-5
fd1 = lambda x: 6*x**2-22*x+17
fd2 = lambda x: 18*x

# PUNTO FIJO
gt = lambda x : 2*sqrt(x)
ld = lambda x : x
fa = lambda x : 2*sqrt(x)-x