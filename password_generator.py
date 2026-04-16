import random
import time

# --- Configuration & Dataset ---
DATA = {
    "names": ["Ali", "Mustafa"],
    "years": ["2006"],
    "football": ["Messi"],
    "cars": ["Mercedes"],
    "cats": ["Siri"],
    "sons": ["Ahmed"]
}

# Flatten the dictionary values into a single list for random selection
BASE_WORDS = [word for sublist in DATA.values() for word in sublist]
SPECIAL_CHARS = ['@', '#', '_', '!', '$']
TARGET_COUNT = 100000

def run_generator():
    """
    Generates a unique wordlist for security awareness demonstration.
    Uses a set to ensure O(1) lookups and zero duplicates.
    """
    passwords = set()
    start_time = time.time()

    print(f"[*] Initializing password generation for {TARGET_COUNT} entries...")

    while len(passwords) < TARGET_COUNT:
        # Randomized components
        w1 = random.choice(BASE_WORDS)
        w2 = random.choice(BASE_WORDS)
        char = random.choice(SPECIAL_CHARS)
        num = str(random.randint(0, 9999))
        
        # Applying diverse patterns to simulate real-world dictionary variations
        patterns = [
            f"{w1}{w2}",                     # Simple concatenation
            f"{w1}{char}{num}",              # Word + Symbol + Number
            f"{w1.upper()}{num}",             # Uppercase variation
            f"{w1.lower()}{char}{w2.lower()}",# Lowercase with separator
            f"{w1.capitalize()}{num}{char}", # Professional/Standard format
            f"{num}{w1}{char}{num}"          # Complex numeric padding
        ]
        
        # Add a random pattern to the set (duplicates are ignored automatically)
        passwords.add(random.choice(patterns))

    # --- File I/O Operation ---
    try:
        with open("passwords.txt", "w", encoding="utf-8") as f:
            for entry in passwords:
                f.write(f"{entry}\n")
        
        end_time = time.time()
        duration = round(end_time - start_time, 2)

        # Standard Lab Output Requirement
        print(f"✅ Successfully generated {len(passwords)} passwords!")
        print(f"📁 Saved to: passwords.txt")
        print(f"⏱️  Time elapsed: {duration} seconds")

    except IOError as e:
        print(f"[!] Critical Error: Could not write to file. {e}")

if name == "main":
    run_generator()