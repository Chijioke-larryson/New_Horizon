# # rem = 0
# # num = 2

# # num = int(input("Enter a number: "))
# # num2 = num

# # sum
# sum = 5
# for i in range (1,6):
#     sum = (sum +i +2) 
#     #  sum = 5 + 1 + 2 =  8
#     #   sum = 8 +2 +2 = 12
#     # 
#     # 
#     # 
#     print('The sum is :',sum, ',',end=" ")




# sum = 0
# for i in range (5):
#     num = eval(input("Enter a number: "))  
#     sum = sum + num
    
# print("The sum of the numbers is:", sum)
# print("The avg of the numbers is ", sum/5)

# Finding the min 

# min =  num 
# num1 = eval(input("Enter a number: "))
# for i in range (4):
#     num2 = eval(input("Enter a number: "))
#     if num1 < num2:
#      num1 = num2
# print("The maxiimum number is:", num1)



# num1 = eval(input("Enter a number: "))
# for i in range (4):
#     num2 = eval(input("Enter a number: "))
#     if num2 < num1:
#      num1 = num2


# num1 = eval(input("Enter a number:"))

# for i in range(4):
#     num2 = eval(input("Enter a number: "))
#     if num1 > num2:
#         num1 = num2
# print('The minumum is :', num1)
        







# print("The minimum number is:", num1)
# from random import randint


# user_num = eval(input("Enter a number between 1 and 100: "))


# rand_num = randint(1,100)
# if user_num == rand_num:
#      print("Congratulations! You guessed the number.")  
# elif user_num < rand_num:
#      print("Too low! Try again.")
# else:
#      print("Your random number is :", rand_num)


# from random import *

# for i in range (7):
#     rand_num = randint(1,15)
#     print('Hello ' * rand_num)


# Write a program that count how many  of the squared of the number 1 to 100 end in a 1   

# count = 0
# from hashlib import new


# from xxlimited import new


# for i in range (1,101):
#     square = i ** 2
    
#     if square %10 == 1:
#         print(i)
    #     # count = square
    #     # print(square, end=" ")
    #      count += 1
# print("The count of squared numbers that end in 1 is:", count)

# for i in range(count):
#     print(i, end=" ")

#1

# count = 0

# for i in range (1,101):
#         square = i ** 2
#         if square %10 == 1:
#             print(i)
#             count += 1
# print("The count of squared numbers that end in 1 is:", count)


#´2
# from hashlib import new


# count = 0

# for i in range(1,101):
#         square = i ** 2
#         if square %10 == 1:
#             # print(i)
#             new_count = count + 1
#             print(count, end=" ")
#         if square % 10 == 9:
#           count += 1
#           print(count, end=" ")
    
#Write a program that asks the user to enter a value n, and compute (1,1/2,1/3,...,1/n) - ln  and print the result. he Ln function is log from math module

# from math import log
# from fractions import Fraction
# n = eval(input("Enter a value n: "))
# result = 0
# for i in range(1, n+1):
#     result += 1/i
#     answer = result - log(n)
# print("The result of the series is:", answer)
# Fraction(answer)
      
# print("The natural logarithm of n is:", Fraction(log(n)))


# def sign_flopping(n):
#     for i in range(1, 100):
#         if i % 2 != 0:
#             print(i,'+' ,end="")
#         else:
#             print(i,'-' ,end="")
# sign_flopping(10)
# n = eval(input("Enter a value n: "))
# sign = 1
# total = 1
# for i in range(2, n+1):
#    total += i * sign
#    sign = -sign
# print("The result of the series is:", total)


#Ask a user to entre a number that  and fid sum of the divisor of that number and print the result

n = eval(input("Enter a number: "))
sum_divisors = 0
for i in range(1, n +(-1)):
    if n % i == 0:
        sum_divisors += i
print("The sum of the divisors of", n, "is:", sum_divisors)
