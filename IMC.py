print("Para determinar su IMC, favor de completar el siguiente formulario :")
nombre=input("Introduce tu nombre: ")
apellido_paterno=input("Introduce tu apellido Paterno: ")
apellido_materno=input("Introduce tu apellido Materno: ")
peso=float(input("Introduce tu peso en Kilogramos: "))
edad=int(input("Introduce tu edad: "))
estatura=float(input("Introduce tu estatura en metros"))
IMC = peso / estatura**2

print("Nombre: " + nombre)
print("Apellido Paterno: " + apellido_paterno)
print("Apellido Materno: "+ apellido_materno)
print("Peso: "+ str(peso) + "kilogramos")
print("Estatura: "+ str(estatura) + "metros")
print("Edad: " + str(edad) + "años")
print("IMC: " + str(IMC) )
