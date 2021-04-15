class Data:
    """
    Awesome data
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


def interpolate(f: list, xi: int, n: int) -> float:
    result = 0.0

    for i in range(n):
        term = f[i].y

        for j in range(n):
            if j != i:
                term *= (xi - f[j].x) / (f[i].x - f[j].x)

        result += term

    return result


f = [
    Data(1940, 132165), 
    Data(1950, 151325), 
    Data(1960, 179323), 
    Data(1970, 203302), 
    Data(1980, 226542), 
    Data(1990, 249533)]

interpolation = interpolate(f=f, xi=1930, n=len(f) - 1)
print(f"P{len(f)-1}(1930) = {interpolation}")
interpolation = interpolate(f=f, xi=1985, n=len(f) - 1)
print(f"P{len(f)-1}(1985) = {interpolation}")
