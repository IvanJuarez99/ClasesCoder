# Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]

# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

# 🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))
lista_0_10 = list(range(0,11))
print("Numeros del 0 al 10:", lista_0_10)
lista_neg10_0 = list(range(-10,1))
print("Numeros del -10 al 0", lista_neg10_0)
lista_0_20 = list(range(0,21,2))
print("Numeros pares de 0 a 20", lista_0_20)
lista_neg20_0 = list(range(-19,1,2))
print("Numeros impares de -20 a 0", lista_neg20_0)
lista_mult_5 = list(range(0,51,5))
print("Numeros multiplos de 5 de 0 a 50", lista_mult_5)