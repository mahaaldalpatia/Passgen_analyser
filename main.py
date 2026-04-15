import random
import string

COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein",
    "qwerty", "abc123", "monkey", "1234567890", "iloveyou"
]

def box(text, width=45):
    print("+" + "-" * width + "+")
    print("|" + text.center(width) + "|")
    print("+" + "-" * width + "+")

def section(title, width=45):
    print("\n+" + "=" * width + "+")
    print("|" + title.center(width) + "|")
    print("+" + "=" * width + "+")

def analysis(password):
    section("  PASSWORD STRENGTH ANALYSIS  ")

    has_upper = has_lower = has_digit = has_symbol = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in string.punctuation:
            has_symbol = True

    score = 0
    tips = []

    # Length scoring
    length = len(password)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters (12+ is recommended)")

    # Character variety
    if has_upper:
        score += 1
    else:
        tips.append("Add UPPERCASE letters (A-Z)")

    if has_lower:
        score += 1
    else:
        tips.append("Add lowercase letters (a-z)")

    if has_digit:
        score += 1
    else:
        tips.append("Add digits (0-9)")

    if has_symbol:
        score += 1
    else:
        tips.append("Add special characters (e.g. @, #, !, $, %)")

    # Repeated characters check
    has_repeat = any(password[i] == password[i+1] == password[i+2]
                     for i in range(len(password)-2))
    if has_repeat:
        score -= 1
        tips.append("Avoid repeating characters (e.g. 'aaa', '111')")

    # Sequential pattern check
    sequences = ["abcdefghijklmnopqrstuvwxyz", "0123456789", "qwertyuiop", "asdfghjkl"]
    has_sequence = any(seq in password.lower() or seq[::-1] in password.lower()
                       for seq in sequences)
    if has_sequence:
        score -= 1
        tips.append("Avoid sequential patterns (e.g. 'abcd', '1234', 'qwerty')")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        tips.append("This is a very commonly used password — never use it!")

    # Results display
    width = 45
    print(f"\n  {'Criteria':<28} {'Status':>10}")
    print("  " + "-" * 38)
    print(f"  {'Length ('+str(length)+' chars)':<28} {'✓' if length >= 8 else '✗':>10}")
    print(f"  {'Uppercase Letters':<28} {'✓' if has_upper else '✗':>10}")
    print(f"  {'Lowercase Letters':<28} {'✓' if has_lower else '✗':>10}")
    print(f"  {'Digits':<28} {'✓' if has_digit else '✗':>10}")
    print(f"  {'Special Characters':<28} {'✓' if has_symbol else '✗':>10}")
    print(f"  {'No Repeated Chars':<28} {'✓' if not has_repeat else '✗':>10}")
    print(f"  {'No Sequential Patterns':<28} {'✓' if not has_sequence else '✗':>10}")
    print(f"  {'Not a Common Password':<28} {'✓' if password.lower() not in COMMON_PASSWORDS else '✗':>10}")
    print("  " + "-" * 38)

    # Strength label
    if score <= 2:
        strength = "WEAK"
        bar = "[##                     ]"
    elif score <= 4:
        strength = "MEDIUM"
        bar = "[############           ]"
    elif score <= 6:
        strength = "STRONG"
        bar = "[####################   ]"
    else:
        strength = "VERY STRONG"
        bar = "[#######################]"

    print(f"\n  Strength : {strength}")
    print(f"  Score    : {max(score,0)}/7")
    print(f"  {bar}")

    # Tips
    if tips:
        section("  TIPS TO IMPROVE  ")
        for i, tip in enumerate(tips, 1):
            print(f"  {i}. {tip}")
    else:
        print("\n  ✓ Your password looks great! No improvements needed.")

    print("\n+" + "=" * 45 + "+\n")

def pass_gen():
    while True:
        section("  PASSWORD GENERATOR  ")
        length = int(input("  Choose Password Length : "))

        if length >= 8:
            l = string.ascii_letters + string.digits + string.punctuation
            p = ''.join(random.choice(l) for _ in range(length))

            print("\n+" + "=" * 45 + "+")
            print("|" + "GENERATED PASSWORD".center(45) + "|")
            print("+" + "=" * 45 + "+")
            print(f"|  {p:<43}|")
            print("+" + "=" * 45 + "+")

            print("\n  1. Strength Analysis of Generated Password")
            print("  2. Create Another One")
            print("  3. Exit")
            a = int(input("  Choose Option : "))

            if a == 1:
                analysis(p)
                print("  1. Create Another One")
                print("  2. Exit")
                again = int(input("  Choose Option : "))
                if again == 1:
                    continue
                else:
                    box("Thank You!!", 45)
                    break
            elif a == 2:
                continue
            else:
                box("Thank You!!", 45)
                break
        else:
            print("\n  ✗ Invalid Length! Minimum is 8 characters.")
            again = input("  Try Again? (yes/no) : ").lower()
            if again == "yes":
                continue
            else:
                box("Thank You!", 45)
                break

# ── Main ──────────────────────────────────────────
box("STRONG PASSWORD GENERATOR", 45)
print("\n  1. Create New Password")
print("  2. Password Strength Analysis")
print("  3. Exit")
n = int(input("  Enter Choice : "))

if n == 1:
    pass_gen()
elif n == 2:
    section("  STRENGTH ANALYSIS  ")
    user_pass = input("  Enter your Password : ")
    analysis(user_pass)
    print("  1. Create New Password")
    print("  2. Analyse Another Password")
    print("  3. Exit")
    d = int(input("  Enter Choice : "))
    if d == 1:
        pass_gen()
    elif d == 2:
        user_pass2 = input("  Enter your Password : ")
        analysis(user_pass2)
    else:
        box("Thank You!!", 45)
else:
    box("Goodbye!", 45)
