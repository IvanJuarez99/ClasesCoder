Partidos_Totales = 20
Partidos_Ganados = int(input("Ingrese la cantidad de partidos ganados "))
Partidos_Empatados = int(input("Ingrese la cantidad de partidos empatados "))
Partidos_Perdidos = int(input("Ingrese la cantidad de partidos perdidos "))
Partidos_Ganados = Partidos_Ganados * 2
Partidos_Empatados = Partidos_Empatados * 1
Partidos_Perdidos = Partidos_Perdidos * 0

promedio = (Partidos_Ganados + Partidos_Empatados	+ Partidos_Perdidos) / Partidos_Totales

print(f"El promedio final de los equipos de futbol es {promedio}")