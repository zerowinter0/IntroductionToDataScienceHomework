import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# 加载鸢尾花数据集
iris = load_iris()
data = iris.data

# 创建K-means模型
kmeans = KMeans(n_clusters=3)  # 选择聚类数，这里选择3个类别

# 拟合模型并获得簇分配结果
kmeans.fit(data)
labels = kmeans.labels_

# 获取簇中心
cluster_centers = kmeans.cluster_centers_

# 可视化聚类结果
plt.figure(figsize=(8, 6))

# 绘制数据点
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')

# 绘制簇中心
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200, marker='X', label='Cluster Centers')

plt.title('K-means Clustering of Iris Dataset')
plt.legend()
plt.show()
