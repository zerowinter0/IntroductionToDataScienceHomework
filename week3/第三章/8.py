import random
import time
import sys
sys.setrecursionlimit(1000000)
def select_sort(lst):
    siz=len(lst)
    for i in range(0,siz):
        target=i
        for j in range(i+1,siz):
            if(lst[target]>lst[j]):
                target=j
        tmp=lst[i]
        lst[i]=lst[target]
        lst[target]=tmp
def quick_sort(lst,begin,end):
    if(end<=begin):
        return
    i=begin
    j=end
    x=lst[(i+j)>>1]
    while(i<j):
        i+=1
        while(lst[i]<x and i<j):
            i+=1
        j-=1
        while(lst[j]>x and i<j):
            j-=1
        
        if(i<j):
            tmp=lst[i]
            lst[i]=lst[j]
            lst[j]=tmp
    quick_sort(lst,begin,j-1)
    quick_sort(lst,j+1,end)
l=1
ListCnt=int(input())
while ListCnt>0 :
    ListCnt-=1
    len1=int(random.random()*1000)+500+l
    lst=list()
    for i in range(0,len1):
        lst.append(int(random.random()*5000))
    l=len1
    print("length of array:",len1)
    time_cnt=time.perf_counter()
    lst1=lst.copy()
    lst2=lst.copy()
    select_sort(lst1)
    time_cnt=time.perf_counter()-time_cnt
    print("cost time of select sort:",time_cnt)
    time_cnt=time.perf_counter()
    quick_sort(lst2,0,len1-1)
    time_cnt=time.perf_counter()-time_cnt
    print("cost time of quick sort:",time_cnt)

