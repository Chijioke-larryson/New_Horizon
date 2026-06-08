#  Write a Python function that takes a string as an argument and prints whether it
# is upper- or lowercase.



# def name(s):
#     if s.isupper():
#         print("The string is uppercase.")
#     elif s.islower():
#         print("The string is lowercase.")
#     else:
#         print("The string is neither uppercase nor lowercase.")

# name(input("Enter a string: "))


# Write a generator that alternates between returning Even and Odd.
def even_odd():
    n = 0
    while True:
        yield n
        n += 1
        yield n
        n += 1
gen = even_odd()
for _ in range(10):
    print(next(gen))

