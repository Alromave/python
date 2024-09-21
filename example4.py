"""The Python programming language includes many augmented assignment operators,
also known as shorthand operators. All the shorthand operators have the same
precedence asthe assignment operator (=). Here is a list of some of the Python shorthand
operators:"""
# **= *= /=  //=  %=  +=  -=

# Example 4
# Compute the total pirce of a pizza
price = 10.95
# Ask the user for the nmber of toppings
number_of_toppings = int(input("How many toppings: "))
# Compute the cost of the toppings
price_of_topping = 1.45
toppings_cost = number_of_toppings * price_of_topping
# Add the costo of th etopping to the price of the pizza
price = price + toppings_cost
# print the price for the user to see
print(f"Price: ${price:.2f}")
