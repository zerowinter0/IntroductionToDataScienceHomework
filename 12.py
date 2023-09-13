x=int(input())
judge=False
if(x<0):
    x=-x
    judge=True
l=0
r=x
while abs(r-l)>1e-5:
    mid=(l+r)/2
    if (mid*mid*mid>x):
        r=mid
    else:
        l=mid
if(abs(round(l)-l)<1e-4):
    l=round(l)
if(judge):
    l=-l
print(l)