import numpy as np

# Cargar datos ignorando líneas de comentarios
data = np.loadtxt('data_position_prueba2_2.txt', comments='#')

# Redondear los valores a 3 decimales
data = np.round(data, decimals=3)

# Guardar nuevamente en el mismo archivo con formato reducido
np.savetxt('data_position_prueba2_2.txt', data, fmt='%.5f', delimiter=' ')
