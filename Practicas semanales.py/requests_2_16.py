
import requests
latitud = 20.1594163
longitud = -99.8909955

api_key = "83d24a4fc4b781d8794c82e43f195eb8"

url_destino = f'http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&lang=es&appid={api_key}'

respuesta = requests.get(url_destino)

if respuesta.status_code != 200 :
    print("Ha ocurrido un error. Intenta nuevamente")
    exit()
datos = respuesta.json()
ciudad = datos["name"]

datos_clima = datos["weather"]
clima = datos_clima[0]["description"]

print(f"El clima en {ciudad} es {clima}")




