import re
check="^"+"\\d{6}"+"(18|19|([2]\\d))\\d{2}"+"((0[1-9])|(10|11|12))"+"(([0-2][1-9])|10|20|30|31)"+"\\d{3}"+"[0-9Xx]"+"$"
s=input()
if(re.match(check,s)):
    print("Yes")
else:print("No")
