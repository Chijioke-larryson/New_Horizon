vote = int(input("Enter your age: "))


if vote >= 18 and vote < 110:
    print(f"You are {vote} years old. You are eligible to vote.")
elif vote < 0:
    print("Invalid age. Age cannot be negative.")
elif vote < 18:
    print(f"You are {vote} years old. You are not eligible to vote.")
elif vote >= 110:
    print("Invalid age. You are too old to vote.")
else:   
    print("Invalid input. Please enter a valid age.")