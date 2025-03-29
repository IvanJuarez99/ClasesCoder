# cliente mayor de edad
# antiguedad de 3 años
# ingreso de 2500 dolare
# si no tiene antiguedad tiene que ingresar 4000 dolares
edad=18
antiguedad=2
ingreso=1500

# Edad=int(input("Ingrese La edad del cliente: "))
# Antiguedad=int(input("Ingrese su antiguedad: "))
# Ingreso=int(input("Ingrese sus ingresos: "))
if edad < 18:
    print("El cliente no tiene la edad suficiente")
if antiguedad < 3:
    print("No es apto por antiguedad, debe corroborar su ingreso")
elif ingreso > 4000:
    print ("El ingreso si es suficiente, credito aprovado")
elif:
    print("Ingreso no suficiente")
elif ingreso < 2500:
    print ("El ingreso no es suficiente")
else:
    print("Credito aprobado")    
