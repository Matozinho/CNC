from sympy import *
import numpy as np
import math as m

pi = np.pi
sin = np.sin
sqrt = m.sqrt

f = lambda formula, x : eval(str(formula).replace("x", str(x)))

def IntegSimpsons(a, b, n, form):
    h = (b - a) / n
    I = Int_even = Int_odd = 0

    for i in range(0, n):
        x = eval(str(a + (h * i)))
        if i%2 == 0:
            Int_even += f(form, x)
        else:
            Int_odd += f(form, x)

    I += (h/3) * (f(form, a) + 4*Int_odd + 2*Int_even + f(form, b))
    I = eval(str(I))
    return I

def CurveSize(a, b, n, formula):
    formula_dev = formula.diff(Symbol('x'))

    L = "sqrt(1 + "+str(formula_dev)+"**2)"

    result = IntegSimpsons(a, b, n, sympify(L))
    return result

print("b - Método de Simpson")
print("Comprimento da Curva: ", CurveSize(0, pi, 20, sympify("sin(x)")))