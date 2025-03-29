# Descripción de la actividad. 
# A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:

# El último ítem de tupla
# El número de ítems de tupla
# La posición donde se encuentra el ítem 87 de tupla
# Una lista con los últimos tres ítems de tupla
# Un ítem que haya en la posición 8 de tupla
# El número de veces que el ítem 7 aparece en tupla

# Copia esta tupla para iniciar el ejercicio:
# tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)
print(f"El ultimo item de la tupla es: {tupla[-1]}")
print(f"El numero de items en la tupla es: {len(tupla)}")
print(f"La posicion donde se encuentra el item 87 es: {tupla.index(87)}")
print(f"La lista con los ultimos tres items de la tupla {list(tupla[-3:])}")
print(f"El item en la posicion 8 de la tupla es: {tupla[8]}")
print(f"El numero de veces que aparece el item 7 es: {tupla.count(7)}")
