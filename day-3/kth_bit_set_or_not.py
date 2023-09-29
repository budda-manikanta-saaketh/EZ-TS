# using bitwise
n=int(input("enter the number:"))
p=int(input("enter the position of bit:"))
res=n&(1<<(p-1))
if res==0:
    print("not set")
else:
    print("set")
    
#not using bitwise
n=int(input("enter the number:"))
p=int(input("enter the position of bit:"))
n=str(bin(n))[::-1]
if (n[p-1]=="1"):
    print("set")
else:
    print("not set")
