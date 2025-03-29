# Realizar una función llamada año_bisiesto:

# Recibirá un año por parámetro

# Imprimirá “El año año es bisiesto” si el año es bisiesto

# Imprimirá “El año año no es bisiesto” si el año no es bisiesto

# Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

# Información a tener en cuenta:

# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. 
# Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

def año_bisiesto():
    while True:
        año_entrada = input("Ingrese el año: ")
# verificar si es solo solo numero
        if año_entrada.isdigit():
# convertir a entero
            año_entrada = int(año_entrada)
# multiplo de 4 resto 0, multiplo de 100 resto diferente a 0,o multiplo de 400 resto 0
            if (año_entrada % 4 == 0 and año_entrada % 100 != 0) or (año_entrada % 400 == 0):
                print(f"Su año {año_entrada} es bisiesto.")
            else:
                print(f"Su año {año_entrada} no es bisiesto.")
        else:
            print("La entrada no es un numero o tiene decimales o es negativo, intente nuevamente ingresando un numero entero")

año_bisiesto()