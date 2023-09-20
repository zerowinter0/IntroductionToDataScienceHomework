# 第一种方法：蒙特卡洛
import random
import time
import math
cnt=0
time_cnt=time.perf_counter()
for i in range(1,10000000):
    x=random.random()
    y=random.random()
    if(x*x+y*y<=1):
        cnt+=1
time_cnt=time.perf_counter()-time_cnt
print(4*cnt/1e+7,'\n耗时:','%.8f'%time_cnt,'秒')

# 第二种方法：已知sinx在Π/2~3*Π/2的范围内的数最近的零点都是Π，所以可以用牛顿法求解

def cal(g):
    if(abs(math.sin(g))<1e-10):
        return True
    else:return False
g=2
time_cnt=time.perf_counter()
while(not cal(g)):
    g=(-math.sin(g)+math.cos(g)*g)/math.cos(g)
time_cnt=time.perf_counter()-time_cnt
print(g,'\n耗时:','%.8f'%time_cnt,'秒')

# 第三种方法：级数求和
ans=0
flag=True
time_cnt=time.perf_counter()
for i in range(1,10000000,2):
    if(flag):
        ans+=1/i
    else:ans-=1/i
    flag=not flag
time_cnt=time.perf_counter()-time_cnt
print(ans*4,'\n耗时:','%.8f'%time_cnt,'秒')