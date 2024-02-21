# script that finds words in a file, and show the line where it appears.
# Convert all strings to lowercase to avoid upper/lowercase sensitivity
# TODO, diferenciar espacios zhou= z hou
import os

def buscar_cadena_en_archivo(archivo, cadena_a_buscar):
    try:
        # Obtener el directorio del archivo
        directorio_archivo = os.path.dirname(archivo)

        if not os.path.isfile(archivo):
            print(f"Error: El archivo '{archivo}' no es un archivo válido.")
            return

        cadena_a_buscar = cadena_a_buscar.lower()  # Convertir la cadena de búsqueda a minúsculas

        encontrado = False  # Variable para rastrear si se encontró la cadena

        with open(archivo, 'r') as archivo_abierto:
            contenido = archivo_abierto.readlines()

            for num_linea, linea in enumerate(contenido, start=1):
                linea_minusculas = linea.lower()  # Convertir la línea a minúsculas
                if cadena_a_buscar in linea_minusculas:
                    print(f"La cadena '{cadena_a_buscar}' fue encontrada en el archivo.")
                    print(f"Se encuentra en el renglón {num_linea}.")
                    encontrado = True

        if not encontrado:
            print(f"La cadena '{cadena_a_buscar}' no fue encontrada en el archivo.")

        print(f"Directorio del archivo: {directorio_archivo}")

    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejemplo de uso
nombre_archivo = '/home/zeeburg/MEGAshared/DynaMesh/Bibliography/resumen_paper.org'  # Sin la barra al final
cadena_a_buscar = 'dynamic mod'  # Reemplaza con la cadena que deseas buscar

buscar_cadena_en_archivo(nombre_archivo, cadena_a_buscar)
