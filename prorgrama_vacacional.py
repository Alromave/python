print("Programa vacacional")

print("Este programa permite saber el día de vacaciones por departamento")

print("Bienvenido al programa de vacaciones")
nombre = input("Cuál es tu nombre: ")
clave = int(input("Cuál es el número de clave de tu departamento: "))
if clave >= 1 and clave <= 3:
    antiguedad= float(input("Cuántos años tienes de servicio: "))

    if clave == 1:
    
        if antiguedad == 1:
            dias = 6

        elif antiguedad <= 6:
            dias = 14
        else:
            dias = 20

   

    elif clave == 2:
 
        if antiguedad == 1:
            dias = 7
        elif antiguedad <= 6:
            dias = 15
        else:
            dias = 25

    elif clave == 3:
 
        if antiguedad == 1:
            dias = 10
        elif antiguedad <= 6:
            dias = 25
        else:
            dias = 30
    print(f"{nombre} tienes derecho a {dias} dias de vacaciones")
else:
    print("El número de clave es incorrecto")
 




