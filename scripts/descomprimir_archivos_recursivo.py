# script that unzip files recursive of a folder
import os
import zipfile

def extract_zip_files(directory):
    # Recorre todos los archivos y subdirectorios en el directorio dado
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                zip_file_path = os.path.join(root, file)
                # Crea un directorio para extraer el contenido del archivo ZIP
                extraction_dir = os.path.splitext(zip_file_path)[0]
                os.makedirs(extraction_dir, exist_ok=True)
                # Extrae el archivo ZIP
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extraction_dir)
                print(f"Descomprimido: {zip_file_path}")
                # Borra el archivo ZIP si se desea
                # os.remove(zip_file_path) 

# Ruta del directorio raíz donde se encuentran los archivos ZIP
root_directory = os.getcwd() # toma el directorio actual
#root_directory = "/ruta/del/directorio"

# Llama a la función para descomprimir archivos ZIP de forma recursiva
extract_zip_files(root_directory)
