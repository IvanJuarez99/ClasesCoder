# Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
while True:
    numero= int(input("Por favor ingrese un numero impar: "))
    if numero % 2 !=0:
        print(f"El numero {numero} es impar")
        break
    else:
        print(f"El numero {numero} es par, intente nuevamente")
