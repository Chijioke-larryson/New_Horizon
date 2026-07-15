# def calculate(quantity, price, discount_percent, tax_percent):
#     subtotal = quantity * price
#     discount = subtotal * (discount_percent / 100)
#     amount_after_discount = subtotal - discount
#     tax = amount_after_discount * (tax_percent / 100)
#     total = amount_after_discount + tax

#     print("\nReceipt")
#     print("-------")
#     print("Quantity:", quantity)
#     print("Price per item:", price)
#     print("Subtotal:", subtotal)
#     print("Discount:", discount)
#     print("Tax:", tax)
#     print("Total amount to pay:", total)


# quantity = int(input("Enter quantity: "))
# price = float(input("Enter price per item: "))
# discount_percent = float(input("Enter discount percentage: "))
# tax_percent = float(input("Enter tax percentage: "))

# calculate(quantity, price, discount_percent, tax_percent)

# job = "Doctor"

# def occupation():
#     global job
#     job = 'Surgeon'
#     print("My occupation is:", job)

# occupation()

# print("I am still A :", job)

def greeting(name="John Doe", time="day"):
    print("Hello, " , name , "Good,",time, "!!!!!")

greeting()

# greeting("Alice", "morning")
# greeting("Bob", "Afternoon")


# import math

# def area():
#     radius = float(input("Enter the radius of the circle: "))
#     area = math.pi  * pow(radius, 2)
#     print("The area of the circle is:", round(area, -1))

# area()

# b = 3
# c = 5
# a = 3

# def add(a,b):
#     return a + b

# add(b, c)
# print("The sum is:", add  )


# def area(radius):
#     return 3.146 * radius * radius

# r = float(input("Enter the radius of the circle: "))
# h = float(input("Enter the height of the circle: "))

# calc_area = area(r)

# def vol(a, h):
#     print("The volume of the circle is:", a * h, )

# vol(calc_area, h)
# vol(area(r), h)








def add(a,b):
    return a + b

sum = add(2,3)
print(sum)


    