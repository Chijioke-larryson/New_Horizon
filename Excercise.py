#1

# name = input("What is your name: ")

# for i in range(100):

#     print(i, name)

    #2

# name = 'Larryson Chijioke'
# while  True:
#     print(name, end=" ")


#3

# name = input("What is your name?: ")
# for i in range(100):
#     print(i+1, f"Your name is {name}" )

#4

# integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# for integer in integers:
#     print(f"{integer} ----",integer*integer)


#5

# for i in range(8, 90, 3):
#     print(i)


#6

# for i in range(100, 1, -2):
#     print(i)

#7

# for i in range(10):
#     print("A", end="")
# for i in range(7):
#     print("B", end="")
# for i in range(4):
#     print("C", end="")
#     print("D", end="")
# print("E",end="")
# for i in range(6):
#     print("F", end="")
# print("G", end="")
# print()

#8

# name = input("What is your name: ")
# num = int(input("How many times do you want to print your name: "))
# print(name * num,)
    
    #8

# name = input("What is your name: ")
# num = int(input("How many times do you want to print your name: "))
# for i in range(num):
#     print(i+1, name)


#9
# a = 1
# b = 1
# a,b = b,a
# n = int(input("How many Fibonacci do you want printed?:  "))

# for i in range(n):
#     print(a, end=" ")
#     a,b = b,a+b

    #10
# wide = int(input("How wide should the '*' print?: "))
# high = int(input("How high should the '*' print?: "))

# for i in range(high):
#     print("*" * wide)

#11


# wide = int(input("How wide should the '*' print?: "))
# height = int(input("How high should the '*' print?: "))

# for row in range(height):
#     if row == 0 or row == height - 1:
#         print("*" * wide)
#     else:
#         print("*" + " " * (wide - 2) + "*")

#12
# height = int(input("How high should the '*' print?: "))
# for i in range(height):
#     print('*' * (i+1))

#13

# height = int(input("How high should the '*' print?: "))
# for i in range(height):
#         print("*" * (height - i))

#14
#We are trying to draw a diamond shape using asterics

height = int(input("How high should the '*' print?: "))
mid = height // 2
# First half (expanding)
for i in range(mid):
    print(" " * (mid - i - 1) + "*" * (2 * i + 1))
# Second half (contracting)
for i in range(mid, height):
    print(" " * (i - mid) + "*" * (2 * (height - i - 1) + 1))