str="Harry Potter"
# swapcase() convert lowercase letters to uppercase letters and vice versa
print(str.swapcase())

# strip() trimmed version of the string
str2="       Harry Potter        "
str3="*********Harry Potter*************"
print(str2)
print(str2.strip())
print(str3.strip("*,-"))

# spit () separate the string with special characters and returns a list
str4="#kru#hbr#vusd#cuifl#yfic#figf#ybf"
print(str4.split("#"))

# ljust() gives left to the string
x=str.ljust(40)
print(x,"is my favorite movie")

# rjust gives right alignment to the string
y=str.rjust(40)
print(y,"is my favorite movie")

# replace() replace specific value with another value
str5="My name is Sudarshan"
print(str5.replace("Sudarshan","Vaibhav"))