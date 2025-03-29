#Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno
#Extraer la nota y almacenarla en una variable llamada nota.
#Extraer la materia y almacenarla en una variable llamada materia.
#Mostrar por pantalla la siguiente estructura: NOMBRE APELLIDO ha sacado un NOTA en MATERIA
#cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena = "acitametaM ,5.8 ,otipeP ordeP"
cadena_al_revez = cadena [::-1]
Nombre = cadena_al_revez[:12]
Nota = cadena_al_revez[14:17]
materia = cadena_al_revez[19:]
print(f"{Nombre} ha sacado un {Nota} en {materia}")