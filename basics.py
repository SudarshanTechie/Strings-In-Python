# print statement
# 1)
print("Hello World!")
# 2)
print('Hello World!')

# Comments in python
# 1) Single Line Comment (Using Hash)
# This is comment1

# 2) Multiline Comment (using """ """)
""" This is 
multiline comment
 """

# Variables ( Container that stores value )
a="Sudarshan"
b=23
# Here a & b are variables that store value sudarshan & 23 respectively

# Data Types
# type() gives which type of data present in variable
a=10
b=10.6
c="Sudarshan"
d= a>b
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Input: To get values from user
# 1) To get input as a string
name=input("Enter your name : ")
print(name)

# 2) To get input as a integer
age=int(input("Enter your age = "))
print(age)

# 3) To get input as a float
weight=float(input("Enter your weight : "))
print(weight)

# 4) To get input as eval ( eval solve expression which is in string datatype )
exp=eval(input("Enter expression here = ")) #for ex: 2+4
print(exp)