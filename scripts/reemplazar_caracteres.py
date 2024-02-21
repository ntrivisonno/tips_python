# script that reads a file and change wome characters

# Nombre del archivo de entrada y salida
archivo_entrada = 'delete.m'
archivo_salida = 'deletenFIXED.m'

# Abrir el archivo de entrada para lectura y el de salida para escritura
with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
    # Leer el contenido del archivo de entrada
    contenido = entrada.read()

    # Eliminar los caracteres '^M' (retorno de carro)
    contenido_sin_carro = contenido.replace('^M', '')

    # Escribir el contenido modificado en el archivo de salida
    salida.write(contenido_sin_carro)

print("Proceso completado. Los caracteres '^M' han sido eliminados.")
