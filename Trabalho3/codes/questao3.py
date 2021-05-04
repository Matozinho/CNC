import numpy as np
from sympy import *

def metHeun(k1, k2, x0, y0, endY, h):
  xn = x0
  yn = y0
  k1 = lambdify(symbols('x y'), k1)
  k2 = lambdify(symbols('x y h'), k2)

  while yn > endY:
    yn = yn + ((h/2) * (k1(xn, yn) + k2(xn, yn, h)))
    xn += h
  
  return xn

# f(x) = k*y
k = -1.244*10**-4 

# k1 = h * f(x, y)
k1 = (k * Symbol('y'))
# k2 = f(x + h, y+h*k1)
k2 = k * (Symbol('y') + (Symbol('h') * k1))

print(metHeun(k1, k2, 0, 1, .92, .5))
