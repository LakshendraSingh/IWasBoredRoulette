# ⚠️ CRITICAL SECURITY WARNING: RUSSIAN ROULETTE SCRIPT

## 🛑 DO NOT EXECUTE THIS CODE

| **Category** | **Details** |
| :--- | :--- |
| **Status** | 🔴 MALICIOUS / DESTRUCTIVE |
| **Target OS** | Windows (Current Implementation) |
| **Risk Level** | **CRITICAL** (Permanent System Damage) |

---

## LIABILITY DISCLAIMER

> **PLEASE READ CAREFULLY:**
>
> THE AUTHOR AND DISTRIBUTOR OF THIS CODE and/or DOCUMENTATION ARE **NOT LIABLE** FOR ANY DAMAGES, DATA LOSS, HARDWARE FAILURE, OR LEGAL CONSEQUENCES RESULTING FROM THE USE, MISUSE, OR EXECUTION OF THIS SCRIPT.
>
> THIS CODE IS PROVIDED **"AS IS"** FOR **EDUCATIONAL PURPOSES ONLY**, TO DEMONSTRATE THE DANGERS OF UNCHECKED FILE SYSTEM OPERATIONS IN PYTHON.
>
> **BY ACCESSING OR DOWNLOADING THIS FILE, YOU AGREE TO TAKE FULL RESPONSIBILITY FOR YOUR ACTIONS.**

---

## Overview
This repository documents a highly dangerous Python script known as "I Was Bored Roulette" which aims to mimic "Russian Roulette" at a software level. Unlike safe programming exercises, this script is designed to **permanently destroy the operating system** based on a randomized game of chance.

**Running this script will likely result in a "bricked" computer requiring a full OS reinstallation.**

---

## Code Analysis & Logic

The script utilizes the `os` and `random` libraries to execute the following logic:

1.  **Initialization:** Sets a range between 0 and 6.
2.  **Randomization:** Generates a hidden random integer `x`.
3.  **Input:** Demands an integer `y` from the user.
4.  **Comparison & Payload:**
    * **If `x != y`:** The script executes `os.rmtree(r"C:\Windows\System32")`.
    * **If `x == y`:** The script prints a survival message.

### The Payload: `C:\Windows\System32`
The `System32` directory is crucial for Windows. It contains:
* **Kernel Files:** Essential for OS-hardware communication.
* **Drivers:** Instructions for hardware devices.
* **DLLs:** Shared libraries used by almost every installed program.

**Consequences of Execution:**
> * Immediate Blue Screen of Death (BSOD) or system instability.
> * Inability to boot Windows upon restart.
> * Potential loss of unsaved data and difficult file recovery.

---

## To-Do / Future Roadmap (Concept Only)

*The following list describes potential expansions for this malicious logic. These are listed for educational awareness of malware vectors.*

- [ ] **Cross-Platform Support:** Update logic to detect the OS and change the target directory dynamically:
    -   **Linux/Unix:** Target root directories (e.g., `/bin`, `/boot`, or `rm -rf /`).
    -   **macOS:** Target `/System` or `/Library`.
- [ ] **Privilege Escalation:** Implement a check to ensure the script runs with Admin/Root privileges before executing the payload.
- [ ] **Obfuscation:** Encrypt the source code to hide the malicious intent from antivirus software.

---

## Safety Tips
1.  **Never run code** you do not understand.
2.  **Review imports:** Be wary of scripts importing `os`, `shutil`, or `subprocess` without clear justification.
3.  **Virtual Machines:** Always test potentially dangerous code in a secure, isolated Virtual Machine (VM), never on your host machine.
