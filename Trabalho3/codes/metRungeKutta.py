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

def metHeun(k1, k2, x0, y0, endX, h):
  xn = x0
  yn = y0
  k1 = lambdify(symbols('x y'), k1)
  k2 = lambdify(symbols('x y h'), k2)

  while xn < endX:
    yn = yn + ((h/2) * (k1(xn, yn) + k2(xn, yn, h)))
    xn += h
  
  return yn

def metRungeKutta(order, k1, k2, k3, k4, x0, y0, endX, h):
  if order==1:
    return metEuler(k1, h, x0, y0, endX)

  elif order==2:
    return metHeun(k1, k2, x0, y0, endX, h)

  elif order==3:
    xn = x0
    yn = y0
    k1 = lambdify(symbols('x y'), k1)
    k2 = lambdify(symbols('x y h'), k2)
    k3 = lambdify(symbols('x y h'), k3)

    while xn < endX:
      yn = yn + ((2/9) * k1(xn, yn)) + ((1/3) * k2(xn, yn, h)) + ((4/9) * k3(xn, yn, h))
      xn += h
    
    return yn
  
  elif order==4:
    xn = x0
    yn = y0
    k1 = lambdify(symbols('x y'), k1)
    k2 = lambdify(symbols('x y h'), k2)
    k3 = lambdify(symbols('x y h'), k3)
    k4 = lambdify(symbols('x y h'), k4)

    while xn < endX:
      yn = yn + ((1/6) * k1(xn, yn) + 2*k2(xn, yn, h) + 2*k3(xn, yn, h) + k4(xn, yn, h))
      xn += h

    return yn 

# f(x) = k*y
# k = -1.244*10**-4 

# k1 = h * f(x, y)
k1 = .1 * (Symbol('x') - Symbol('y') + 2)
# k2 = h * f(x+(h/2), y+(k1/2))
k2 = .1 * ((Symbol('x') + Symbol('h') / 2) - (Symbol('y') + (k1 / 2)) + 2)
#k3 = h * f(x + h / 2 , y + k2 / 2 )
k3 = .1 * ((Symbol('x') + Symbol('h') / 2) - (Symbol('y') + (k2 / 2)) + 2)

print(metRungeKutta(3, k1, k2, k3, 0, 0, 100, .3, .1))
