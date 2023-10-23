import numpy as np
data = np.array([[1,-1,4],
                 [2,1,3],
                 [1,3,-1]])
cov_matrix = np.cov(data, rowvar=False)
print(cov_matrix)
