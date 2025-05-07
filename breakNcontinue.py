"""
Break and Continue

1) Continue : to skip special iteration from loop
2) Break : to stop the loop
"""

# Example for continue
for i in range(1,11):
    if i==5:
        continue #to skip iteration i==5
    print(i)

# Example for break
for i in range(1,50):
    if i==9:
        break # loop will stop when i hit to 9
    print(i)