from sympy import *

# yn = y + hy' + h**2/2!y''

def temperatureVariation(functions, x0, y0, endX, h):
  xn = x0
  yn = y0

  functions[0] = lambdify(symbols('x y'), functions[0])
  functions[1] = lambdify(symbols('x y'), functions[1])

  while xn < endX:
    yn = yn + h * functions[0](xn, yn) + (h**2/2) * functions[1](xn, yn)
    xn += h
  
  return yn

y1 = -.32 * (Symbol('y') - 28)
y2 = 0.1024 * Symbol('y') - 2.8672

equations=[]
equations.append(y1)
equations.append(y2)

print(temperatureVariation(equations, 0, 90, 5, .5))
