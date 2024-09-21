"""
If you look closely at the code in examples1 and 5, you will realize that both programs
have the same problem, namely both the print_cylinder_volume function in example 1
and the main function in example 5 are not reusable because both of them get input from
a user and print to a terminal window. A better way to write the program in examples1

and 5 isto separate the program into two functions, one named main and one named
compute_cylinder_volume asshown in example 6.
Example 6 contains a complete program with two functions, the first named main at
line 6 and the second named compute_cylinder_volume at line 20. At line 13, the main
function callsthe compute_cylinder_volume function. Notice that the
compute_cylinder_volume function getsitsinput through parameters and returns a
result which makesthisfunction reusable in other programs, including programsthat
run automatically without a user.
"""
# Example 6
import math
# define the  main function
def main ():
    # Get a radius and a height from the user.
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    # Call the compute_cylinder_volume function and store
    # its return value in a variable to use later.
    volume = compute_cylinder_volume(radius, height)
    # Print the volume of the cylinder.
    print(f"Volume: {volume: .2f}")

# Define a function that accepts two parameters.
def compute_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder.
    Parameters
    radius: the radius of the cylinder
    height: the height of the cylinder
    Return: the volume of the cylinder
    """ 
    # Compute the volume of the cylinder.
    volume = math.pi *  radius**2 * height
    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    # The returned result will be available wherever
    # this function was called.
    return volume
# Start this program by
# calling the main function.

main()
"""
The most reusable functions are onesthat have parameters, perform calculations, and
return a result but do not perform user input and output. In the previous code example,
there are two functions named main and compute_cylinder_volume. The main function is
certainly useful in the program, but it is not reusable in other programs because it gets
user input and printsthe result for the user to see. The compute_cylinder_volume
function is very reusable in another program because it doesn't get user input or print
output. Instead, it takestwo parameters, performs a calculation, and returns a result to
the calling function. The compute_cylinder_volume function isso reusable that it could
be included in a library of functionsthat compute the area and volume of 2-D and 3-D
geometric shapes.
"""
"""
What Happens When the Computer Calls a Function?
Some students have trouble visualizing what happens when the computer calls
(executes) a function. The following diagram containsthe same program as example 6.
The circled numbersshow the order in which the events happen in the computer. The
green numbers and arrowsin the diagram show the order in which the computer
executesstatementsin the program. The blue numbers and arrowsshow how data flows
from argumentsinto parameters and from a returned result to a variable
"""





