def balanced(s):
    stack=[]
    for i in s:
        if i=="(" or i=="{" or i=="[":
            stack.append(i)
        elif i==")" or i=="}" or i=="]":
            if len(stack)==0:
                return False
            elif i==")" and stack[-1]=="(":
                stack.pop()
            elif i=="}" and stack[-1]=="{":
                stack.pop()
            elif i=="]" and stack[-1]=="[":
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False
def gen_par(n):
    res=[]
    def par(n,l,r,s):
        if l<n:
            par(n,l+1,r,s+"(")
        if r<l:
            par(n,l,r+1,s+")")
        if l<n:
            par(n,l+1,r,s+"{")
        if r<l:
            par(n,l,r+1,s+"}")
        if l<n:
            par(n,l+1,r,s+"[")
        if r<l:
            par(n,l,r+1,s+"]")
        if l==n and r==n:
            if balanced(s):
                res.append(s)
    par(n,0,0,"")
    return res

n=int(input("enter no of pairs you want:"))
li=gen_par(n)
print(li)
