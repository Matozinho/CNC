from sympy import *

def metHeun(y, x0, y0, endX, h):
  xn = x0
  yn = y0

  while xn < endX:
    yn = yn + ((h/2) * (y(yn) + y(yn + (h * y(yn)))) )
    xn += h
  
  return yn

y = lambdify(symbols('y'), 200 - ((200 / 400000) * Symbol('y')))

print("Método de Heun: ", metHeun(y, 0, 10*400000, 120, .5))
