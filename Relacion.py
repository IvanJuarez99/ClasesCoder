# Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
# Si el primer número es mayor que el segundo, debe devolver 1.

# Si el primer número es menor que el segundo, debe devolver -1.

# Si ambos números son iguales, debe devolver un 0.


# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(numero1, numero2):
    if numero1 > numero2:
        return 1
    elif numero1 < numero2:
        return -1
    else :
        return 0
print(f"El primer numero es 5 y le segundo 10, devolucion: ",relacion(5, 10)) 
print(f"El primer numero es 10 y el segundo 5, devolucion: ",relacion(10, 5))
print(f"El primer numero es 5 y el segundo es 5, devolucion: ",relacion(5, 5))