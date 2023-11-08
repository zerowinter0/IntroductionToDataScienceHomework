from sklearn.datasets import load_iris
iris_dataset=load_iris()
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0,test_size=0.3)
print("X_train shape: {}".format(X_train.shape)) 
print("Y_train shape: {}".format(Y_train.shape)) 
print("X_test shape: {}".format(X_test.shape))
print("Y_test shape: {}".format(Y_test.shape))