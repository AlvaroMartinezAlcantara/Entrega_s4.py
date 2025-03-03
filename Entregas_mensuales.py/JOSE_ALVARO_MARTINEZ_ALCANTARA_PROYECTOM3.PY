"""
Importamos las librerias NUMPY Y MATPLOTLIB y le asignamos un alias para facilitar su uso al ser llamados
"""
#Usamos la libreria numpy para generar datos aleatoriamente 
import numpy as np
#Usamos la libreria matplotlib para graficar los datos
import matplotlib.pyplot as plt
# Definimos la funcion para las 3000 canicas para doce niveles.
def maquina_galton(n_canicas=3000, n_niveles=12):
#Usamos np.zeros para que en los contenedores inicen de cero así como int. para contar canicas enteras
    contenedores = np.zeros(n_niveles + 1, dtype=int)
# Usamos un ciclo for para contar las n_canicas
    for _ in range(n_canicas):
#generamos una lista de valores aleatorios donde 0 es a la izquierda y 1 es a la derecha
        posicion = sum(np.random.choice([0, 1], size=n_niveles)) 
#Registramos el conteo de donde han caido las canicas
        contenedores[posicion] += 1
    
    return contenedores

"""
 Grafica el histograma de distribución de las canicas en los contenedores.
 """
#Definimos la funcion para graficar los resultados
def graficar_histograma(contenedores):
# Creamos un histograma con los datos obtenidos   
    plt.hist(range(len(contenedores)), bins=len(contenedores), weights=contenedores, color='dodgerblue',)
#Asignamos nombre al eje x
    plt.xlabel('Posición del Contenedor')
#Asignamos nombre al eje y
    plt.ylabel('Cantidad de Canicas')
#Asigamos el nombre al histograma 
    plt.title('Máquina de Galton')
#Mandamos mostrar el grafico
    plt.show()

# Ejecuta la actividad y grafica los resultados
contenedores = maquina_galton()
graficar_histograma(contenedores)