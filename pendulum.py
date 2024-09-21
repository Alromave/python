# 01 Class Activity: Review Python
"""Write a Python program that getsinput from a user, uses variables, performs arithmetic
using the math module, and displaysresultsfor the user to see."""

#Problem Statement
"""The time in seconds that a pendulum takesto swing back and forth once is given by this
formula:"""
#t = 2π square root of:  h/9.81

"""t isthe time in seconds,
π isthe constant PI, which isthe ratio of the circumference of a circle divided by its
diameter (use math.pi),
h is the length of the pendulum in meters."""

#Activity
"""Write a program named pendulum.py that prompts a user to enter the length of a
pendulum in meters and then computes and printsthe time in secondsthat it takesfor
that pendulum to swing back and forth. To start your program, copy and paste the
following code into your program and use it as an outline as you write code. Note that in
a Python program, a triple quoted string at the top of the file acts as a comment for the
entire program."""

"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
____
/ h
t = 2π / ----
√ 9.81
t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.
Write a program that prompts a user to enter the length of a
Helpful Documentation
The prepare content for thislesson explains how to write code to do the
following:
Get input from a user
Convert user input from a string to a number
Calculate results
Display resultsfor the user to see
The Python math module contains mathematical constants and functions
including math.pi and math.sqrt().
Testing Procedure
Verify that your program works correctly by following each step in thistesting
procedure:
1. Run your program and enter the inputshown below. Ensure that your
program's output matchesthe output below.
> python pendulum.py
Length of pendulum (meters): 1.5
Time (seconds): 2.46
Sample Solution
Please work diligently with your classto complete this activity. After classis over,
please compare your approach to the sample solution. Please do not look at the
sample solution until you have either finished the program or diligently worked with
your class.
Ponder
During this assignment, you wrote a Python program that getsinput from a user,
uses variables, performs arithmetic, and displaysresultsfor the user to see. Because
you should have learned how to write thistype of program in CSE 110, this
assignmentshould have been fairly easy for you. If this assignment was difficult for
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""
# pendulum exercise
import math


h = float(input("What is the length of a pendulum:"))

pi = math.pi
t = (2 * pi) * (math.sqrt(h / 9.8))
print (f" the time (in seconds) is: {t:.2f}")





