# A partir de una lista realizar las siguientes tareas sin modificar la lista original:

# Borrar los elementos duplicados

# Ordenar la lista de mayor a menor

# Eliminar todos los números impares ( for ---- if (%2==1) ---- pop, remove )

# Realizar una suma de todos los números que quedan (sum(lista))

# Añadir como primer elemento de la lista la suma realizada insert(0, suma)

# Devolver la lista modificada

# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

# lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
ListaSinDuplicados = lista
ListaSinDuplicados = list(set(lista))
print(f"La lista sin numeros duplicados es la siguiente: {ListaSinDuplicados}")
ListaSinDuplicados.sort(reverse=True)
print(f"La lista ordenada de mayor a menor queda de la siguiente forma: {ListaSinDuplicados}")
ListaSinDuplicados = [numero for numero in ListaSinDuplicados if numero %2==0]
print(f"La lista sin numeros impares es la siguiente: {ListaSinDuplicados}")
SumaDeLista=(sum(ListaSinDuplicados))
print (f"La lista sumada da el siguiente resultado: {SumaDeLista}")
ListaSinDuplicados.insert(0, SumaDeLista)
print(f"La lista con la suma como primer elemento es la siguiente: {ListaSinDuplicados}")
print(f"La suma de {ListaSinDuplicados[1:]} es igual a {SumaDeLista}")
print(f"La lista original no se ve afectada {lista}")