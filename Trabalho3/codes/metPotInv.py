import numpy as np

A = np.matrix([
  [0, 3, -4], #[1, 3]
  [4, -3, 6], #[2, 6]
  [0, 2, -6] #[7, 11]
])

V0 = np.matrix([[1, 0, 0]]).transpose()

def metPotInv(A, V, q, eps, Npassos):
  mi = []
  lmbd = np.zeros(2)
  I = np.identity(A.shape[0])
  err = float("inf")
  k = 0

  B = (A - (q * I))**-1
  
  while err > eps and k < Npassos:
    U = B * V
    
    if k >= 1:
      lmbd[1] = ((U.ravel()*V).item(0)) / ((V.ravel()*V).item(0))
      mi.append(lmbd[1])
    
    if k >= 2 :
      err = np.abs(lmbd[1] - lmbd[0]) / np.abs(lmbd[1])
  
    V = W = U / np.abs(U).max()
    lmbd[0] = lmbd[1]
    k += 1

  print(mi)
  return 1.0 / mi[0] + q
  

print(metPotInv(A, V0, 4, .001, 5))