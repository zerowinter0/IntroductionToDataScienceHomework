import math
def common_chech_prime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i==0):
            return False
    return True
def qpow(a,n,mod):
    ans=1
    while(n):
        if(n&1):
            ans*=a
            ans%=mod
        a*=a
        a%=mod
        n>>=1
    return ans

def miller_rabin(a):
    u=a-1
    t=0
    while(u%2==0):
        u//=2
        t+=1
    check_list={2,325,9375,28178,450775,9780504,1795265022}
    for i in check_list:
        v=qpow(i,u,a)
        if(v==1 or v==a-1 or v==0):continue
        for j in range(1,t+1):
            v=(v*v)%a
            if(v==a-1 and j!=t):
                v=1
                break
            if(v==1):return False
        if(v!=1):
            return False
    return True

x=int(input())
checkresult=False
if(x<1e+14):
    checkresult=common_chech_prime(x)
else:
    checkresult=miller_rabin(x)
if(checkresult):
    print("Yes")
else:print("No")