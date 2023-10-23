import numpy as np
import matplotlib.pyplot as plt
lst=list()
for i in range(0,100):
    lst.append(np.random.randn())
import seaborn as sns
sns.kdeplot(lst, shade=True, color='r')
plt.show()
