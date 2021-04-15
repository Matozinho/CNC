from sympy import *
import numpy as np
import math as m
# import matplotlib.pyplot as plt

pi = np.pi
sin = np.sin
e = np.e
sqrt = m.sqrt

def isDigit(d):
    try:
        float(d)
    except ValueError:
        return False
    return True

f = lambda formula, x : eval(str(formula).replace("x", str(x)))


# def f(formula, x): return eval(str(formula).replace("x", str(x)))

def CurveLength(a, b, n, method, formula):
    """
    Calcula o comprimento de uma curva
    utilizando

    .. math::
        \int_a^b \sqrt{1 + f'(x)^2}dx
    """
    formula_dev = formula.diff(Symbol('x'))

    # type = int(input("Non-param Curve(0) Param Curve(1)"))

    L = "sqrt(1 + "+str(formula_dev)+"**2)"

    result = IntegRegraTrap(a, b, n, sympify(L)) if not method else IntegSimpsons(a, b, n, sympify(L))
    return result

def IntegRegraTrap(a, b, n, form):
    h = eval(str((b - a) / n))
    I = 0
    for i in range(1, n):
        x = eval(str(a + (h * i)))
        I += f(form, x)

    I = (h/2) * (f(form, a) + 2*I + f(form, b))
    I = eval(str(I))
    return I


def IntegSimpsons(a, b, n, form):
    h = eval(str((b - a) / n))
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


# TODO: Allow A & B to be symbols
a = input("a: ")
b = input("b: ")

# Convert to float or symbols
a = float(a) if isDigit(a) else sympify(a)
b = float(b) if isDigit(b) else sympify(b)
# 

n = int(input("n: "))
AreaOrCurve = int(input("Choose Area(0) Curve(1): "))
TpOrSimp = int(input("TrapsRule(0) or Simpson(1): "))

formula = sympify(input("formula: "))

result = CurveLength(a, b, n, TpOrSimp, formula) if AreaOrCurve else IntegRegraTrap(a, b, n, formula)
print(f"Curve length {result}" if AreaOrCurve else f"Area under the curve: {result}")
