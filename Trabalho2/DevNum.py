from sympy import *
import numpy as np
import math as m

e = m.e


def f(x):
    return m.e**(x+2) * (x**(3/2)-x**(1/2))

def f_sd_dev(x):
    return e**(x+2) * ((4*x**3 + 8*x**2 - x + 1)/(4*x**(3/2)))

def f_rd_dev(x):
    return e**(x+2) * ((8*x**4 + 28*x**3 + 6*x**2 + 3*x -3)) / (8*x**(5/2))

def quest_a(list_h, list_x0):
    for x0 in list_x0:
        for h in list_h:
            res = ((f(x0 + h) - f(x0)) / (h))
            print(f"h: {h}\nf\'({x0}): {res}")

            erro = err(h, x0, eq="a")
            print(f"erro: {erro}\n\n")

def quest_b(list_h, list_x0):
    for x0 in list_x0:
        for h in list_h:
            res = (-1*f(x0 - h) + f(x0 + h)) / (2*h)
            print(f"h: {h}\nf\'({x0}): {res}")

            erro = err(h, x0, eq="b")
            print(f"erro: {erro}\n\n")

def quest_c(list_h, list_x0):
    for x0 in list_x0:
        for h in list_h:
            res = (-3*f(x0) + 4*f(x0+h) - f(x0+2*h)) / (2*h)
            print(f"h: {h}\nf\'({x0}): {res}")

            erro = err(h, x0, eq="c")
            print(f"erro: {erro}\n\n")

def err(h, x, eq):
    if eq == "a":
        return (h / 2) * f_sd_dev(x)
    elif eq == "b":
        return (h**2 / 6) * f_rd_dev(x)
    elif eq == "c":
        return (h**2 / 3) * f_rd_dev(x)

h = input("h: ")
x = input("x: ")

h = float(h) if isDigit(h) else sympify(h)
x = float(x) if isDigit(x) else sympify(x)

quest_a([.01], [.4])
quest_b([.01], [.4])
quest_c([.01], [.4])
