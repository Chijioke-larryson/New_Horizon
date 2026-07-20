new_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_sequence.insert(1, 100)
print(new_sequence)
# print(new_sequence[0:120:])

Details = '''
    This is a multiple line test,
    Trying to figure out how most of this things work
    Test case 1
'''
print(Details.strip())

from string import Template

greeting = Template("Hello, $name! Welcome to $place.")
print(greeting.substitute(name="Alice", place="Wonderland"))



from string import Template

t = Template("Hello, $name")
print(t.substitute(name="World"))


for i in range(3):
    num = eval(input('Enter a number: '))
print ('The square of your number is', num*num )
print("Loop is done ")

for i in range(1):
    name = str(input("What is your name: "))
    age = int(input("How old are you: "))
    village = str(input("What is your name: "))
print(f"My name is {name}, i am {age} years old, I am from {village}")

print("A")
print('B')

for i in range(5):
    print("C")
    print("D")
print("E")
print("F")

for i in range(5):
    print(i,"*" * i  )

