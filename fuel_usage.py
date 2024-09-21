# Get an odometer value in U.S. miles from the user.
# Get another odometer value in U.S. miles from the user.
# Get a fuel amount in U.S. gallons from the user.
# Call the miles_per_gallon function and store
# the result in a variable named mpg.
# Call the lp100k_from_mpg function to convert the
# miles per gallon to liters per 100 kilometers and
# store the result in a variable named lp100k.
# Display the results for the user to see.
#
def main():
    val_1 = float(input("What is the first value in your odometer? "))

    val_2 = float(input("What is the second value in your odometer? "))
    fuel_amont = float(input("What is the fuel amount?"))
    mpg = miles_per_gallon(val_1, val_2, fuel_amont)
    lp100k = lp100k_from_mpg(mpg)
    print(f" If your odometer started in {val_1} miles and finished in {val_2} miles  and your spent {fuel_amont} gallons, your fuel eficiency is {mpg:.2f} or in liters {lp100k:.2f}"
          )
    pass
def miles_per_gallon(val_1, val_2, fuel_amont):
    mpg = (val_2 - val_1)/fuel_amont
    return mpg
def lp100k_from_mpg(mpg):
    lp100k = 235.215/mpg
    return lp100k
    
main()



