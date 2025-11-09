# 🔐 Strong Password Generator

A simple and fun Python project that generates strong, random passwords and checks their strength.  
Built to practice Python basics, loops, conditionals, and working with built-in modules like `random` and `string`.

---

## 🚀 Features

- 🔄 Generate random passwords of any custom length  
- 🧠 Analyze password strength (Weak / Medium / Strong)  
- 🔢 Uses uppercase, lowercase, numbers, and special symbols  
- 🧱 Minimum password length: 8  
- 🖥️ Simple, menu-driven console interface  

---

## 🧠 How It Works

1. Choose what you want to do:
   - Create a new password  
   - Analyze the strength of your existing password  
2. When creating a password:
   - Enter a desired length (minimum 8 characters)  
   - The program generates a random password using letters, digits, and punctuation  
3. You can then:
   - Check its strength  
   - Generate another password  
   - Exit the program  

---

## 💪 Password Strength Logic

The strength is calculated based on the presence of:

- Uppercase letters  
- Lowercase letters  
- Numbers  
- Special symbols  

Each category adds to the score → higher score = stronger password.

| Score | Criteria Met | Strength |
|:------|:--------------|:----------|
| 1–2 | Few character types | Weak |
| 3 | Most character types | Medium |
| 4 | All character types | Strong |

---

## ⚙️ How to Run

```bash
# Clone this repository
git clone https://github.com/<your-username>/<repo-name>.git

# Navigate to the project directory
cd <repo-name>

# Run the program
python password_generator.py
