#01 Checkpoint: Review Python
"""Write a Python program that gets input from a user, uses variables, performs arithmetic,
and displays results for the user to seePurpose"""

#Problem Statement
"""When you physically exercise to strengthen your heart, you should maintain your heart
rate within a range for at least 20 minutes. To find that range,subtract your age from 220.
This difference is your maximum heart rate per minute. Your heartsimply will not beat
faster than this maximum (220 − age). When exercising to strengthen your heart, you
should keep your heart rate between 65% and 85% of your heart's maximum rate."""

#Assignment

"""Write a Python program named heart_rate.py that asksfor a person's age and
computes and outputsthe slowest and fastest rates necessary to strengthen his heart. To
start your program, copy and paste the following code into your program and use it as an
outline as you write code. Note that in a Python program, a triple quoted string at the top
of the file acts as a comment for the entire program."""

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
print("Welcome to heart_rate exercise:")
name = input("What is your name: ")
age = int(input("Please enter your age: "))
max = 220 - age
slow_hear_rate = 0.65 * max
fast_heart_rate = 0.85 *  max
print(f" {name} When you exercise to strengthen your heart, you should keep your heart rate between \n {slow_hear_rate: .0f} and {fast_heart_rate: .0f} beats per minute.")




