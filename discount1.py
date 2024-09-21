from datetime import datetime
subtotal = 0
print("Enter the price and quantity for each item.")
price = 1
while price != 0:
    price = float(input("What is the price"))
    if price != 0:
        quantity = int(input("What is the quantity"))
        subtotal += price * quantity
subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal: .2f}")
