from sympy import *

def metHeun(y, x0, y0, endY, h):
  xn = x0
  yn = y0

  while yn > endY:
    yn = yn + ((h/2) * (y(yn) + y(yn + (h * y(yn)))) )
    xn += h
  
  return xn

y = lambdify(symbols('y'), 200 - ((200 / 400000) * Symbol('y')))

print("Método de Heun: ", metHeun(y, 0, 10*400000, 2.1*400000, .5))
