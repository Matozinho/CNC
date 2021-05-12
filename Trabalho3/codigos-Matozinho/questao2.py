import numpy as np
from sympy import *

def metHeun(k1, k2, x0, y0, endX, h):
  xn = x0
  yn = y0

  k1 = lambdify(symbols('x y'), k1)
  k2 = lambdify(symbols('x y h'), k2)

  while xn < endX:
    yn = yn + ((h/2) * (k1(xn, yn) + k2(xn, yn, h)))
    xn += h

  return yn

# k1 = f(x,y)
k1 = -.01 * Symbol('y')

# k2 = f(x+h, y+h*f(x,y))
k2 = -.01 * (Symbol('y') + Symbol('h') * (-.01 * Symbol('y')))

print("Método de Heun: ", metHeun(k1, k2, 0, 10, 4, .2))
