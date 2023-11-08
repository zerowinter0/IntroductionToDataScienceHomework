import numpy as np
from sklearn.datasets import load_iris
from scipy.spatial import distance

# 加载鸢尾花数据集
data = load_iris()
X = data.data
y = data.target

# 计算不同标签类别的中心点
unique_labels = np.unique(y)
centroids = []

for label in unique_labels:
    label_data = X[y == label]
    centroid = np.mean(label_data, axis=0)
    centroids.append(centroid)

# 打印中心点
for label, centroid in zip(unique_labels, centroids):
    print(f"中心点 ({label}): {centroid}")

# 计算数据点到中心点的欧氏距离
distances = []

for i in range(len(X)):
    label = y[i]
    centroid = centroids[label]
    euclidean_dist = distance.euclidean(X[i], centroid)
    distances.append(euclidean_dist)

# 打印数据点到中心点的欧氏距离
for i, dist in enumerate(distances):
    label = y[i]
    print(f"数据点 {i} 到中心点 ({label}) 的欧氏距离: {dist:.2f}")
