"""if Statements
In Python, we use if statementsto cause the computer to make decisions; if statements
are also called selection statements because the computerselects one group of
statementsto execute and skipsthe other group ofstatements.
There are six comparison operatorsthat we can use in an if statement:
< lessthan
<= lessthan or equal
> greater than
>= greater than or equal
== equal to
!= not equal to"""

#Example 6 contains Python code that checks if a number is greater than 500.

# Get an account balance as a number from the user.

balance = float(input("Enter the account balance:"))
# If the balance is greater than 500, then
# compute and add interest to the balance.
if balance > 500:
    interes = balance *.03
    balance += interes

# Print the balance.
print(f"Balance: {balance: .2f}")



