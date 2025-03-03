# consumo de API, usando la pokeapi

import requests
url = "https://pokeapi.co/api/v2/pokemon/charmander"

try : 
    respuesta = requests.get(url, timeout=10)
except requests.Timeout:
    print("Error: El tiempo de espera ha finalizado")

if respuesta.status_code !=200 :
    print("Pokemón encontrado")
else:
    print(respuesta)

datos = respuesta.json()
nombre = datos["name"]

print("Movimientos de " + nombre + ' :')

movimientos= datos["moves"]
for i in range(int(len(movimientos))) :
    movimiento = movimientos[i]["move"]["name"]
    print(movimiento)


