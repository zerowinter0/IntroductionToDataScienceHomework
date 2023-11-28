from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 加载20newsgroups数据集
data = fetch_20newsgroups()

# 获取数据集中的文本数据和标签
corpus = data.data
labels = data.target

# 初始化TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 对文本数据进行TF-IDF向量化
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, labels, test_size=0.2, random_state=42)

# 初始化朴素贝叶斯分类器
nb_classifier = MultinomialNB()

# 训练朴素贝叶斯分类器
nb_classifier.fit(X_train, y_train)

# 预测训练集和测试集
y_train_pred = nb_classifier.predict(X_train)
y_test_pred = nb_classifier.predict(X_test)

# 计算训练集和测试集的准确度
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print("训练集准确度：", train_accuracy)
print("测试集准确度：", test_accuracy)
