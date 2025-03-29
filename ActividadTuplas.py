# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

# 🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

# Partirás de:

# matriz = [

# [1, 5, 1],

# [2, 1, 2],

# [3, 0, 1],

# [1, 4, 4]

# ]

# Debes llegar a:

# matriz = [

# [1, 5, 1, 7],

# [2, 1, 2, 5],

# [3, 0, 1, 4],

# [1, 4, 4, 9]

# ]

matriz = [

[1, 5, 1],

[2, 1, 2],

[3, 0, 1],

[1, 4, 4]

]
lista0=matriz[0]
lista1=matriz[1]
lista2=matriz[2]
lista3=matriz[3]
matriz[0].append(sum(lista0))
matriz[1].append(sum(lista1))
matriz[2].append(sum(lista2))
matriz[3].append(sum(lista3))
print(f"La nueva matriz es la siguiente {matriz}")

