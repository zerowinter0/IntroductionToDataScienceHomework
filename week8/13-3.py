# 导入所需的库
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化KNN分类器
knn = KNeighborsClassifier(n_neighbors=3)  # 这里选择K=3，你可以根据需要调整

# 训练模型
knn.fit(X_train, y_train)

# 预测训练集和测试集
y_train_pred = knn.predict(X_train)
y_test_pred = knn.predict(X_test)

# 计算训练集和测试集的准确度
train_accuracy = metrics.accuracy_score(y_train, y_train_pred)
test_accuracy = metrics.accuracy_score(y_test, y_test_pred)

# 输出结果
print("训练集准确度: {:.5f}%".format(train_accuracy * 100))
print("测试集准确度: {:.5f}%".format(test_accuracy * 100))
