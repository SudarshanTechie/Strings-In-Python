str=("why fit in, when you born to stand out!")

# len() to get a length of string
a=len(str)
print(a)

# count() to calculate how much letter or word present in the string
print(str.count("o"))
print(str.count("in"))

# lower() to convert all string to lowercase
# upper() to convert all string to uppercase
print(str.lower())
print(str.upper())

# title() conversion of every first letter to capital letter
print(str.title())

# find() to find a index number of letter or word
print(str.find("fit"))
print(str.find("y"))

# capitalize() convert the first letter to capital letter
print(str.capitalize())

# index() to find index of letter or world within a range
print(str.index("i",1,6)) #print 5
print(str.index("i",6,10)) #print 8

name="John"
a="my name is {}"
# format() to write variable inside a string
print(a.format(name))

a="abc"
b="123"
c="123abc"
d="123 abc"
e=" "
# isalnum : string should contain alphabets or numeric value or combination of both.
print(a.isalnum())
print(b.isalnum())
print(a.isalnum())
print(d.isalnum())

# isalpha() : return true when if all characters in the string are alphabets
print(a.isalpha())
print(b.isalpha())

# isdecimal() : return true if all characters in the string are integer
print(b.isdecimal())
print(a.isdecimal())

# islower() : check the string is in lower case or not
print(str.islower())

# isupper() : check the string is in upper case or not
print(str.isupper())
str3="SUDARSHAN"
print(str3.isupper())

# isspace() return true if string only contains white spaces
print(str.isspace())
str4=" "
print(str4.isspace())

# istitle() check if string follows title rule or not
print(str.istitle())
str5="Sudarshan Gambhire"
print(str5.istitle())

# endswith() return true when string ends with what we give
str6="John"
print(str6.endswith("n"))

# startswith() return true when string starts with what we give
print(str6.startswith("J"))

