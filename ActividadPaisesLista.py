# Crear un conjunto en Python que posea los siguientes elementos:

# Países: Inglaterra, USA, México.

# Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA

# Elimina a los países: Chile e Italia

# Pregunta: ¿Qué pasa si queremos eliminar al país Chile utilizando el método remove?, ¿Qué pasó con el element de USA?

# Consigna Dicts

# Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla:

# Ejemplo del output solicitado:

# Juan tiene 25 años, y vive en Carrera 7 - Bogotá
PrimerosPaises= ["Inglaterra", "USA", "Mexico"]
print(f"Su lista contiene los siguientes paises {PrimerosPaises}")
PrimerosPaises+=["Islandia", "Italia", "Argentina", "Portugal", "Chile"]
print(f"Ahora su lista contiene los siguientes pasises {PrimerosPaises}")
SegundosPaises= PrimerosPaises.pop(4)
SegundosPaises= PrimerosPaises.pop(-1)
print(f" Asi queda su lista despues de elimiar los paises de Chile e Italia {PrimerosPaises}")