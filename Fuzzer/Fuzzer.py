# =================================================================
# Challenge: whekkees's my first simple crack me by whekkees
# Challenge Link: https://crackmes.one/crackme/69b18083ddd6176826ae8947
# Writeup Link: https://github.com/thefinalbit/ctf-writeups/blob/main/Reverse%20Engineering/whekkees's-my-first-simple-crack-me-by-whekkees.md
# Description: This helper script was created with AI assistance 
#              to fuzz the binary and analyze input crashes.
# =================================================================

import sys
# بقية الكود الخاص بكِ يستمر من هنا...
import subprocess
import sys

TARGET = "./target.exe" 
BASE_PAYLOADS = ["qwert", "whekkees"]

def run_fuzzer():
    print("[*] Starting Fuzzer...")
    
    for base in BASE_PAYLOADS:
        print(f"\n[*] Testing Base Payload: '{base}'")
        for padding_length in range(1, 150):
            payload = base + ("A" * padding_length)
            
            # Progress indicator to show the current payload length
            print(f"\r[>] Trying payload length: {len(payload)}...", end="")
            sys.stdout.flush()
            
            try:
                result = subprocess.run(
                    ["wine", TARGET, payload],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                # Check output for flags or success keywords
                if result.stdout and any(keyword in result.stdout.lower() for keyword in ["flag", "{", "congrat"]):
                    print(f"\n\n[+] Success! Output detected at length {len(payload)}:")
                    print(result.stdout)
                    print("-" * 40)
                
                # If the program exits normally (no crash), continue fuzzing
                if result.returncode == 0:
                    continue
                
                # If return code is not 0, a crash or error occurred
                print(f"\n\n[!!!] Crash detected (Non-zero exit code)!")
                
            except subprocess.TimeoutExpired:
                # If the program hangs (potential Denial of Service)
                print(f"\n\n[!!!] Crash detected (Timeout / Denial of Service)!")
                # Create a dummy result object to hold a custom exit code
                class DummyResult: returncode = "TIMEOUT"
                result = DummyResult()

            # Print the detailed crash report
            print(f"Base: {base}")
            print(f"Padding: {padding_length}")
            print(f"Total Length: {len(payload)}")
            print(f"Exit Code: {result.returncode}")
            print("-" * 40)
            break # Stop testing the current base and move to the next one

    print("\n[*] Fuzzing session finished.")

if __name__ == "__main__":
    run_fuzzer()
