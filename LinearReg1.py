import numpy as np
from scipy import linalg
#pts are (0,1),(1,2),(2,3),(3,4),(4,3)
A = [[0 ,1],[1 ,1], [2 ,1], [3 ,1], [4 ,1]]
A = np.array(A)
Y = [1 , 2, 3, 4,3]
Y = np.array(Y)
AtA = np.matmul(A.T, A)
# AtA = A.T @ A
AtAi = linalg.inv(AtA)
# FA = AtAi @ A.T
FA = np.matmul(AtAi, A.T)
# w = FA @ Y
w = np.matmul(FA, Y)
print(w)