"""
%@author: ntrivisonno
   
script for bifurcation diagram or logistic map
"""
# script que levanta todo los nombres (carpeta y archivos) de un directorio y filtra los paso del tiempo de una corrida de OF
import os
import csv


# Ruta del directorio
directorio = "./"  # Reemplaza esto con la ruta correcta

# Lista para almacenar los pasos de tiempo
pasos_de_tiempo = []

# Recorre el directorio
for entrada in os.listdir(directorio):
    ruta_completa = os.path.join(directorio, entrada)

    # Verifica si es un directorio y tiene un formato num�rico (podr�a ser un paso de tiempo)
    if os.path.isdir(ruta_completa) and entrada.replace(".", "", 1).isdigit():
        pasos_de_tiempo.append(float(entrada))  # Convierte a tipo float

# Ordena la lista de pasos de tiempo
pasos_de_tiempo.sort()

# Imprime la lista resultante
print(pasos_de_tiempo)
print(f'Se guardaron los pasos de tiempo en la variable: "pasos_de_tiempo"')

# write csv file
nombreArchivo = 'tiempoOF_csv'
ruta_csv = os.path.join(os.getcwd(), nombreArchivo)
with open(ruta_csv, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Pasos de Tiempo'])  # Escribir encabezado
    for paso_tiempo in pasos_de_tiempo:
        escritor_csv.writerow([paso_tiempo])

print('#--------------------------------------------')
print('\n FIN, OK!')

plt.show()
