#This excercise is to choice the bigger number
# the program ask you for three numbers
# then the program will display the bigger number 

number_one = int(input("What is the first number; "))
number_two = int(input("What si the second nomber: "))
number_three = int(input("What is the third number:"))

if number_one > number_two and number_one > number_three:
    print(f"The bigger number is {number_one}")
elif number_two > number_three:
    print(f"The bigger number is {number_two}")   
else:
    print(f"The bigger number is {number_three}") 

