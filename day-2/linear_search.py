#linear search of elements
def find(li,num):
    f=0
    for i in li:
        if num==i:
            print ("number found")
            f=1
            break
    return f
li=list(map(int,input("enter the list elements:").split(" ")))
num=int(input("enter the number to search:"))
f=find(li,num)
if f==0:
    print(f"the element {num} is not present ")
        