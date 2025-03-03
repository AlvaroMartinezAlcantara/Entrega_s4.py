#Importamos las librerias necesarias
import requests # liberia para pedir informacion HTTP
import os # libreria para manejar carpetas y archivos
import json # Libreria para guardar archivos en un formato json

#Definimos una funcion 
def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}" # Url de la API con el nombre del pokemon en minusculas para evitar errores de entrada del usuario
    response = requests.get(url) #Hacer la solicitud a la api para obetener los datos
    
    if response.status_code == 200: # Verifica si la respuesta es exitosa
        datos = response.json() #Convierte la respueta en formato json
        #Diccionario para obtener la informacion del pokemon
        informacion_pokemon = {
            "nombre": datos["name"], # Obtiene el nombre 
             "peso": datos["weight"] / 10, # peso del pokemon en kilogramos
            "altura": datos["height"] / 10, #  altura del pokemon en metros
            "movimientos": [mov["move"]["name"] for mov in datos["moves"]], #obtenemos el nombre de todos sus movimientos
            "habilidades": [hab["ability"]["name"] for hab in datos["abilities"]], # Obtenemos el nombre de las habilidades
            "tipos": [tipo["type"]["name"] for tipo in datos["types"]], #Obtenemos los tipo de pokemon
            "imagen": datos["sprites"]["front_default"] #obtenemos la imagen del pokemon
        }
        return informacion_pokemon #retornamos la informacion del pokemon en un diccionario
    else:
        return None # Retornar None si el pokemon no existe o hay un error

def guardar_en_json(nombre_pokemon, datos):
    carpeta = "pokedex" #Nombre de la carpeta donde se guardara la informcion json
    if not os.path.exists(carpeta): #Verificar si la carpeta existe
        os.makedirs(carpeta) # Crear la carpeta sino existe
    
    ruta_archivo = os.path.join(carpeta, f"{nombre_pokemon}.json") #Construir la carpeta de archivo json
    with open(ruta_archivo, "w", encoding="utf-8") as archivo: #abre el archivo en modo escritura 
        json.dump(datos, archivo, indent=4, ensure_ascii=False) #Guarda el archivo en formato jason
    print(f"Datos de {nombre_pokemon} guardados en {ruta_archivo}") # Mensaje de confirmacion

def main():
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ") #Solicita al usuario el nombre del pokemon que desee
    datos_pokemon = obtener_datos_pokemon(nombre_pokemon) #Se obtiene la informacion desde la api
    
    if datos_pokemon:
        print("\nInformación del Pokémon:") #se imprime la informacion del pokemon
        print(json.dumps(datos_pokemon, indent=4, ensure_ascii=False))#se imprime la informacion en formato json 
        guardar_en_json(nombre_pokemon, datos_pokemon) #Guarda la informacion en un formato json
    else:
        print("Error: Pokémon no encontrado. Asegúrate de escribir el nombre correctamente.") #Se imprime un mensaje de error si el nombre del pokemon no se encontro

if __name__ == "__main__": # Comprobar si el script se esta ejecutando directamente
    main()  # Llamar a la funcion principal para iniciar el programa