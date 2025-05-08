"""
-String are the collection of multiple words or multiple letters together
-we can store a string in a variable
"""
name="Sudarshan Gambhire" #String
print(name)
print(type (name)) #type() function gives which type of data present in the given variable

# String Slicing
print(name[2:9]) #gives characters from 2 to 8
print(name[:9]) #automatically starts with 0
print(name[10:]) #automatically ends with last index
print(name[-8:]) #starts with -8 index till end
str="0123456789"
print(str[::2]) #here the output is with gap of two
print(str[::-1]) # gap of -1 means reverse the string
print(str[:7:2]) # gap of 2 only upto seven characters

# Iteration in string (to get single letter )
# for i in name:
#     print(i)

