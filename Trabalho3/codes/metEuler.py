import numpy as np
from sympy import *

def metEuler(function, h, x0, y0, endX):
  exp = lambdify(symbols('x y'), (Symbol('y') + h * function))
  yn = y0
  xn = x0

  while xn < endX:
    yn = exp(xn, yn)
    xn += h
  
  return yn

function = Symbol('x') - Symbol('y') + 2
print(metEuler(function, 0.2, 0, 20, ))