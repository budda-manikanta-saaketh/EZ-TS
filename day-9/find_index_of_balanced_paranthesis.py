#balanced brackets problem
#input:()()
#output:0
#input:((())
#output:6
#input:{(){}[]}(}
#output:10
#input:{[()}
#output:5

#s="((())"
#s='()()'
#s="{(){}[]}(}"
#s="{[()}"
s=input()
l=[]
c=0
f=0
for i in range(len(s)):
    if(s[i]=='(' or s[i]=='[' or s[i]=='{'):
        l.append(s[i])
        c+=1
    elif((s[i]==')' and l[-1]=='(') or (s[i]==']' and l[-1]=='[') or (s[i]=='}' and l[-1]=='{')):
        l.pop()
        c+=1
    else:
        print(c+1)
        f=1
        break

if(f==0):
    if(c%2==0):
        print(0)
    else:
        print(c+1)