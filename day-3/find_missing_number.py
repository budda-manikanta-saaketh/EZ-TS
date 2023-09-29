li=list(map(int,input().split(" ")))
li2=[]
n=max(li)
f=0
li=[i for i in range(len(li)) if i>=0]
for i in range(n):
    if li.count(i)==0:
        print(i)
if f==0:
    print(n+1)
