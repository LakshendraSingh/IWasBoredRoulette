⚠️ CRITICAL SECURITY WARNING: RUSSIAN ROULETTE SCRIPT

🛑 DO NOT EXECUTE THIS CODE

Category	Details
Status	🔴 MALICIOUS / DESTRUCTIVE
Target OS	Windows, Linux, and macOS
Risk Level	CRITICAL — Potential Permanent System Damage
Privileges Required	Administrator/root
Primary Behavior	Destructive filesystem deletion

⸻

LIABILITY DISCLAIMER

PLEASE READ CAREFULLY:

THE AUTHOR AND DISTRIBUTOR OF THIS CODE and/or DOCUMENTATION ARE NOT LIABLE FOR ANY DAMAGES, DATA LOSS, HARDWARE FAILURE, OR LEGAL CONSEQUENCES RESULTING FROM THE USE, MISUSE, OR EXECUTION OF THIS SCRIPT.

THIS CODE IS PROVIDED “AS IS” FOR EDUCATIONAL AND SECURITY-AWARENESS PURPOSES ONLY, TO DEMONSTRATE THE DANGERS OF UNCHECKED, PRIVILEGED FILESYSTEM OPERATIONS.

DO NOT EXECUTE THIS SCRIPT ON A REAL SYSTEM OR WITH ADMINISTRATOR/ROOT PRIVILEGES.

⸻

Overview

This repository documents a highly dangerous Python script known as “I Was Bored Roulette”, which attempts to mimic “Russian Roulette” at a software level.

The script generates a random number and asks the user to guess it. If the guess is incorrect, the program attempts to delete critical operating-system directories using elevated privileges.

This is destructive code, not a harmless programming exercise. Execution can result in severe system damage, data loss, loss of system functionality, or an operating system that requires reinstallation.

⸻

Code Analysis & Logic

The script performs the following sequence:

1. Operating-System Detection
    * Uses Python’s platform.system() to identify Windows, Linux, or macOS.
2. Privilege Check
    * Windows checks whether the process has Administrator privileges.
    * Linux and macOS check for root privileges.
    * The program exits if the required privileges are unavailable.
3. Randomization
    * Generates a random integer between 0 and 7 inclusive.
    * Note that the input prompt incorrectly tells the user to select a number between 0 and 6.
4. User Input
    * The user supplies an integer guess.
5. Comparison
    * If the guess matches the generated number, the program prints:
        You survived. THIS TIME.
    * If the guess does not match, the destructive branch is executed.

⸻

⚠️ Destructive Payload

Windows

The Windows branch attempts to launch elevated commands against paths including:

* C:\
* C:\Windows\System32
* C:\Windows\System32\drivers
* C:\Windows\System32\config

It uses PowerShell to launch cmd.exe with rmdir /s /q.

Linux

The Linux branch attempts recursive deletion of critical system locations including:

* /
* /usr/bin
* /usr/lib
* /lib
* /etc
* /lib/modules
* /bin
* /boot

It invokes sudo rm -rf against these paths.

macOS

The macOS branch similarly attempts recursive deletion of critical locations including:

* /
* /usr/bin
* /usr/lib
* /etc
* /System/Library
* /System
* /bin

It invokes sudo rm -rf against these paths.

⸻

Why This Is Dangerous

The targeted locations contain files required for the operating system to function.

Deleting or corrupting these files can cause:

* Failure to boot.
* Severe operating-system instability.
* Broken system utilities and applications.
* Loss of system configuration.
* Loss of user and application data, depending on what deletion succeeds.
* A potentially unrecoverable system without restoration or OS reinstallation.

The exact outcome depends on the operating system, filesystem protections, permissions, system state, and which deletion commands successfully execute.

Do not assume that modern operating systems will automatically protect the system from this script.

⸻

Important Code Details

The random-number range

The script *intentionally* contains:

initialValue = 0
finalValue = 7
x = random.randint(initialValue, finalValue)

random.randint() includes both endpoints, meaning the generated value can be 0 through 7.

However, the prompt says:

pick a number between 0 and 6

Therefore, there is currently an additional 7 that the user is not explicitly told about.

Privilege escalation

The script intentionally requires elevated privileges before reaching the game logic. This substantially increases the potential impact of the destructive commands.

Error handling

The destructive subprocess calls use:

check=False

Consequently, unsuccessful commands do not necessarily stop the program from continuing to subsequent targets.

⸻

Safety Notice

Do not run this script on your primary computer.

Do not execute it:

* With sudo.
* From an Administrator command prompt.
* On a production machine.
* On a computer containing important data.
* On a shared or organizational system.
* On a system you do not have explicit permission to test.

If this repository is being used for security education, the destructive filesystem operations should be replaced with harmless simulations.

⸻

To-Do / Future Roadmap

The project should focus on safe security education and detection, rather than improving the destructive payload.

* Add explicit warnings before the game starts.
* Document how privileged filesystem operations can become dangerous.
* Add examples of safe sandboxing and defensive testing.
* Document indicators that security tools could use to identify destructive behavior.

⸻

Safety Tips

1. Never run code you do not understand, especially code requesting Administrator/root privileges.
2. Treat rm -rf, rmdir /s /q, and recursive deletion of system directories as potentially destructive.
3. Review uses of modules such as os, shutil, and subprocess when they interact with the filesystem or execute shell commands.
4. Be particularly cautious when code requests elevated privileges.
5. Use disposable virtual machines or dedicated test environments for legitimate security research.
6. Keep important data backed up independently of the machine being tested.
7. For educational demonstrations, simulate destructive actions instead of performing them.