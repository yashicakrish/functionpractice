# Name:Yashica Krishnaperumal 

def add(a, b):
    return a + b;     

def subtract(a, b):
    return a - b;  

print("************************************")
print("|                                  |")
print("| Welcome to Addition or Subtraction|")
print("|                                  |")
print("************************************")
type = input("Do you want to do math?(add/subtract) ")
if type == "add" or type == "subtract":
    a = int(input("Enter First Number "))
    b = int(input("Enter second Number "))
    if type == "add":
        res = add(a, b)
        print(" Add : Result : ", res)
    else:
        res = subtract(a, b)
        print(" Subtract : Result : ", res)      
else:
   print("Sorry, Invalid input")   

