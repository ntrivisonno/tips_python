'''
import pandas as pd

# Crear un diccionario con datos de ejemplo
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

# Crear una multicolumna con tres columnas
multi_columns = pd.MultiIndex.from_tuples([('Grupo 1', 'Columna 1'),
                                           ('Grupo 1', 'Columna 2'),
                                           ('Grupo 2', 'Columna 3')])

# Crear un DataFrame a partir del diccionario y la multicolumna
df = pd.DataFrame(data, columns=multi_columns)

# Mostrar el DataFrame
print(df)
'''
'''
import pandas as pd

# Definir los nombres de grupos y columnas como listas separadas
nombres_grupos = ['Grupo 1', 'Grupo 1', 'Grupo 2']
nombres_columnas = ['Columna 1', 'Columna 2', 'Columna 3']

# Crear una multicolumna con los nombres de grupos y columnas
multi_columns = pd.MultiIndex.from_tuples(list(zip(nombres_grupos, nombres_columnas)))

# Crear un DataFrame con la multicolumna
df = pd.DataFrame(columns=multi_columns)

# Definir los datos como listas
datos = {
    ('Grupo 1', 'Columna 1'): [1, 2, 3],
    ('Grupo 1', 'Columna 2'): [4, 5, 6],
    ('Grupo 2', 'Columna 3'): [7, 8, 9]
}

# Agregar datos al DataFrame
df = df.append(datos, ignore_index=True)

# Mostrar el DataFrame
print(df)
'''
import pandas as pd

# Definir los datos
data = {
    ('Reynolds 100', 'cd'): [1.33, 1.35, 1.38, 1.31, 1.33, 1.36, 1.35, 1.34],
    ('Reynolds 100', 'cd_std'): [0.32, 0.014, 0.007, 0.04, 0.04, 0.015, 0.012, 0.011],
    ('Reynolds 100', 'cl'): ['± 0.32', '±0.300', '±0.322', '±0.65', '±0.68', '±0.25', '±0.339', '±0.315'],
    ('Reynolds 100', 'St'): [0.165, 0.1751, 0.169, 0.20, 0.196, 1.40, 0.164, 0.164]
}

# Crear un DataFrame
df = pd.DataFrame(data, index=['Kim et al.[11]', 'Calhoun[27]', 'Russell and Wang[28]',
                                'Rosenfeld et al.[29]', 'Wright and Smith[30]', 'Braza et al.[31]',
                                'Liu et al.[32]', 'Present (second-order)'])

# Mostrar el DataFrame
print(df)


# para acceder a alg'un valor:
#$print(df.loc[df.index[0],('Reynolds 100','cd')])

# para incorporar un rengl'on nuevo
#df.loc['Nuevo index', ('Reynolds 100','cd')]=100
