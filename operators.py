"""
for ex: a+b
operator = which action will be perform
operand = on what action will be perform
"""
"""
Arithmetic Operator
Addition(+)
Substraction(-)
Multiplication(*)
Division(/)
Exponential(**)
Modulas(%)
Floor Division(//)

"""
a=100
b=23
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b) #gives 100 raised to the power 23
print(a%b) #gives reminder
print(a//b) # gives quotient before decimal value

"""
Comparison Operator
less than (<)
greater than (>)
equal to (==)
less than equal to (<=)
greater than equal to (>=)
not equal to (!=)
"""

a=300
b=79
print(a<b) #gives false because 300 is greater than 79
print(a>b) #gives true because 300 is greater than 79
print(a==b) #gives false because 100 is not equal to 79

a=209
b=209
print(a<=b) #gives true because it satisfies less than or equal to
print(a>=b) #gives true because it satisfies greater than equal to
print(a!=b) #gives false because a is equal to b

"""
Logical Operator
and (if both conditions are true it will give you true otherwise false)
or (if both conditions are false it will return false otherwise true)
not (T->F  F->T)
"""
a=10
b=20
print(b>a and a!=b) #gives true because both conditions are true
print(a<b and a==b) #gives false because one condition is false

print(a<b or a!=b) #gives true because both conditions are true
print(a>b or a==b) #gives false because both conditions are false

print(not a==b) #gives true because the condition gives you false
