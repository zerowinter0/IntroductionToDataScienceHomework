lst=list({1,2,3,4,5})
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end=" ")
print("")
i=len(lst)
while (i>0):
    i-=1
    print(lst[i],end=" ")