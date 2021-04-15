import numpy as np

e = np.e

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

print("Área y = x²/2 = ", IntegRegraTrap(2, 6, 20, "x**2 / 2"))
print("Área y = e^-x = ", IntegRegraTrap(2, 6, 20, "e**(-x)"))