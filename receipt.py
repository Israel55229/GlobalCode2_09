# Challenge
product = input("Enter the name of the product you wnat to buy: ")
price = int(input("Price of product: "))
quantity = int(input("Enter the product quantity: "))
print("========================")
print("|         RECEIPT      |")
print("========================")
print()
print(f"Product: {product}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")

total = (price * quantity)
print(f"Total: {total}")