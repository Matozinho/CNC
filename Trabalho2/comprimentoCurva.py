from sympy import *
import numpy as np
import math as m

pi = np.pi
sin = np.sin
sqrt = m.sqrt

f = lambda formula, x : eval(str(formula).replace("x", str(x)))

def IntegRegraTrap(a, b, n, form):
    h = (b - a) / n
    I = 0
    for i in range(1, n):
        x = a + (h * i)
        I += f(form, x)

    I = (h/2) * (f(form, a) + 2*I + f(form, b))
    I = eval(str(I))
    return I

def CurveSize(a, b, n, formula):
    formula_dev = formula.diff(Symbol('x'))

    L = "sqrt(1 + "+str(formula_dev)+"**2)"

    result = IntegRegraTrap(a, b, n, sympify(L))
    return result

print("a - Regra dos Trapézios")
print("Comprimento da Curva: ", CurveSize(0, pi, 20, sympify("sin(x)")))