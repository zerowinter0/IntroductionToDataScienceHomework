import numpy as np
data = np.array([[1,-1,4],
                 [2,1,3],
                 [1,3,-1]])
cov_matrix = np.cov(data, rowvar=False)
print(cov_matrix)
A=cov_matrix
num_eigenvalues = 3
max_iterations = 100
tolerance = 1e-6
eigenvalues = []
for k in range(num_eigenvalues):
    # Choose a random initial estimate for the eigenvector
    x = np.random.rand(3)
    for i in range(max_iterations):
        # Apply eigenvalue shift (mu)
        mu = 5
        v = np.dot(A, x) + mu * x
        # Normalize the estimate of the eigenvector
        x = v / np.linalg.norm(v)
        # Estimate the eigenvalue
        eigenvalue = np.dot(x, np.dot(A, x))
        if np.linalg.norm(np.dot(A, x) - eigenvalue * x) < tolerance:
            eigenvalues.append(eigenvalue)
            break
    # Deflate the matrix A by removing the found eigenvalue and eigenvector
    A = A - eigenvalue * np.outer(x, x)
print("Estimated Eigenvalues:", eigenvalues)
