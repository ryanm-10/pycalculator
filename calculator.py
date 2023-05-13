#Calulator for two numbers

#defying functions for add,sub,etc.
def add(a,b) :
    added = a + b
    return added
def mult(a,b):
    multiplied = a * b
    return multiplied
def div(a,b):
    divided = a / b
    return divided
def sub(a,b):
    subtracted = a - b
    return subtracted

#ask for add,sub,etc.
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", sub(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", mult(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", div(num1,num2))
else:
   print("Invalid input")
