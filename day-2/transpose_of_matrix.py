#transpose of a matrix.
li=[]
li2=[[0,0,0] for i in range(3)]
n=int(input("enter no of rows:"))
for i in range(n):
    li.append(list(map(int,input().split(" "))))
for i in range(len(li)):
    for j in range(len(li[i])):
        li2[j][i]=li[i][j]
for i in range(3):
    print(li2[i])

