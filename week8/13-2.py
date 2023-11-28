import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd

# 加载尾花数据集
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.2)
print(X_train.size,X_test.size)