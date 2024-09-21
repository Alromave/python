# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
def main():
# Get the user's gender, birthdate, height, and weight.
# Call the compute_age, kg_from_lb, cm_from_in,
# body_mass_index, and basal_metabolic_rate functions
# as needed.
# Print the results for the user to see.
    gender = input("What is your gender:(M or F): ")
    birth_str = input("What is your birthdate: (YYYY-MM-DD)")
    
    pounds = float(input("What is your weight in pounds: "))
    inches = float(input("What is your height in inches: "))
    years = compute_age(birth_str)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(inches)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)
    print(f"Because your gender is: {gender}, your age is: {years}, your weight is {kg} kilogrames, your height is: {cm} centimeters, so your bmi is {bmi} and your bmr is {bmr}")

    pass



    


def compute_age(birth_str):
    """
    Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
    as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str,"%Y-%m-%d")
    today = datetime.now()
    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year
    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
         (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    return years
def kg_from_lb(pounds):

    """
    Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = 0.45359237 * pounds
    return kg

def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = 2.54 * inches
    return cm
def body_mass_index(weight, height):
    """
    Compute and return a person's body mass index.
    Parameters
    weight: a person's weight in kilograms.
    height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (1000 * weight) / height ** 2
    return bmi
def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
    weight: a person's weight in kilograms.
    height: a person's height in centimeters.
    age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    
    if gender.upper() == "F":
        bmr = 447.593 + (9.47 * weight) + (3.098 * height) - (4.330 * age)
    else:
        bmr = 88.632 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return bmr
main()






    