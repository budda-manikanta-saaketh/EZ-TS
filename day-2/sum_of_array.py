def soe(li):
    s=0
    for i in li:
        s+=i
    return s
li=list(map(int,input().split(" ")))
add=soe(li)
print(add)
