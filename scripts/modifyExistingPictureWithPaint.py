# -*- coding: utf-8 -*-
"""
Script that open a files with n *.png frames in kolourpaint, allowing any
change. Each picture is opened an once the changed is made, you close the 
file and automatically the next is opened. This is repeated until the end.
If the output file already exist, the program is cancel so there is no
overwritten files. The opened files were saved this way -> frame_0131.png

@author: ntrivisonno
@date: JUL2025
"""

import os
import subprocess
import sys
import time

tStart = time.time()

# Carpetas
carpeta_origen = "./frames_tagged"
carpeta_destino = "./frames_tagged_twoCirclesAAA"
numberFiles = 1870
delta = 5 # increment of the frames

# Si la carpeta destino ya existe, abortar
if os.path.exists(carpeta_destino):
    print(f"❌ La carpeta destino ya existe: {carpeta_destino}")
    print("🛑 Abortar para no sobrescribir archivos existentes.")
    sys.exit(1)

# Crear carpeta destino
os.makedirs(carpeta_destino)
print(f"📁 Carpeta destino creada: {carpeta_destino}")

# Bucle para abrir imágenes una por una
for i in range(0, numberFiles, delta):
    nombre_archivo = f"frame_{i:04d}.png"
    ruta_origen = os.path.join(carpeta_origen, nombre_archivo)
    ruta_destino = os.path.join(carpeta_destino, nombre_archivo)

    if os.path.exists(ruta_origen):
        # Copiar archivo a la carpeta destino
        subprocess.run(["cp", ruta_origen, ruta_destino])
        
        print(f"\n🖼️ Abriendo {nombre_archivo} para editar...")
        print("💾 Guardá los cambios y cerrá kolourpaint para continuar.")
        
        # Abrir imagen copiada y esperar que se cierre kolourpaint
        subprocess.run(["kolourpaint", ruta_destino])
    else:
        print(f"⚠️ Archivo no encontrado: {nombre_archivo}")

print("\n✅ Todas las imágenes han sido procesadas exitosamente.")

endTime = time.time()
elapse = endTime - tStart
print('#--------------------------------------------')
print(f'FIN, OK! - time = {elapse}')
