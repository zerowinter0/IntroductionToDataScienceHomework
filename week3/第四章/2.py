import time
time_cnt=time.perf_counter()
##do something here
now=1
for i in range(0, 10000):
    now+=i

##
time_cnt=time.perf_counter()-time_cnt
print(time_cnt)