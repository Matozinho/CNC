import numpy as np
from sympy import *

def metEuler(function, h, x0, y0, endX):
  exp = lambdify(symbols('y'), (Symbol('y') + h * function))
  yn = y0
  xn = x0

  while xn < endX:
    yn = exp(yn)
    xn += h

  return yn

function = 0.8 * Symbol('y')
print("Método de Euler: ", metEuler(function, 0.2, 0, 20, 4))
