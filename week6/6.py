import numpy as np
data = np.array([[1,-1,4],
                 [2,1,3],
                 [1,3,-1]])
A = np.cov(data, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(A)
for i in range(len(eigenvalues)):
    eigenvalue = eigenvalues[i]
    eigenvector = eigenvectors[:, i]
    print(eigenvalue)
    print(eigenvector)
    print("\n")