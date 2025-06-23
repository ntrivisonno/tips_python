# script que verificar si los vectores son LI

import numpy as np

def check_linear_independence(v1, v2, v3):
    """
    Verifica si tres vectores en R^3 son linealmente independientes.
    """
    # Crear una matriz con los vectores como filas
    matrix = np.array([v1, v2, v3])
    
    # Calcular el determinante
    determinant = np.linalg.det(matrix)
    
    # Verificar la independencia
    if np.isclose(determinant, 0):
        print("Los vectores son linealmente dependientes.")
    else:
        print("Los vectores son linealmente independientes.")

    print(f"Determinante: {determinant}")

# Ejemplo de vectores
v1 = [1, 2, 3]
v2 = [4, 5, 6]
v3 = [7, 8, 9]

check_linear_independence(v1, v2, v3)
