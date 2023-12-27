# Script that computes specific method and atributes of a class
"""

@author: ntrivisonno
"""
'''
Outputs:
- metodos: todos los métodos de la clase/instancias. Incluidos los standards
- atributos: todos los atributos de la clase/instancias. Incluidos los standards
- metodos filtrados: métodos ad-hoc de la clase/instancias.
- atributos filtrados: atributos ad-hoc de la clase/instancias.
'''

import os


# Crear una instancia de la clase
objeto = MiClase() # Colocar nombre del objeto

try :
    objeto = MiClase()
    if not isinstance (objeto, MiClase):
        raise Exception(f"Debes asignar la clase a la variable objeto\nobjeto=MiClase()")
except Exception as e:
    print(e)

# Obtener todos los nombres disponibles en la clase
nombres = dir(objeto)

# Filtrar para mostrar solo los métodos
metodos = [nombre for nombre in nombres if callable(getattr(objeto, nombre))]

# Filtrar para mostrar solo los atributos (variables)
atributos = [nombre for nombre in nombres if not callable(getattr(objeto, nombre))]

print("Métodos:", metodos)
print("Atributos:", atributos)

# Si se quieren filtrar los métodos y atributos mágicos/especiales
metodos_filtrados = [nombre for nombre in metodos if not nombre.startswith('__')]
atributos_filtrados = [nombre for nombre in atributos if not nombre.startswith('__')]

print("Métodos filtrados:", metodos_filtrados)
print("Atributos filtrados:", atributos_filtrados)

