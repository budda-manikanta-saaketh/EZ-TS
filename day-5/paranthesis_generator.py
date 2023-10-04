#write python program to generate all the possible balanced paranthesis from this list of parathesis para=["(",")","{","}","[","]"] each element should be only used once
para=["(",")","{","}","[","]"]
balanced=[]
str=""
for i in range(len(para)-1,-1,-1):
    str=" "
    for j in range(len(para)):
        if i!=j:
            if para[i]=='(':
                if para[j]==')':
                    str+=para[i]+para[j]
            if para[i]=='{':
                if para[j]=='}':
                    str+=para[i]+para[j]
            if para[i]=='[':
                if para[j]==']':
                    str+=para[i]+para[j]
            balanced.append(str)
print(balanced)





