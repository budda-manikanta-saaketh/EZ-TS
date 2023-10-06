def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
li=list(map(int,input().split(" ")))
x=int(input())
x=linear_search(li,x)
if x!=-1:
    print("element is present in the list")
else:
    print("element is not present")

