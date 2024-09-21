# Example 1 Lesson 3
import math
# Define a function named print_cylinder_volume.

def print_cylinder_volume():
    """Compute and print the volume of a cylinder.
    Parameters: none
    Return: nothing
    """
    # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cilynder: "))
    height = float(input("Enter the height of a cylinder: "))
    # Compute the volume of the cylinder.
    volume = math.pi * radius * height 

    # Print the volume of the cylinder.

    print(f"Volume: {volume: .2f}")
print_cylinder_volume()

# Example 2
def print_cylinder_volume1(radius1, height1):
    """Compute and print the volume of a cylinder.
    Parameters
    radius1: the radius of the cylinder
    height1: the height of the cylinder
    Return: nothing
    """
    # Compute the volume of the cylinder.
    volume1 = math.pi * radius1 * height1
    # Print the volume of the cylinder.
    print (volume1)

print_cylinder_volume1(1,2)

# Example 3
# Define a function named computer_cylinder_volume.
def print_cylinder_volume2(radius2,height2):
    """Compute and return the volume of a cylinder.
    Parameters
    radius: the radius of the cylinder
    height: the height of the cylinder
    Return: the volume of the cylinder
    """
    # Compute the volume of the cylinder.
    volume2 = math.pi * radius2 * height2
    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    return volume2

volume2 = print_cylinder_volume2(5,6)
print(volume2)

# Example 4
# the main- User Defined Function
"""
In all previous Python programsthat you wrote in CSE 110 and 111, you wrote statements
that were not in a function like the simple program in example 4
# Example 4
import math
# Get the radius and height from the user.
radius = float(input("Enter the radius of a cylinder: "))
height = float(input("Enter the height of a cylinder: "))
# Compute the volume of the cylinder.
volume = math.pi * radius**2 * height
# Print the volume of the cylinder.
print(f"Volume: {volume:.2f}"
"""
"""
Writing statements outside a function can lead to poor organization within a large
program. Professionalsoftware developers write statementsinside a function whenever
possible. Beginning with thislesson, you will write nearly allstatementsinside a userdefined function. Also, in each program, you will write a user-defined function named
main, which will contain the beginning statements of the program. In addition, in each
program you will write one or more user-defined functionsthat have parameteters,
perform calculations and other useful work, and return a result to the call point.
Example 5 containsthe same Python program as example 4 except most of the
statements are inside a user-defined function named main
"""
# Example 5
import math
# Define a function named main.
def main():
    # # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cylinder"))
    height = float(input("Enter the height of a cylinder"))

    # compute the volume of the cylinder
    volume = math.pi * radius**2 * height
    
    # print the volume of the cylinder
    print(f"Volume: {volume: .2f}")
# Start this program by
# calling the main function.
main()







