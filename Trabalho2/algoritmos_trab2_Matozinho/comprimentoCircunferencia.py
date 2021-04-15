from sympy import *
import numpy as np
import math as m

pi = np.pi
sin = np.sin
sqrt = m.sqrt

f = lambda formula, x : eval(str(formula).replace("x", str(x)))

def IntegSimpsons(a, b, n, form):
    h = 0.1
    I = Int_even = Int_odd = 0

    for i in range(n):
        x = eval(str(a + (h * i)))
        if i%2 == 0:
            Int_even += f(form, x)
        else:
            Int_odd += f(form, x)

    I += (h/3) * (f(form, a) + 4*Int_odd + 2*Int_even + f(form, b))
    I = eval(str(I))
    return I

def circleSize(a, b, gt, ht):
    gt_dev = gt.diff(Symbol('x'))
    gt_dev = str(gt_dev).replace('x', str(a))
    ht_dev = ht.diff(Symbol('x'))
    ht_dev = str(ht_dev).replace('x', str(b))

    L = "sqrt("+str(gt_dev)+"**2 + "+str(ht_dev)+"**2)"

    result = IntegSimpsons(a, b, int(20*pi), sympify(L))
    return result

diametro = circleSize(0, (2 * pi), sympify("4*cos(x)"), sympify("4*sin(x)"))
print("Comprimento do Círculo: ", diametro * 2)