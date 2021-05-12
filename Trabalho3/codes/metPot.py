import numpy as np

A = np.matrix([
  [1, 2, -2, 5],
  [3, 12, 3, 4],
  [3, 13, 0, 7],
  [2, 11, 2, 12]
])

V0 = np.matrix([[1, 1, 1, 1]]).transpose()

def metPot(A, V, eps, Npassos):
  err = float("inf")
  k = 0
  lmbd = np.zeros(2)
  
  while err > eps and k < Npassos:
    U = A * V
    if k >= 1:
      lmbd[1] = ((U.ravel()*V).item(0)) / ((V.ravel()*V).item(0))
    if k >= 2:
      err = np.abs(lmbd[1] - lmbd[0]) / np.abs(lmbd[1])
    
    V = W = U / np.abs(U).max()
    #V = W
    lmbd[0] = lmbd[1]
    k += 1
  
  return (W, U, lmbd[1])

resp = metPot(A, V0, .0001, 5)
print("Maior autovalor: ", resp[2])
print("Autovetor normalizado: ")
print(resp[0])
print("AutoVetor não normalizado: ")
print(resp[1])
