import math
def cal(x,c):
    return x*x*x-c
c=int(input())
g=c
while(True):
    k=3*g*g
    res=cal(g,c)
    if(abs(res)<1e-5):
        print(g)
        break
    g=(2*g*g*g+c)/(3*g*g)
