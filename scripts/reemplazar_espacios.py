# script for changing white spaces into underscore

def reemplazar_espacios(cadena):
    nueva_cadena = cadena.replace(" ", "_")
    return nueva_cadena

# Ejemplo de uso
texto = input("Ingrese una cadena de texto: ")
resultado = reemplazar_espacios(texto)
print("Resultado:\n{}".format(resultado))

print('#--------------------------------------------')
print('\n FIN, OK!')
