from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups

# 加载20newsgroups数据集
data = fetch_20newsgroups()

# 获取数据集中的文本数据
corpus = data.data

# 初始化TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 对文本数据进行TF-IDF向量化
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# 输出第一个文本的TF-IDF向量
first_text_tfidf = tfidf_matrix[0]

print("TF-IDF向量第一个文本的结果:")
print(first_text_tfidf)
