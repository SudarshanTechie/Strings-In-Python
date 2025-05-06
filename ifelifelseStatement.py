"""
conditional statement
3) if elif else
we use if elif else statement when we have more than two conditions to check
using elif statement we can check numerious conditions

Syntax:

if condition1:
   #block of code
elif condition2:
   #block of code
elif condition3:
   #block of code
else:
   #block of code
"""
# Example 1
signal="green"
if signal=="red" or signal== "Red":
    print("Stop")
elif signal=="yello" or signal=="Yello":
    print("Get Ready")
elif signal=="green" or signal=="Green":
    print("Go")
else:
    print("invalid input")

# Example 2
marks=90
if marks>=90:
    print("A+")
elif marks>=80 and marks<90:
    print("A")
elif marks>=70 and marks<80:
    print("B+")
elif marks>=60 and marks<70:
    print("B")
elif marks>=50 and marks<60:
    print("C+")
elif marks>=35 and marks<50:
    print("C")
else:
    print("You Failed")