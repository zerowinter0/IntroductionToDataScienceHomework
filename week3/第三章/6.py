score=int(input())
grade=""
if(score<60):grade="不合格"
elif(score<75):grade="合格"
elif(score<90):grade="良好"
else:grade="优秀"
print(grade)