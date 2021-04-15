class Data:
  def __init__(self, x, y):
    self.x = x
    self.y = y

#points => pontos tabelados, x => valor de interesse, n => tamanho da lista
def laGrangeInterpol(points, x, n):
  L = []
  for k in range(n):
    #Recebem elemento neutro da multiplicação
    P1 = 1 
    P2 = 1
    for i in range(n):
      if i != k:
        P1 *= (x - points[i].x)
        P2 *= (points[k].x - points[i].x)

    L.append(P1 / P2)
  
  #Elemento neutro da adição
  Soma = 0
  for k in range(n):
    Soma += points[k].y * L[k]
  
  return Soma

f = [Data(1940, 132165), Data(1950, 151326), Data(1960, 179323), Data(1970, 203302), Data(1980, 226542), Data(1990, 249633)]
print("P(1930) = ", laGrangeInterpol(f, 1930, len(f)))
print("P(1985) = ", laGrangeInterpol(f, 1985, len(f)))