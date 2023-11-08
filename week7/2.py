import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
x=np.linspace(0,10,30)
y=9*x+8+np.random.randn()
reg=linear_model.LinearRegression()
x=x.reshape(-1,1)
reg.fit(x,y)
print(reg.coef_)