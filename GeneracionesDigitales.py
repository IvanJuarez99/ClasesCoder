# generacion silenciosa 1920-1940
# generacion boomer 1946-1964
# generacion x 1965-1979
# generacion y 1980-2000
# generacion z 2001-2010
Año = int(input("Ingrese el año que quiera corroborar: "))
if Año >=1920 and Año <=1940:
    print(f"Su año es {Año}, Es de la generacion Sileciosa")
elif Año >=1946 and Año <=1964:
    print(f"Su año es {Año}, Es de la generacion Boomer")
elif Año >=1965 and Año <=1979:
    print(f"Su año es {Año}, Es de la generacion X")
elif Año >=1980 and Año <=2000:
    print (f"Su año es {Año}, Es de la generacion Y")
elif Año >=2001 and Año <=2010:
    print(f"Su año es {Año}, Es de la generacion Z")
else:
    print("No pertence a ninguna generacion")