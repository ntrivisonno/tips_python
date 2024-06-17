'''
Diagrama de Gantt 
fecha inicio, final y duración de proyecto todo a pata

@author: ntrivisonno
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Definir la fecha de inicio del proyecto
fecha_inicio_proyecto = datetime.strptime('2024-05-08', '%Y-%m-%d')

# Definir los datos de las actividades y su estado de avance en un diccionario anidado
data = {
    'Relevamiento en planta': {
        'Inicio': '2024-06-10',
        'Fin': '2024-06-10',
        'Progreso': 100
    },
    'Modelado 3D': {
        'Inicio': fecha_inicio_proyecto,
        'Fin': '2024-06-20',
        'Progreso': 75
    },
    'Setteo de simulaciones': {
        'Inicio': '2024-05-08',
        'Fin': '2024-06-20',
        'Progreso': 80
    },
    'Simulación Silo A': {
        'Inicio': '2024-06-20',
        'Fin': '2024-06-25',
        'Progreso': 0
    },
    'Simulación Silo 1': {
        'Inicio': '2024-06-20',
        'Fin': '2024-06-25',
        'Progreso': 0
    },
    'Simulación Silo 2': {
        'Inicio': '2024-06-20',
        'Fin': '2024-06-25',
        'Progreso': 0
    },
    'Simulación Homogeneizador': {
        'Inicio': '2024-06-20',
        'Fin': '2024-06-25',
        'Progreso': 0
    },
    'Post-proceso y análisis': {
        'Inicio': '2024-06-10',
        'Fin': '2024-07-18',
        'Progreso': 0
    }
}

# Calcular la duración de cada tarea y convertir fechas de inicio y fin a strings
for task in data:
    if isinstance(data[task]['Inicio'], datetime):
        inicio = data[task]['Inicio']
        data[task]['Inicio'] = inicio.strftime('%Y-%m-%d')
    else:
        inicio = datetime.strptime(data[task]['Inicio'], '%Y-%m-%d')
        
    if isinstance(data[task]['Fin'], datetime):
        fin = data[task]['Fin']
        data[task]['Fin'] = fin.strftime('%Y-%m-%d')
    else:
        fin = datetime.strptime(data[task]['Fin'], '%Y-%m-%d')
        
    duracion = (fin - inicio).days + 1  # +1 para incluir el día de fin
    data[task]['Duración'] = duracion

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Mostrar el DataFrame para verificar
print(df)

# Función para dibujar la línea vertical indicando la fecha actual
def draw_today_line(ax):
    today = datetime.today()
    ax.axvline(today, color='red', linestyle='--', label='Hoy')
    ax.text(today, ax.get_ylim()[1], 'Hoy', color='red', ha='center', va='bottom')

# Crear el gráfico de Gantt
fig, ax = plt.subplots(figsize=(10, 6))

# Configuración del gráfico
y_pos = np.arange(len(df.columns))
start_dates = [datetime.strptime(df[task]['Inicio'], '%Y-%m-%d') for task in df.columns]
end_dates = [datetime.strptime(df[task]['Fin'], '%Y-%m-%d') for task in df.columns]
durations = [df[task]['Duración'] for task in df.columns]
progresses = [df[task]['Progreso'] / 100 for task in df.columns]

# Dibujar las barras del gráfico de Gantt
for i, (start_date, duration, progress) in enumerate(zip(start_dates, durations, progresses)):
    ax.barh(i, duration, left=start_date, color='skyblue', edgecolor='black')
    ax.barh(i, duration * progress, left=start_date, color='green', edgecolor='black')

# Configuración del eje y
ax.set_yticks(y_pos)
ax.set_yticklabels(df.columns)
ax.invert_yaxis()  # Las tareas más recientes arriba

# Configuración del eje x
ax.set_xlabel('Fecha')
ax.xaxis_date()

# Dibujar la línea vertical indicando la fecha actual
draw_today_line(ax)

# Leyenda
ax.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
