
import random
import math
res=0
for i in range(0,100000):
    x=random.uniform(2,3)
    res+=x*x+4*x*math.sin(x)
print(res/100000)