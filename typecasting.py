"""
Type Casting
Type Casting means conversion from one datatype to another
type() function gives which type of data present in the variable
"""
"""Implicit Type Casting (done by python itself) """
a=120
b=12.34
c=a+b #by adding two different data types here the int is converted into float
print(c)
print(type(c))

"""Explicit Type Casting (do not done by python we have to change it manually)"""
# Example 1
a="1313"
a=int(a) #conversion from string to integer
print(a)
print(type(a))

# Example 2
a=1414
a=float(a) #conversion from integer to float
print(a)
print(type(a))
