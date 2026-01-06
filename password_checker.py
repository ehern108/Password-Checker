import re

common_passwords = {"password", "123456", "12345678", "qwerty", "letmein", "admin", "iloveyou", "welcome", "abc123", "password1"}

def score_password(pw:str)-> tuple[int, list[str],str]:
    tips = []
    score = 0

    #length
    if len(pw)>= 12:
        score+= 30
    elif len(pw) >= 8:
        score+= 20
        tips.append("Make it 12 or more characters for better strength.")
    else:
        score += 5
        tips.append("Too short. Aim for at least 12 characters.")


    #Character types
    if re.search(r"[a-z]",pw):
        score += 15
    else:
        tips.append("Add lowercase letters (A-Z).")

    if re.search(r"[A-Z]",pw):
        score += 15
    else:
        tips.append("Add uppercase letters (A-Z).")

    if re.search(r"\d",pw):
        score += 15
    else:
        tips.append("Add numbers (0-9).")

    if re.search(r"[\w\s]", pw):
        score += 15
    else:
        tips.append("Add symbols (such as !, @, #, $).")

    #Bonus:variety
    if len(set(pw)) >= 8:
        score += 5
    else:
        tips.append("Use more unique characters and avoid repetition.")

    #Penalties
    lower_pw = pw.lower()
    if lower_pw in common_passwords:
        score = min(score,15)
        tips.append("This password is very common and easy to guess.")

    if re.search(r"(.)\1\1", pw):
        score -= 10
        tips.append("Avoid repeating the same character three or more times in a row.")

    if re.search(r"(123|abcd|qwerty)", lower_pw):
        score -= 10
        tips.append("Avoid simple sequences like 1234, abcd, or qwerty.")

    #Clamp score
    score = max(0,min(100,score))

    # Rating
    if score >= 80:
        rating = "Strong"
    elif score >= 50:
        rating = "Medium"
    else:
        rating = "Weak"

    return score,tips,rating

def main():
    print("Password Strength Checker\n")

    pw = input("Enter a password to test: ")

    score,tip,rating = score_password(pw)

    print("\n---------------------------")
    print(f"Score: {score}/100")
    print(f"Rating: {rating}")
    print("---------------------------\n")

    if tip:
        print("How to improve:")
        for t in tip:
            print(f"- {t}")
    else:
        print("Your password looks good!")

if __name__ == "__main__":
    main()
