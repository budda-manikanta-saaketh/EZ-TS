#using while loop
"""n=int(input("enter a number:"))
sum=0
while(n!=0):
    rem=n%10
    sum+=rem
    n//=10
print("the sum is",sum)"""
#using string
"""n=input("enter a number:")
l=list(n)
l=[int(i) for i in l]
print(sum(l))"""
#using for loop
n=int(input("enter a number:"))
sum=0
for i in range(n):
    rem=n%10
    sum+=rem
    n//=10
print(sum)
