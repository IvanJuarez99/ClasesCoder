# Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras. Realiza los siguientes puntos usando las funciones integradas ya vistas y el método slice [ : ] Imprime la lista correspondiente luego de cada punto.

# Añade a la lista_1 el <int> 456789 y luego el <str> "Hola Mundo"
# Luego añade a la lista_2 el <str> "Hola y adiós", y luego el <int> 5555
# Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento
# Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento
# Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3
lista_1= [1, 12, 123]
lista_2= ["bye","Ciao","Agur","Adieu"]
lista_1.append(456789)
lista_1.append("Hola Mundo")
lista_2.append("Hola y Adios")
lista_2.append(5555)
lista_3 = lista_1
lista_3.pop()
print(f"Lista 3 {lista_3}")
lista_4 = lista_2
lista_4.pop(0)
lista_4.pop()
print(f"Lista 4 {lista_4}")
lista_5 = lista_4 + lista_3
print (f"Lista 5 {lista_5}")
