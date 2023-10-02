#create a class that consists of  three varaibles with initialization and you have to take two methods and first method is
#two argumented function first one string type of argument and second one is int type if argument and inside of the method 
#string reverse have to print and square root interger argument value . the second method is displayResults one statement
#should print length of string and another statement should print modulus division of two integer variables.
class problem_1:
    def __init__(self,string,num,num2):
        self.string=string
        self.integer=num
        self.integer2=num2
    def stringReverse(self,string,num):
        print("Reverse of a string:",string[::-1])
        print(f"Square root of {num}:",num**0.5)
    def displayResults(self):
        print("Length of string:",len(self.string))
        print(f"Modular division of {self.integer} and {self.integer2}:",self.integer%self.integer2)
string=input("enter a string:")
num=int(input("enter a number:"))
num2=int(input("enter a number 2:"))
obj=problem_1(string,num,num2)
obj.stringReverse(string,num)
obj.displayResults()