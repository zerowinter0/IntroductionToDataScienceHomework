import random
n=int(input())
lst=list()
for i in range(0,n):
    lst.append(int(random.random()*100))
for i in range(0,n):
    target=lst[i]
    for j in range(i-1,-1,-1):
        if(lst[j]>target):
            lst[j+1]=lst[j]
        else:
            lst[j+1]=target
            break
    if(lst[0]>target):
        lst[0]=target
for i in lst:
    print(i,end=' ')