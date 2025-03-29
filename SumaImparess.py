# Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100: 🖐 Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

opcion = input("¿Quieres hacer la suma automáticamente (A) o manualmente (M)? (A/M): ").strip().upper()
# Sumar auto impares
if opcion == "A":

    impares = range(1, 101, 2) 
    suma = sum(impares) 
    print(f"La suma de los números impares entre 0 y 100 es: {suma}")
# Sumar manual impares
elif opcion == "M":

    suma = 0
    numero = 1 

    print("Suma de números impares. Presiona Enter sumar el siguiente número impar.")

    while numero <= 100:
        input(f"Presiona Enter para sumar el número impar {numero}.")
        suma += numero  
        print(f"Suma actual: {suma}") 
        numero += 2 

    print(f"La suma total de los números impares entre 0 y 100 es: {suma}")

else:
    print("Opción no válida. Por favor, elige 'A' para automático o 'M' para manual.")
