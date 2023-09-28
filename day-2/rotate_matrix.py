#first procedure

li=[]
n=int(input("enter no of rows:"))
k=0
for i in range(n):
    li.append(list(map(int,input().split(" "))))
c=len(li[0])
li2=[[k for i in range(c)] for i in range(n)]
for i in range(len(li)):
    for j in range(len(li[i])):
        li2[j][i]=li[i][j]
for i in range(n):
    li2[i].reverse()
for i in range(n):
    print(li2[i])


#second procedure

li=[]
li2=[]
n=int(input("enter no of rows:"))
c=int(input("enter no of coloums:"))
for i in range(n):
    li3=[]
    li4=[]
    for j in range(c):
        li3.append(int(input()))
        li4.append(0)
    li.append(li3)
    li2.append(li4)
for i in range(len(li)):
    for j in range(len(li[i])):
        li2[j][i]=li[i][j]
for i in range(3):
    li2[i].reverse()
for i in range(3):
    print(li2[i])