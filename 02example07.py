# Example 7
import math
# Get a number from the user.
number = float(input("Enter a number: "))

# Call the math.sqrt function and
# immediately print its return value.
print(math.sqrt(number))
# Call the math.sqrt function again and
# use its return value in an if statement.
if math.sqrt(number) < 100:
    print(f"The square root is less than 100.")
elif math.squart(number) > 100:
    print(f"The square root is more than 100")
else:
    print(f"The square root is exactly 100") 

"""Notice in example 7, there are three statementsthat call the math.sqrt function, one at
line 10 to print the square root, another at line 14 to check if the square root islessthan
100, and yet another at line 16 to check if the square root is greater than 100. Every time
the computer calls a function, the computer will execute the code that isinside that
function. In example 7, because the arguments are the same at lines10, 14 and 16, the
returned result will be the same in all three cases. So it would be faster to save the result
in a variable and reuse the variable instead, asshown in example 8 at lines10, 12, 14,
and 16."""
