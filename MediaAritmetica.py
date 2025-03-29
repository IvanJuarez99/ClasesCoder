# Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.
cantidad = int(input("Ingrese la cantidad de numeros que quiere utilizar: "))
suma=0
for i in range(cantidad):
    numero= int(input(f"Ingrese el numero {i+1}: "))
    suma += numero
media = suma / cantidad
print(f" La media aritmetica de los numeros introducidos es: {media}")