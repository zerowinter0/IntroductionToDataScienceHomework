## 0为狼，1为羊，2为菜
def checkexist(x,num):
    return (x//(1<<num))%2==1
def checklegal(x):
    if(checkexist(x,0) and checkexist(x,1)):
        return False
    if(checkexist(x,1) and checkexist(x,2)):
        return False
    return True
ansList=list()
dic=dict()
dic[0]='狼'
dic[1]='羊'
dic[2]='菜'
def dfs(initplace,finalplace,boatplace,st1,lst):
    if initplace*100+finalplace*10+boatplace in st1:##本方案必定每一步都有意义，不会重复经历本方案经历过的完全相同的状态
        return
    if((boatplace==2 and not checklegal(initplace)) or (boatplace ==1 and not checklegal(finalplace))):
        return
    if(finalplace==7 and boatplace==2):
        ansList.append(lst)
        return
    st=st1.copy()
    st.add(initplace*100+finalplace*10+boatplace)
    if(boatplace==1):
        for x in range(0,3):
            if(not checkexist(initplace,x)):
                continue
            lst2=lst.copy()
            lst2.append(dic[x]+',人去对岸')
            dfs(initplace-(1<<x),finalplace+(1<<x),2,st,lst2)
        lst2=lst.copy()
        lst2.append('人去对岸')
        dfs(initplace,finalplace,2,st,lst2)
    if(boatplace==2):
        for x in range(0,3):
            if(not checkexist(finalplace,x)):
                continue
            lst2=lst.copy()
            lst2.append(dic[x]+',人回来')
            dfs(initplace+(1<<x),finalplace-(1<<x),1,st,lst2)
        lst2=lst.copy()
        lst2.append('人回来')
        dfs(initplace,finalplace,1,st,lst2)
lst=list()
st=set()
dfs(7,0,1,st,lst)
cnt=1
for i in ansList:
    print("第",cnt,"种方案:")
    for j in i:
        print(j)
    cnt+=1
    print()
