# Más allá de los decoradores standards, se pueden crear decoradores personalizados.

def mi_decorador(func):
    def envoltura(*args, **kwargs):
        print("Algo se ejecuta antes de la función.")
        resultado = func(*args, **kwargs)
        print("Algo se ejecuta después de la función.")
        return resultado
    return envoltura

@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Mundo")


'''
#Salida CON decorador:
$run decorador_personalizado.py
Algo se ejecuta antes de la función.
Hola, Mundo!
Algo se ejecuta después de la función.

#Salida SIN decorador:
$run decorador_personalizado.py
Hola, Mundo!

'''
