#Stretch Challenges
"""
Near the beginning of your program replace the code that asksthe user for the
subtotal with a loop that repeatedly asksthe user for a price and a quantity and
computesthe subtotal. Thisloop should repeat until the user enters "0" for the
price.
"""
# To set the day of the week
from datetime import datetime
current_date_and_time =  datetime.now()

day_week_day = current_date_and_time.weekday()

# parametres

subtotal = 0
print("Enter the price and quantity for each time: ")

price = 1
while price != 0:
    price = float(input("Please enter the price: "))
    if price != 0:
        quantity= int(input("Please enter the quantity: "))
        subtotal += price * quantity

subtotal = round(subtotal, 2)
print(f"subtotal: {subtotal: .2f}")
print()


if subtotal > 50 and (day_week_day == 1 or day_week_day == 3):
    discount_rate = 0.1
else:
    discount_rate = 0
print(discount_rate)
discount = subtotal * discount_rate
total = subtotal - discount


sales_tax_rate = 0.06
sales_tax = total * sales_tax_rate


total += sales_tax

print(f" Sales tax amount: {sales_tax:.2f}")
print (f" Total: {total:.2f}")



