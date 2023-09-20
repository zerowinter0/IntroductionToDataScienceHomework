import math
def cal(x,c):
    return x*x-c
c=int(input())
g=c/2
while(True):
    k=2*g
    res=cal(g,c)
    if(abs(res)<1e-5):
        print(g)
        break
    g=g-res/k

# 无论c取2或2000都能运行出正确结果