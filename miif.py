score = int(input("Enter your score: "))
if score < 0 or  score > 100:
        print("Invalid score. Score cannot be negative or above 100.")
else:
    if score >= 80 :
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