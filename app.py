import numpy as np

# Array de una dimensión

vector = np.array([10, 20, 30, 40, 50, 60]) # Creamos un array de una dimensión

print("INFO DEL ARRAY -----------------------------------------------------")
print("Dimensión: ", vector.ndim)
print("Forma: ", vector.shape)
print("Cantidad de elementos: ", vector.size)
print("Tipo de dato: ", vector.dtype)

print("SLICING DEL ARRAY ---------------------------------------------------")
print("Desde indice 1 hasta 4: ", vector[1:5])
print("Desde inicio hasta indice 3: ", vector[:3])
print("Saltando de 2 en 2: ", vector[::2])