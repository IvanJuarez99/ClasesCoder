# # NOTA: COMO NO VIMOS FUNCIONES, CADA EJERCICIO QUE DIGA ESCRIBIR UNA FUNCION CREAN UN ARCHIVO QUE HAGA LO QUE PIDE EL ENUNCIADO.
# # ES DECIR, EL EJERCICIO 6.5 SI QUIEREN QUE SE LOS CORRIJA ME PASARAN 3 ARCHIVOS, 6_5_PuntoA, 6_5_PuntoB, etc..
# # NOTA 2: DONDE DICE DEVUELVA, HAGAN UN PRINT() PORQUE TAMPOCO VIMOS RETURN.
# """
# Ejercicio 9.2. Diccionarios usados para contar.
#     a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
#         de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace
#         hoy" debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
#     b) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
#         realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
#         dados. Determinar que el dado se tira un minimo de 3 veces.
# Nota: utilizar el módulo random para obtener tiradas aleatorias.
# import random

# # Simular una tirada de un dado de 6 caras
# tirada_dado = random.randint(1, 6)
# print(tirada_dado)
# """

# # Punto A: cadena_1 = "El gato negro corre por el jardín y el perro negro ladra en el jardín." cadena_2 = "La casa grande tiene un jardín grande y una piscina grande."

cadena_1= "El gato negro corre por el jardín y el perro negro ladra en el jardín ."
cadena_split= cadena_1.split()
print (cadena_split)
diccionario= {}
for palabra in cadena_split:
    palabra = palabra.lower()
    if palabra in diccionario:
       diccionario[palabra] =diccionario.get(palabra, 0)+1
    else :
         diccionario[palabra]=1
print(diccionario)

# //////////////////////////////////////////////////////////////////////////////////////////////////// #

# import random
# tirada_dado= random.randint(1,6)
# tirada_dado2= random.randint(1,6)
# print (tirada_dado)
# print(tirada_dado2)
# print(tirada_dado+tirada_dado2)
