Clave=("123*")
Usuario=("Cisco")
print("******Menu******")
print("1. Retiro")
print("2. Saldo")
print("3. Consignacion")
respuesta1=(str(input("Ingrese su usuario")))
respuesta2=(str(input("ingrese su clave")))
if (Clave==respuesta2) and (Usuario==respuesta1):
    print("Bienvenido, su usuario y contraseña son correctos")
else:
    print("Su usuario o contraseña son incorrectos") 