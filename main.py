import random
import string
def pass_gen():
    
    while True:
        length = int(input("Choose Password Length :"))
        if length >= 8:
            l = string.ascii_letters+string.digits+string.punctuation
            p = ''.join(random.choice(l) for _ in range(length)) 
            print("Your Password =",p)
            print("---Password Generated---")
            a = int(input("1. Strength Analysis Of Generated Password\n2. Create Another One\n3. Exit\nChoose Option :"))
            if a==1:
               analysis(p) 
               again = int(input("1. Create Another One\n2. Exit\nChoose Option: "))
               if again == 1:
                    continue
               else:
                    print("Thank You!!")
                    break
            elif a==2:
                continue
            else:
                print("Thank You!!")
                break
       
        
        else:
            print("Invalid Length!!!\nChoose a Minimum Length of 8 Characters!")
            again = input("Wanna Try Again(Yes/No): ").lower()
            if again == "yes":
                continue
            else:
                print("Thank You!")
                break

def analysis(password):
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
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1

    if score <=2:
        print("Password Strength :Weak")
    if score == 3:
        print("Password Strength :Medium")
    if score == 4 or score == 5:
        print("Password Strength :Strong")
        
    

print("---Strong Password Generator---")
n = int(input("1.Create New Password\n2.Password Strength Analysis\n3.Exit\nEnter Choice:"))

if n==1:
    pass_gen()
elif n==2:
    user_pass = input("Enter your Password:")
    analysis(user_pass)
    d =int(input("1.Create New Password\n2.Password Strength Analysis\n3.Exit\nEnter Choice:"))
    if d==1:
        pass_gen()
    elif d==2:
        analysis()
    else:
        print("Thank You!!")

else:
    print(end ="")
