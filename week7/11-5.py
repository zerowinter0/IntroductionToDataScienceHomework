import numpy as np
from sklearn import datasets
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt
iris=datasets.load_iris()
x=iris['data']
y=iris['target']
np.bincount(y)
iy=y==2
y[iy]=0
np.bincount(y)
y=y.reshape(150,1)
w=np.zeros((4,1))
b=np.zeros((1,1))
n=0
j_last=0
list_j=[]
list_auc=[]
list_logll=[]
alpha=0.19
stop_times=80000
diff_j=0.00000000000000001
while n<stop_times:
    z=np.dot(x,w)+b
    a=(1/(1+np.exp(-z)))
    dz=a-y
    dw=np.dot(x.T,dz)/float(x.shape[0])
    db=np.sum(dz)/float(x.shape[0])
    w=w-alpha*dw
    b=b-alpha*db
    ll=np.cumprod(a[y==1])[-1]*np.cumprod(1-a[y==0])[-1]
    j=np.mean(-(y*np.log(a)+(1-y)*np.log(1-a)))
    if np.abs(j-j_last)<diff_j:
        break
    j_last=j
    fpr,tpr,thresholds=roc_curve(y,a)
    list_auc.append(auc(fpr,tpr))
    list_logll.append(np.log(ll))
    list_j.append(j)
    n+=1
    print(n,j,np.log(ll))