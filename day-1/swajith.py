"""Swajith is having 1 lakh in his bank Account; rate of interest is 12% per annum. In the 5th month Swajith is withdrawing 25000 rupees in order to buy gift for his loved one. In the 9th month 10000 is being deposited in his account by his second loved one. End of the financial year how much Swajith is having in his account ."""
#user input
amount = input("enter the bank balance:")
ch=0
c=0
def deposit(amount):
    a = int(input("Enter the amount to be Deposited: "))
    amount+=a
    return amount
def withdraw(amount):
    b =int (input ("Enter the Amount To Be Withdrawn :"))
    amount-=b
    return amount
while True:
    cho=int(input("continue or no:"))
    if(cho==0):
        break
    else:
        m = int(input("enter the month in which you will do any operation:"))
        m = m-c
        amount = int(amount)
        interest = amount*0.01
        amount+=interest*(m)
        c=c+m
        ch=int(input("1.depost\n2.withdraw\n"))
        if ch==1:
            amount=deposit(amount)
        if ch==2:
            amount=withdraw(amount)
c=12-c+1
amount=int(amount)
interest=amount*0.01
amount+=interest*(c)
print(amount)