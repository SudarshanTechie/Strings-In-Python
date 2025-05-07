"""
Loops
To perform single task multiple times (Repeat Tasks)
2) while True:
-It is a infinite loop
-To stop this loop we use break statement
-It is basically use for getting input repeatedly

Syntax:
while True
   #block of code
   break


"""

# Example
# getting input and add two numbers using while true loop
while True:
    a=int(input("Enter a number = "))
    b=int(input("Enter a number = "))
    print("Addition = ",a+b)
    c=input("Do you want to repeat = ")
    if c=="n" or c=="N":
        print("Thank You!!")
        break