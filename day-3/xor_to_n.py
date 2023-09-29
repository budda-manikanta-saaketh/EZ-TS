def xor(n):
    if n==0:
        return 0
    return n^xor(n-1)
l=int(input("enter lower range:"))
r=int(input("enter upper range:"))
res=xor(r)^xor(l-1)
print(res)