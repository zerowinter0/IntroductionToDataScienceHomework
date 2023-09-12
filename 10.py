s=input()
judge=False
for i in range(1,len(s)):
    if(s[i]==s[i-1]):
        judge=True
if(judge):
    print("Yes")
else:
    print("No")