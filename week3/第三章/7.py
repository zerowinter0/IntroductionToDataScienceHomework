x,y=(input()).split()
x=int(x)
y=int(y)
xcopy=x
ycopy=y
l=2
dic=dict()
while(xcopy>1):
    while(xcopy%l!=0):
        l+=1
    if(dic.get(l)):
        dic[l]+=1
    else:
        dic[l]=1
    xcopy/=l
l=2
same=1
while(ycopy>1):
    while(ycopy%l!=0):
        l+=1
    if(dic.get(l) and dic[l]>0):
        dic[l]-=1
        same*=l
    ycopy/=l
print(same)