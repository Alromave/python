#01 Prove Milestone: Review Python
#Purpose
"""Prove that you can write a Python program that gets input from a user, performs
arithmetic, and displays results for the user to see."""

#Problem Statement

"""The size of a car tire in the United States is represented with three numbers like this:
205/60R15. The first number is the width of the tire in millimeters. The second number is
the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits.
The volume of space inside a tire can be approximated with this formula:"""

"""v = π w2 a(w a + 2,540 d) / 10,000,000,000
v isthe volume in liters,
π isthe constant PI, which isthe ratio of the circumference of a circle divided by its
diameter (use math.pi),
w isthe width of the tire in millimeters,
a isthe aspect ratio of the tire, and
d isthe diameter of the wheel in inches."""

#Assignment
#Write a Python program named tire_volume.py that reads from the keyboard the three
#numbers for a tire and computes and outputs the volume of space inside that tire.
import math

w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): " ))
d = int (input("Enter the diameter of the wheel in inches (ex 15):"))
v = (math.pi  * (w**2) * a * ((w * a) + (2540 * d))) / (10000000000)
print(f"The approximate volume is {v: .2f} liters ")


#Problem Statement
"""
Many companies wish to understand the needs and wants of their customers more
deeply so the company can create productsthat fill those needs and wants. One way to
understand customers more deeply isto record the values entered by customers while
they are using a program and then to analyze those values. One common way to record
valuesisfor a program to store them in a file.
"""

#Assignment
"""
The previous lesson's prove milestone required you to write a program named
tire_volume.py that computesthe approximate volume of air inside a tire. Add code
near the end of that program that doesthe following:
Getsthe current date from the computer's operating system.
2. Opens a text file named volumes.txt for appending.
3. Appendsto the end of the volumes.txt file one line of text that containsthe
following five values:
a. current date
b. width of the tire
c. aspect ratio of the tire
d. diameter of the wheel
e. volume of the tire


"""
# current date
from datetime import datetime
currentDay = datetime.now()
print(f"{currentDay:%Y-%m-%d}")

# Open a text file named cities.txt in append mode.
with open("volumes.txt", "at") as volumes_file:
# Print a city's name and information to the file.
    print(currentDay, file=volumes_file)
    print(f"{currentDay}, {w}, {a,} {d}, {v}", file=volumes_file)




