"""The statement at line 16 in example 4 causesthe computer to get the value in the price
variable which is10.95, then add the cost of the toppingsto 10.95, and then store the sum
back into the price variable. Python includes a shorthand operator that combines
addition (+) and assignment (=) into one operator (+=). We can use thisshorthand
operator to rewrite line 16 like this:
price += toppinc_cost"""

"""Thisstatement with the shorthand operator is equivalent to the statement on line 16 of
example 4, meaning the two statements cause the computer to do the same thing.
Example 5 containsthe same program as example 4 but usesthe shorthand operator +=
at line 16."""

# Example 5
# Compute the total of a large pizza is $10.95

price = 10.95
# Ask the user for the number of toppings.
number_toppings = int(input("How many toppings: "))
# compute the cost of toppings
price_per_toppings = 1.45

topping_cost = number_toppings * price_per_toppings

# # Add the cost of the toppings to the price of the pizza.
price  += topping_cost

print(f"Price: ${price: .2f}")
