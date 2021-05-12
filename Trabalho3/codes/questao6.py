from sympy import *

def metHeun(y, x0, y0, endX, h):
  xn = x0
  yn = y0

  while xn < endX:
    yn = yn + ((h/2) * (y(yn) + y(yn + (h * y(yn)))) )
    xn += h
  
  return yn

V0 = 2000
a = 4  #ml/L de álcool no barril
b = 6  #ml/L de álcool da cerveja inserida
e = 20 #Entrada de cerveja em L/min
s = 20 #Vazão de cerveja em L/min

y = lambdify(symbols('y'), b*e - (s / (V0 + Symbol('t') * (e - s))) * Symbol('y')) 

print("Método de Heun: ", metHeun(y, 0, 4*2000, 60, .1) / 2000)
