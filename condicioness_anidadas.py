print("======")
print("Bienvenidos al programa de conversión")
print("======\n")

print("Este programa le permite convertir un numero a letra y letra a número \n")
print("Escriba 1 si quiere convertir un número y 2 si quiere convertir una palabra \n")

opcion = int(input("Elija su opción: "))
if opcion == 1:
    numero  = int(input("Cuál es el número que quieres convertir: "))
    if numero == 1:
        print("el número es uno")
    elif numero == 2:
        print( "el número es dos")
    
    elif numero == 3:
        print( "el número es tres")
    elif numero == 4:
        print( "el número es tres")
    elif numero == 5:
        print( "el número es tres")
    else:
        print("su número no es posible convertir")
elif opcion == 2:
    letra = input("Cual es el número (en letras) que desea convertir: ")
    letra_minuscula = letra.lower()
    if letra_minuscula == "uno":
        print("El número es 1")
    elif letra_minuscula == "dos":
        print("el número es 2")
    elif letra_minuscula == "tres":
        print("el número es 3")
    elif letra_minuscula == "cuatro":
        print("el número es 4")
    elif letra_minuscula == "cinco":
        print("el número es 5")
    else:
        print("Su número no se puede convertir")
else:
    print("Esta opción no está disponible \n")
print("Muchas gracias")


