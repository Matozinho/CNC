import sympy

def laGrangePolGenerator(list_x, list_y):
    x = sympy.symbols("x")
    len_list = len(list_x)

    y = 0
    for i in range(len_list):
        t = 1

        for j in range(len_list):
            if j != i:
                t = t * ((x - list_x[j]) / (list_x[i] - list_x[j]))
        y += t * list_y[i]

    return y

print("Polinômio interpolador:")
print(laGrangePolGenerator([-1, 0, 2], [5, -1, 11]))