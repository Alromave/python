# 02 Team Activity: Calling Functions
#Instructions
"""
Each lesson in CSE 111 contains a team activity that is designed to take about one hour to
complete. You should prepare for all team activities by completing the preparation
material and the individual checkpoint assignment before starting a team activity. The
goal of the team activities is for studentsto work together and teach and learn from each
other. As your team completes a team activity, instead of moving through it as quickly as
you can, you should help everyone understand the concepts.
"""
# Problem Statement
"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which
are the store's slowest sales days. On Tuesday and Wednesday, if a customer's subtotal is
$50 or greater, the store will discount the customer's subtotal by 10%.
"""

#Assignment
"""
Work as a team to write a Python program named discount.py that gets a customer's
subtotal as input and gets the current day of the week from your computer's operating
system. Your program must not ask the user to enter the day of the week. Instead, it must
get the day of the week from your computer's operating system.
If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must
subtract 10% from the subtotal. Your program must then compute the total amount due
by adding salestax of 6% to the subtotal. Your program must print the discount amount
if applicable, the salestax amount, and the total amount due.
"""

#Core Requirements
"""
Your program asks the user for the subtotal but does not ask the user for the day of
the week. Your program gets the day of the week from your computer's operating
system.
2. Your program correctly computes and prints the discount amount if applicable.
3. Your program correctly computes and prints the sales tax amount and the total
amount due.
"""
from datetime import datetime
current_date_and_time =  datetime.now()
print (current_date_and_time)
day_week_day = current_date_and_time.weekday()

#print(day_week_day)
"""
subtotal = float(input("Please enter the subtotal: "))
#print(subtotal)
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
"""

# Stretch Challenges
"""
If your team finishesthe core requirementsin lessthan an hour, complete one or more of
these stretch challenges. Note that the stretch challenges are optional.
"""
"""
1. Add code to your program that the computer will execute if today is Tuesday or
Wednesday and the customer is not purchasing enough to receive the discount.
This added code should compute and print the difference between $50 and the
subtotal which isthe additional amount the customer would need to purchase in
order to receive the discount.
"""

"""
if subtotal < 50:
    gap = 50 - subtotal
    print(f"You should buy more {gap: .2f} dollars")
    
"""
"""
2. Near the beginning of your program replace the code that asks the user for the
subtotal with a loop that repeatedly asks the user for a price and a quantity and
computesthe subtotal. This loop should repeat until the user enters "0" for the
price
"""

dic_rate = 0.1
sales_tax_rate = 0.06
subtotal = 0
print("Enter the price and quantity por each time")
price = 1
while price != 0:
    price = float(input("Pleas enter the price"))
    if price != 0:
        quantity = int(input("Please enter the quantity:"))

        subtotal += price * quantity
        




