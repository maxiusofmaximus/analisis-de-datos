# Python para análisis de datos existen varias librerías. Entre esas tenemos:

# Numpy: Es una librería para realizar operaciones matemáticas y estadísticas

# Pandas: Es una librería para manipulación de los datos:
#  (Cargar datos, Limpieza de datos, Análisis Exploratorio, Análisis Descriptivo)

# Matplotlib: Es una librería para gráficas estadísticas. Ej: Histogramas, Diagramas de barras,
# Diagramas de dispersión, Diagramas de pastel, etc.

# Seaborn: Gráficos estadísticos avanzados

# Introducción a Pandas

# Importar las librerías
import pandas as pd
from tabulate import tabulate
import numpy as np
import openpyxl

# Llamar o cargar dataset CSV
df = pd.read_csv('datasets_G615/CalificacionesTXT.csv')
# print(tabulate(df))
# print(tabulate(df.head()))
# print(df.tail())
# print(df.describe())
# print(df.info())

df_nuevo = pd.read_csv('datasets_G615/CalificacionesTXT.csv')

est_programa = df_nuevo.groupby('Programa').agg({'Programa': 'count'})

# print("\nPrograma\n", tabulate(est_programa), end="\n\n")

# Cantidad de estudiantes

est_genero = df_nuevo.groupby('Genero').agg({'Genero': 'count'})

# print("\nPrograma\n", tabulate(est_genero), end="\n\n")

# Cantidad de estudiantes por programa y genero

est_programa_genero = df_nuevo.groupby(['Programa', 'Genero']).agg({'Programa': 'count'})

# print("\nPrograma\n", tabulate(est_programa_genero), end="\n\n")

# Cantidad de estudiantes que aprueban matemáticas

# aprueba_matematicas = df_nuevo['Matematicas']>=3.5
# aprueba_matematicas = aprueba_matematicas.replace({False: 'No aprobado', True: 'Aprobado'})
# estado_aprueba_matematicas = df_nuevo.groupby(aprueba_matematicas)['Matematicas'].count()

# print(estado_aprueba_matematicas)

# Operación y generación de nuevas columnas

# Reemplazamos la coma por punto y convertimos a float para que la suma funcione
df_nuevo['Promedio'] = (
    df_nuevo['Matematicas'].str.replace(',', '.').astype(float) + 
    df_nuevo['Español'].str.replace(',', '.').astype(float) + 
    df_nuevo['Ciencias'].str.replace(',', '.').astype(float) + 
    df_nuevo['Idiomas'].str.replace(',', '.').astype(float)
) / 4

# print(df_nuevo)

# Exportar el dataset a 

# Excel

# df_nuevo.to_excel('datos.xlsx', index=False)
df_nuevo.to_csv('datos.csv', index=False)

# html_table = df.to_html(classes='table table-striped table-hover table-bordered', index=False)