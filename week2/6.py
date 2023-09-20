import math
def cal(x,c):
    return x*x-c
c=int(input())
g=c
while(True):
    k=2*g
    res=cal(g,c)
    if(abs(res)<1e-5):
        print(g)
        break
    g=g-res/k

# g初始值其实只要取的是正数最后答案都是正确的，所以c/2,c,c/4都可