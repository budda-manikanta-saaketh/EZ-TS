#reverse a given string and keeping its special character at the same place
#input:srin#vas
#output:savn#irs
st=input()
li=[i for i in st]
for i in range(len(li)):
    if li[i].isalpha()==False and li[i].isdigit()==False:
        p=i
        sc=li[i]
        li.remove(li[i])
        break
li.reverse()
li.insert(p,sc)
print(li)
st=''.join(li)
print(st)
