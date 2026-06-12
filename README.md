# 🛡️ Cybersecurity Scripts & Research Lab

Welcome to my security research repository. This repository serves as a centralized lab where I document my solutions for various Capture The Flag (CTF) challenges, reverse engineering tasks, and custom automation tools.

Everything here is structured cleanly into dedicated modules to separate automation scripts from core code analysis.

---

## 📂 Repository Structure & Directory Guide

To navigate through this repository without getting lost, please use the guides below:

### 1. 🚀 [Fuzzer](./Fuzzer)
This folder contains automated fuzzing and stress-testing scripts designed to find software behaviors and input crashes.
* **Key Files:** `Fuzzer.py` (The main automation tool).
* **Documentation:** Inside this folder, you will find a dedicated `README.md` explaining how to configure and run the script.

### 2. 🔏 [knock](./knock)
This folder is dedicated to low-level software analysis and vulnerability research. 
* **Key Files:** `knock.c` (The target low-level C program).
* **Documentation:** Contains a detailed writeup analyzing memory layouts, command-line arguments (`argc`/`argv`), and how environment differences affect execution flow.

---

## 🛠️ Global Prerequisites

To run or test any script in this repository, ensure your environment has:
* **Python 3.x** (For automation and tooling).
* **GCC/Clang** (For compiling low-level C files).
* **Linux Environment / Virtual Machine** (Recommended for safe execution and binary analysis).

---

## 🤝 Disclaimer
> [!IMPORTANT]
> All tools and code in this repository are created and used strictly for **educational purposes** and ethical hacking practice. Do not use them against unauthorized targets.

---
*Created and maintained with a focus on low-level software engineering and offensive security research.*
