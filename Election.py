voter = float(input("Enter your age: "))

if voter >= 18 and voter < 110:
    print(f"You are {voter} years old. You are eligible to vote.")


elif voter < 0:
    print("Invalid age. Age cannot be negative.")  

elif  voter < 18:
    print(f"You are {voter} years old. You are not eligible to vote.")
elif voter >= 110:
    print("Invalid age. You are too old to vote.")

else:
    print("Invalid input. Please enter a valid age.")
