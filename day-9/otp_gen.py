st=input()
li=[int(i) for i in st]
li2=[li[i]**2 for i in range(len(li)) if i%2!=0]
st=''
for i in li2:
    if len(st)<4:
        st+=str(i)
print(st)
