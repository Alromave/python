"""If you have written programsin other programming languagessuch asJavaScript, Java,
or C++, you always used curly bracesto mark the start and end of the body of an if
statement. However, notice in example 6 that if statementsin Python do not use curly
braces. Instead, we type a colon (:) after the comparison of the if statement asshown on
line 8. Then we indent all the statementsthat are in the body of the if statement as
shown on lines 9 and 10. The body of the if statement ends with the first line of code
that is not indented, like line 13."""

"""It may seem strange to not use curly bracesto mark the start and end of the body of an if
statement. However, the Python way forces usto write code where the indentation
matchesthe functionality or in other words, the way we indent the code matchesthe way
that the computer will execute the code.
"""

# if … elif … else Statements
#Each if statement may have an else statement asshown in example 7 on line 13. We can
#combine else and if into the keyword elif asshown on lines 9 and 11.

#Example 7
# Get the cost of an item from the user.

cost = float(input("Please enter the cost:"))
# Determine a discount rate based on the cost.
if cost < 100:
    rate = 0.1
elif cost <250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.2
print()
print("Este es un ejemplo \n de partir una línea")


# Compute the discount amount
# and the discounted cost.

discount = cost * rate

cost -= discount
# Print the discounted cost for the user to see.

print(f"Cost: {cost: .2f}")

"""Logical Operators
Python includestwo logic operators which are the keywords and, or that we can use to
combine two comparisons. Python also includesthe logical not operator. Notice in
Python that the logical operators are literally the words: and, or, not and notsymbols as
in other programming languages:"""

"""if driver >= 54 or (driver >= 32 and passenger >= 54):
message = "Enjoy the ride!"""



