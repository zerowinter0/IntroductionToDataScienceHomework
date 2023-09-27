a=list()
b=list()

n=int(input())
a.append(0)
inputlist=input().split(' ')
for i in inputlist:
    val=int(i)
    a.append(val)
pre=list()
suf=list()
now=1
pre.append(1)
for i in range(1,n+1):
    now*=a[i]
    pre.append(now)
now=1
suf=[0]*(n+1)
suf[n]=1
for i in range(n,0,-1):
    now*=a[i]
    suf[i-1]=now
b=[None]*(n)
for i in range(0,n):
    b[i]=pre[i]*suf[i+1]
for i in b:
    print(i,end=' ')