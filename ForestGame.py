# Este es un juego para escoger en destinos desconocidos y encontrar un premio
# El juego consiste en escoger una opción binaria de tres niveles que puede llevar al premio o no.
# Se preguntará al usuario por 1 o 2 para continuar con el camino

print ("Welcome to forest game")
print("You have to input the number 1 if you choice the option one or input number 2 if you choice the option 2")
print ("you are walking in the forest and then you arrive at in intersection")
print( "you have two options: first option is path (number 1) and second option is cave")
print("if your choice path, put 1 or if your choice cave put 2")
selection_1 = int(input("What is your first option: "))


if selection_1 == 1:
    first_option = "path"
    print (f"you arrive at the {first_option}")
    print("So you have decide the second option")
    print ("Put number 1 if your choice is 'cottage' and 2 if your choice is 'bridge'")
    
    if first_option == "path":
        selection_2 = int(input("What is your second option: "))
        
        if selection_2 == 1:
            second_option = "cottage"
            print (f"you arrive at the {second_option}")
            print("So you have decide the third option")
            print ("Put number 1 if your choice is 'golden chest' and 2 if your choice is 'silver chest'")
            selection_3 = int(input("What is your third option: "))
            if selection_3 == 1:
                third_option = "golden chest"
                print(f"you arrive ath the {third_option}, I am sorry you could not win a prize")
            elif selection_3 == 2:
                third_option = "silver chest"
                print(f"you arrive ath the {third_option}, I am sorry you could not win a prize")
            else:
                print("I am sorry the number is not valid")

        elif selection_2 == 2:
            second_option = "bridge"
            print (f"you arrive at the {second_option}")
            print("So you have decide the third option")
            print ("Put number 1 if your choice is 'waterfall' and 2 if your choice is 'hill'")
            selection_3 = int(input("What is your third option"))
            if selection_3 == 1:
                third_option = "waterfall"
                print(f"you arrive at the {third_option}, I am sorry you could not win a prize")
            elif selection_3 == 2:
                third_option = "hill"
                print(f"you arrive ath the {third_option}, I am sorry you could not win a prize")
            else:
                print("I am sorry your number is not valid")


        else:
            print("I am sorry your number is not valid")
            


elif selection_1 == 2:
    first_option = "cave" 
    print (F"you arrive at the {first_option}")
    print("So you have decide the second option")
    print ("Put number 1 if your choice is 'dark tunnel' and 2 if your choice is 'ligth tunnel'")
    
    

    if first_option == "cave":
        selection_2 = int(input("What is your second option: "))
        


        if selection_2 == 1:
            second_option = "dark tunnel"
            print (F"you arrive at the {second_option}")
            print("So you have decide the third option")
            print ("Put number 1 if your choice is 'box with light' and 2 if your choice is 'flowers'")
            selection_3 = int(input("What is your third option: "))
            if selection_3 == 1:
                third_option = "box_with_light"
                print(f"you arrive ath the {third_option}, I am sorry you could not win a prize")
            elif selection_3 == 2:
                third_option = "flowers"
                print(f"you arrive ath the {third_option}, I am sorry you could not win a prize")
            else:
                print("Your number is not valid")
            


        elif selection_2 == 2:
            second_option = "ligth tunnel"
            print (F"you arrive at the {second_option}")
            print("So you have decide the third option")
            print ("Put number 1 if your choice is 'golden box' and 2 if your choice is 'wooden box'")
            selection_3 = int(input("What is your third option: "))
            if selection_3 == 1:
                third_option = "golden_box"
                print(f"you arrive ath the {third_option}, !Contratulations your are a winner!")
            elif selection_3 == 2:
                third_option = "wooden_box"
                print(f"you arrive ath the {third_option}, I am sorry you could not win a prize")
            else:
                print("Your number is not valid")

        else:
            print("I am sorry your number is not valid")
            
    

else:
    print("I am sorry your number is not valid")

