# Example 8
import math
# Get a number from the user.
number = float(input("What is the number "))
# Call the math.sqrt function and store its
# return value in a variable to use later.
root = math.sqrt(number)
print(f"The square root is {root:.2f}")
if root < 100:
    print(f"The square root is less than 100.")
elif root > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")

#Summary
"""A function is a group ofstatementsthat together perform one task. The computer will
not execute the code in a function unless you write code that callsthe function. In this
lesson, you learned how to call built-in functions, functionsthat are in a module, and
functions(methods) that belong to an object."""

"""
1. To call a built-in function, write code that follows this template:
    variable_name = function_name(arg1, arg2, … argN)
2. To call a function from a module, import the module and write code that follows
this template:
    import module_name
    variable_name = module_name.function_name(arg1, arg2, … argN)

3. To call a method, write code that followsthis template:
    variable_name = function_name(arg1, arg2, … argN)
    import module_name
"""

