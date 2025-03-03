# numerador = 10
# denominador = 0
# cadena = "3"
# numerico = 5
# print(numerador/denominador)
# print(cadena + numerico)

#error 1 ZeroDivisionError
#error 2 TypeError

# try :
#     print(numerador/denominador)
# except ZeroDivisionError:
#     print("Ha ocurrdido una division entre cero")

# try:
#     print(cadena + numerico)
# except TypeError:
#     print("Ha ocurrdido un error de tipo")
# print("fin del programa")

# try:
#     print( 10/ 0)
# except TypeError:
#     print("Ha ocurrdio un error de tipo")
# except:
#     print("Ha ocurrido un error desconocido")
#############################################################
while True:
    try:
        dividendo= int(input("Ingrese el dividendo: "))
        divisor= int(input("Ingrese el divisor: "))
        print("El resultado es: ", dividendo / divisor)
        break
    except ValueError:
        print("Debe ingresar un numero")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
print("Fin del programa")
    



