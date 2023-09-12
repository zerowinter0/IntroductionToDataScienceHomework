x=int(input())
l=1
r=x
while l<r:
    mid=int((l+r)/2)
    if (mid*mid*mid>x):
        r=mid
    else:
        l=mid+1
while(l*l*l>x):
    l-=1
print(l)