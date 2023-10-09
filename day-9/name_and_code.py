#take the input form the user in the given format(constiste of name and code),find the max digits from the code which is less or equal to the length of strings and put that place char in final string, if there is no any digit
#input=
#abhisek:438448, mayur:3749,friend:3949, yeah:7878
#output:kuex

def sort(num,name):
    li=[int(i) for i in num]
    li.sort(reverse=True)
    for i in li:
        if i<=len(name):
            return i
    return -1
n=int(input("enter no of pairs:"))
d={}
for i in range(n):
    name=input("enter name:")
    code=input("enter code:")
    d[name]=code
for i in d.keys():
    f=sort(d[i],i)
    if f==-1:
        print("x",end="")
    else:
        print(i[f-1],end="")

