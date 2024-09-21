# Example 3
# Python has many arithmetic operators including power (**), negation (-), multiplication
# (*), division (/), floor division (//), modulo (%), addition (+), and subtraction (-).
# Operator Precedence
# Un comentario de parrafo se hace con tres comillas
"""When we write an arithmetic expression that contains more than one operator, the
computer executes the operators according to their precedence, also known as the order
of operations. Thistable shows the precedence for the arithmetic operators.""
""When an arithmetic expression includestwo operators with the same precedence, the
computer evaluatesthe operatorsfrom left to right. For example, in the arithmetic
expression x / y * c the computer will first divide x by y and then multiply that result
by c. If you need the computer to evaluate a lower precedence operator before a higher
precedence one, you can add parenthesesto the expression to change the evaluation
order. The computer will always evaluate arithmetic that isinside parentheses first
because parentheses have the highest precedence of all the arithmetic operators.""
#Given the distance that a cable will span and the distance
#it will sag or dip in the middle, this program computes the
#length of the cable."""

span = float(input("Distance the cable mus span in meters:"))
dip = float(input("Distance the calbe will sag in meters: "))
#Use the numbers to compute the cable length.

length = span + (8 * dip**2) / (3 * span)

# Print the cable length in the
# console window for the user to see.
print(f"Length of cable in meters: {length:.2f}")




      


    


