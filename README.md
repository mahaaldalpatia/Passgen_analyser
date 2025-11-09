🔐 Strong Password Generator

A simple Python project that generates strong, random passwords and checks how secure they are.
Made to practice Python basics, logic building, and a bit of user interaction in the console.

🚀 Features

Generate random passwords of custom length

Analyze password strength (Weak / Medium / Strong)

Uses uppercase, lowercase, numbers, and special characters

Minimum password length: 8

Simple text-based menu system

🧠 How It Works

Choose if you want to:

Create a new password

Check the strength of an existing password

When creating one, just enter the length you want (≥ 8).

The program builds a random password using letters, digits, and symbols.

You can then analyze its strength or generate another one.

💪 Password Strength Logic

It checks your password for:

Uppercase letters

Lowercase letters

Numbers

Special symbols

Each type adds to your score → higher score = stronger password.

Score	Strength
1–2	Weak
3	Medium
4	Strong
⚙️ How to Run
# Clone this repo
git clone https://github.com/<your-username>/<repo-name>.git

# Move into the folder
cd <repo-name>

# Run the script
python password_generator.py

🧰 Requirements

Python 3.x

Modules used: random, string (both built-in)
