score = int(input("Enter your score: "))

try:
    score = int(score)
    if score < 0:
        print("Invalid score. Score cannot be negative.")

    elif score >= 80 and  score <= 100:
        print("Your grade is A+")
    elif score >= 70  and score <= 79:
        print("Your grade is A")
    elif score >= 60 and score <= 69:
        print("Your grade is B")
    elif score >= 50 and  score <= 59:
        print("Your grade is C")
    elif score >= 40 and score <= 49:
        print("Your grade is D")
    elif score >= 35 and score <= 39:
        print("Your grade is E")
    else:
        print("Your grade is F")

except ValueError as e:
    print(f"Invalid input. Please enter a valid integer score.. {e}")     

