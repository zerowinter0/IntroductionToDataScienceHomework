## (1):将2001全部拆分成3再相乘
## (2):可证当我们把5以上的数拆分成一个数列相乘时，若数列中含有x，则表示x自身无法再拆成更优的数列相乘。接下来证明x必定小于等于四：
##  当x大于4时，x拆成(x-2)*2可得2*x-4,因为x>4,所以易证2*x-4>x，所以x大于4时总可以将其拆成更优的数列相乘。接下来证明当x可拆成3个及以上的2时会优先拆成3
##  6=2+2+2=3+3，2*2*2=8<3*3=9，所以每3个2可以转化为2个3。经过优化我们可以得到：将x拆分成若干个2和3最优，并且2的数量不超过2
## 易证此时方案数有且只有一个，即先将x整除3得到3的数量，若余数为1则舍弃一个3以得到4，转化成2个2；若余数为2则保留这个2，若余数为0则不乘2

x=int(input(""))
cnt3=x//3
cnt2=0
res=x%3
if(x==1):
    print(1)
    exit()
if(res==1):
    cnt3-=1
    cnt2+=2
if(res==2):
    cnt2+=1
while(cnt3):
    print("3",end="")
    cnt3-=1
    if(cnt3>0 or cnt2>0):
        print("*",end="")
while(cnt2):
    print("2",end="")
    cnt2-=1
    if(cnt2>0):
        print("*",end="")