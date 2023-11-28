from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split

data = fetch_20newsgroups()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
model = make_pipeline(CountVectorizer(), LogisticRegression(max_iter=10000))

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("score =", model.score(X_test, y_test))
