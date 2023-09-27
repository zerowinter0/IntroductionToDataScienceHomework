import random
n=int(input())
lst=list()
for i in range(0,n):
    lst.append(int(random.random()*100))
gap=n
while(gap):
    for i in range(0,gap):
        for j in range(i+gap,n,gap):
            target=lst[j]
            for k in range(j-gap,-1,-gap):
                if(lst[k]<=target):
                    lst[k+gap]=target
                    break
                else:lst[k+gap]=lst[k]
            if(lst[i]>target):lst[i]=target
    gap//=2
for i in lst:
    print(i,end=' ')