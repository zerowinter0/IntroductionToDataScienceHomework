from snownlp import SnowNLP
from snownlp import sentiment
#sentiment.train('C:/Users/Alex/Desktop/数据科学导论作业/FinalProject/sample.negative.txt', 'C:/Users/Alex/Desktop/数据科学导论作业/FinalProject/sample.postive.txt')
#sentiment.save('sentiment.marshal')
comment=input()
sentiment.load('sentiment.marshal')
print(SnowNLP(comment).sentiments)