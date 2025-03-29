# Consigna:

# Crear un conjunto en Python de Colores.

# Trabajaremos con el notebook de la sesión, específicamente sobre la temática de Sets.

# Crear un conjunto en Python que posea los siguientes elementos:

# Colores: Rojo, Blanco, Azul.

# Posteriormente, agrega nuestro set de colores, los valores de: Violeta y Dorado

# Elimina a los colores: Celeste, Blanco y Dorado

# Pregunta: ¿Qué pasa si queremos eliminar el color Celeste utilizando el método discard?
Colores= {"Rojo", "Blanco", "Azul"}
print (f"Su lista contiene los siguientes colores {Colores}")
Colores.add ("Violeta")
Colores.add ("Dorado")
print (f"Se agregaron los siguientes colores {Colores}")
# Colores.remove("Celeste") celeste no esta en la lista
Colores.discard("Celeste")
Colores.remove("Blanco")
Colores.remove("Dorado")

print (f"Los colores resultantes son {Colores}")
