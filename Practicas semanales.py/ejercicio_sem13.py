while True:
    nombre = input("Introduce tu nombre :")
    apellido = input("Introduce tu apellido: ")
    if nombre == "":
        print("No haz introducido tu nombre: ")
    elif apellido == "":
        print("No haz introducido tu apellido: ")
    else:
        break

while True:
    try:
        edad = int(input("introduce tu edad"))
        break
    except ValueError:
        print("Debes introducir un numero")

correo = input("Introduce tu correo: ")

while True:
    try:
        telefono = input("Introduce tu teléfono: ")
        int(telefono)
        break
    except ValueError:
        print("Debes introducir un numero: ")

print("Nombre:" + nombre)
print("Apellido:" + apellido)
print("Tengo " + str(edad) + "años")
print("Correo: " + correo)
print("Telefono: " + telefono)