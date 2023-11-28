from sklearn.feature_extraction.text import CountVectorizer

# 输入的文本数据
text_data = ["Hello,world! this is the first sentence",
             "Hello,world! this is the second sentence",
             "Hello,world! this is the third sentence"]

# 初始化词袋模型向量化器
vectorizer = CountVectorizer()

# 将文本数据转换为词袋模型向量
X = vectorizer.fit_transform(text_data)

# 输出向量化的结果
print("\n文本向量:")
print(X.toarray())
