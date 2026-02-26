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

# Llamar o cargar dataset CSV
df = pd.read_csv('datasets_G615/CalificacionesTXT.csv')
print(tabulate(df))
print(tabulate(df.head()))
print(df.tail())
print(df.describe())
print(df.info())