# Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

# Mostrar una suma de los dos números

# Mostrar una resta de los dos números (el primero menos el segundo)

# Mostrar una multiplicación de los dos números

# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará

# En caso de no introducir una opción válida, el programa informará de que no es correcta.


Numero1 = float(input("Ingrese su primer numero: "))
Numero2 = float(input("Ingrese su segundo numero: "))
while True:
    print(" \nSeleccione que desea hacer")
    print("1. Sumar los dos numeros")
    print("2. Restar los dos numeros")
    print("3. Multiplicar los dos nuemros")
    print("4. Finalizar")
    Menu = int(input("Elige una opcion: "))
    if Menu == 1:
        print(f" La suma de sus numeros es:",Numero1 + Numero2)
    elif Menu == 2:
        print(f"La resta de sus numeros es:", Numero1 - Numero2)
    elif Menu == 3:
        print(f"La multiplicacion de sus numeros es:", Numero1*Numero2)
        print("El programa se reiniciara")
    elif Menu == 4:
        print("Eligio finalizar el programa")
        break
    else:
        print("Opcion no valida")