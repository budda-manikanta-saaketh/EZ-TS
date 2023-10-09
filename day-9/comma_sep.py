#input:a string of comma seperated number are given such that the numbers 4 and 7 are already available in the list
#Assummption:7 always comes after 4 in the given string
#number1=Add all number which do not lie b/w 4 and 7(excluding 4 and 7) in the given input
#number2= numbers formed by concating all number between 4 and 7 including 4 n 7
#output=number1+number2
#input=2,5,1,4,3,2,7,8

li=list(map(int,input().split(",")))
st=''
s=0
p4=li.index(4)
p7=li.index(7)
for i in li[:p4]+li[p7+1:]:
    s+=i
for i in range(p4,p7+1):
    st+=str(li[i]) 
print(s,st)     
print(s+int(st))