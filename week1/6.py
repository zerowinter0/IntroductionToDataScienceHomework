w,x,y,z=input().split(' ')
st=list()
st.append(int(w))
st.append(int(x))
st.append(int(y))
st.append(int(z))
st.sort(reverse=True)
for i in st:
    print(i,end=" ")