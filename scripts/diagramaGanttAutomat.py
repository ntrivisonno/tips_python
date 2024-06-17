'''
Diagrama de Gantt con fecha inicio, final y duración de proyecto
Tareas fechadas en función de N días desde comienzo

@author: ntrivisonno
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Definir la fecha de inicio y final del proyecto
fecha_inicio_proyecto = datetime.strptime('2024-05-08', '%Y-%m-%d') # Generan OC - Orden de Compra
fecha_final_proyecto = datetime.strptime('2024-07-18', '%Y-%m-%d')
duracion_total = (fecha_final_proyecto - fecha_inicio_proyecto).days + 1

# Definir los datos de las actividades y su estado de avance en un diccionario anidado
data = {
    'Relevamiento en planta': {
        'Inicio': '2024-06-10',
        'Fin': '2024-06-10',
        'Progreso': 100
    },
    'Modelado 3D': {
        'Inicio': fecha_inicio_proyecto,
        'Fin': fecha_inicio_proyecto + timedelta(days=10),
        'Progreso': 75
    },
    'Setteo de simulaciones': {
        #'Inicio':  fecha_inicio_proyecto + timedelta(days=5),
        'Inicio':  fecha_inicio_proyecto,
        'Fin': '2024-06-18',
        'Progreso': 90
    },
    'Simulación Silo A': {
        'Inicio': '2024-06-19',
        'Fin': fecha_final_proyecto-timedelta(days=10),
        'Progreso': 0
    },
    'Simulación Silo 1': {
        'Inicio': '2024-06-19',
        'Fin': fecha_final_proyecto-timedelta(days=10),
        'Progreso': 0
    },
    'Simulación Silo 2': {
        'Inicio': '2024-06-19',
        'Fin': fecha_final_proyecto-timedelta(days=10),
        'Progreso': 0
    },
    'Simulación Homogeneizador': {
        'Inicio': '2024-06-19',
        'Fin': fecha_final_proyecto-timedelta(days=10),
        'Progreso': 0
    },
    'Post-proceso y análisis': {
        'Inicio': fecha_inicio_proyecto+timedelta(days=50),
        'Fin': fecha_final_proyecto,
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
fig, ax = plt.subplots(figsize=(12, 8))

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
ax.set_xlim(fecha_inicio_proyecto, fecha_final_proyecto)
ax.set_xlabel('Fecha')
ax.xaxis_date()

# Añadir el segundo eje x para los días desde el inicio del proyecto
ax2 = ax.twiny()

# Ajustar los límites del nuevo eje x para que coincidan con el eje de las fechas
ax2.set_xlim(ax.get_xlim())

# Crear las etiquetas para el segundo eje x cada 10 días
date_range = pd.date_range(start=fecha_inicio_proyecto, end=fecha_final_proyecto)
days_since_start = [(date - fecha_inicio_proyecto).days for date in date_range]
ticks = date_range[::10]
tick_labels = [str((tick - fecha_inicio_proyecto).days) for tick in ticks]
ax2.set_xticks(ticks)
ax2.set_xticklabels(tick_labels)

ax2.set_xlabel('Días desde el inicio del proyecto')

# Dibujar la línea vertical indicando la fecha actual
draw_today_line(ax)

# Añadir un recuadro con la fecha de inicio y final del proyecto
textstr = f'Fecha de inicio: {fecha_inicio_proyecto.strftime("%Y-%m-%d")}\nFecha de final: {fecha_final_proyecto.strftime("%Y-%m-%d")}\nDuración: {duracion_total} días'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.15, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# Leyenda
ax.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.savefig('diagramaGantt.pdf')
print('#--------------------------------------------')
print('\n FIN, OK!')

plt.show()
