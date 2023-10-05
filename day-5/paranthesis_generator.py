def gen_par(n):
    res=[]
    def par(n,l,r,s):
        if l<n:
            par(n,l+1,r,s+"(")
        if r<l:
            par(n,l,r+1,s+")")
        if l==n and r==n:
            res.append(s)
    par(n,0,0,"")
    return res

n=int(input("enter no of pairs you want:"))
li=gen_par(n)
print(li)
