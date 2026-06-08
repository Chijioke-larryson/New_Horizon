# menu  = {"rice": "$1.50", "milk": "$0.99", "eggs": "$2.50", "bread": "$1.00", "cheese": "$3.00"}

# total = 0
# cart = []
# while True:
#     item = input("Enter an item to add to your cart (or 'q' to quit): ").lower()
#     if item.lower() == 'done':
#         break
#     elif item in menu:
#         cart.append(item)
#         total += float(menu[item].strip('$'))
#         print(f"{item} added to cart. Current total: ${total:.2f}")
#     else:
#         print("Item not found in menu. Please try again.")

# num1 = {5}
# print(type(num1))

score = {"james": 90, "susan": 85, "michael": 92, "henry": 88, "lisa": 95}
print(score.get("james"))