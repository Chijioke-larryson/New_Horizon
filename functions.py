def displayName():
    print("Your name is John Doe")

displayName()



def displayNames(name):
    print('My name is : {name}')

displayNames('John Doe')


def sum(a,b):
    return a + b

add = sum(2,4)
print(add)


myName = str(input("Enter your name: ")).capitalize()
myTime = input("Enter your time, (Morning/Afternoon/Evening): ").upper()

def greet(name, time):
    print(f"Good {time}, {name}!")


greet(myName, myTime)

  