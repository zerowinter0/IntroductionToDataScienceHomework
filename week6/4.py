import numpy as np

def power_iteration(matrix, num_iterations):
    n = matrix.shape[0]
    x = np.random.rand(n)  # 随机初始化一个向量

    for _ in range(num_iterations):
        y = np.dot(matrix, x)
        x = y / np.linalg.norm(y)  # 归一化向量

    eigenvalue = np.dot(np.dot(x, matrix), x) / np.dot(x, x)
    return eigenvalue
A = np.array([[2, 1],
              [4, 5]])
num_iterations = 100
eigenvalue = power_iteration(A, num_iterations)
print(eigenvalue)
