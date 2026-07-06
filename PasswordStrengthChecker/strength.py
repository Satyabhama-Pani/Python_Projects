# 2. Password Strength checker
print("\n" + "*"*40)
print(f"{"\U0001F6E1\uFE0F Password Strength checker\U0001F6E1\uFE0F":^40}")
print("*"*40)
upper_count, lower_count, digit_count, special_count =(0,0,0,0)
score = 0
try:
    password = input("Enter your passoword: ")  
    # validation
    if len(password) >= 8:
        score +=1 
        for ch in password:
            if ch.isupper():
                upper_count += 1
            elif ch.islower():
                lower_count += 1
            elif ch in "@#$*_":
                special_count += 1          
            elif ch.isdecimal():
                digit_count += 1
except Exception as e:
    print("Unexpected Error: {e}")

# count score
if upper_count > 0:
    score += 1
if lower_count > 0:
    score += 1
if digit_count > 0:
    score += 1
if special_count > 0:
    score += 1

# check score
if score == 5:
    strength = "Strong Password\u2705"
elif score >= 3:
    strength = "Medium Password\u26A0\uFE0F"
else:
    strength = "Weak Password\u274C"

# Scoreboard    
print("======Score\U0001F512======")
print(f'''Length: {len(password)}
Uppercase letter: {upper_count}
Lowercase letter: {lower_count}
Digits: {digit_count}
Special character: {special_count}
Toatl Score: {score}/5
Strength: {strength} 
''')