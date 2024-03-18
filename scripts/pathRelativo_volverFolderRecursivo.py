# scripts that go back 'n' folder in relative path
import os
import sys

def add_parent_directories(num_levels):
    # Obtenemos el directorio actual
    current_directory = os.getcwd()

    # Retrocedemos num_levels veces
    for _ in range(num_levels):
        current_directory = os.path.dirname(current_directory)

    # Agregamos la ruta de la carpeta anterior al sys.path
    sys.path.append(current_directory)

    # Mostramos la ruta agregada al sys.path
    print(f"Ruta agregada al sys.path: {current_directory}")

# Número de niveles que queremos retroceder
num_levels_back = 2  # Cambia a la cantidad deseada de niveles

# Llamamos a la función para agregar los directorios
add_parent_directories(num_levels_back)
