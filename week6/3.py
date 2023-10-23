import numpy as np
matrix = np.array([[2, 1],
                  [4,  5]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(eigenvalues)
print(eigenvectors)
