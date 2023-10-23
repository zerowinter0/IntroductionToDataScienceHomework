import numpy as np
lst=list()
for i in range(0,100):
    lst.append(np.random.randn())
for i in lst:
    print(i,end=' ')