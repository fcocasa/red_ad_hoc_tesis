import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()  # Habilitar modo interactivo

def plot_robot(ax, x, y, z, x_0, y_0, trajectory, radius=5):
    """Dibuja la posición del robot, la trayectoria y muestra 'z'."""
    ax.clear()  # Limpiar el gráfico para actualizar
    ax.set_xlim(x_0-50, x_0+50)  # Ajustar los límites según la escala real
    ax.set_ylim(y_0-50, y_0+50)
#    ax.set_title(f"Tiempo: {t:.2f} s")  # Mostrar tiempo en el título
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)  # Agregar grilla

    # Dibujar la trayectoria hasta el punto actual
    ax.plot(trajectory[:, 0], trajectory[:, 1], 'b-', linewidth=1.5, alpha=0.7)

    # Dibujar el robot en su posición actual
    robot_circle = plt.Circle((x, y), radius, color='c', fill=True)
    ax.add_patch(robot_circle)

    # Mostrar el valor de 'z' al lado del robot
    ax.text(x + 5, y + 5, f"z={z:.2f}", fontsize=12, color='black')

    plt.draw()
    plt.pause(0.0001)  # Pausa corta para suavizar la animación


def interpolate_path(x_vals, y_vals, z_vals, num_interpolaciones=5):
    """Interpolación para suavizar el movimiento del robot."""
    x_interp, y_interp, z_interp = [], [], []#, []

    for i in range(len(x_vals) - 1):
        for j in np.linspace(0, 1, num_interpolaciones):
            x_interp.append((1 - j) * x_vals[i] + j * x_vals[i + 1])
            y_interp.append((1 - j) * y_vals[i] + j * y_vals[i + 1])
            z_interp.append((1 - j) * z_vals[i] + j * z_vals[i + 1])
#            t_interp.append((1 - j) * t_vals[i] + j * t_vals[i + 1])

    return np.array(x_interp), np.array(y_interp), np.array(z_interp)#, np.array(t_interp)


# Cargar datos del archivo
data = np.loadtxt('data_position_prueba2_2.txt', comments='#')  # Archivo con formato (t, x, y, z)
#t_vals, 
x_vals, y_vals, z_vals = data[:, 0], data[:, 1], data[:, 2]#, data[:, 3]

# Suavizar movimiento interpolando puntos intermedios
#x_vals, y_vals, z_vals, t_vals = interpolate_path(x_vals, y_vals, z_vals, t_vals)

# Inicializar la figura
fig, ax = plt.subplots()
trajectory = np.zeros((0, 2))  # Para almacenar la trayectoria

# Animar la trayectoria del robot
#t_prev = 0
x0, y0 = x_vals[0], y_vals[0]
for x, y, z in zip(x_vals, y_vals, z_vals):
    #time.sleep(t-t_prev)  # Simular tiempo real
    time.sleep(0.01)
    trajectory = np.vstack((trajectory, [x, y]))  # Agregar nueva posición
    plot_robot(ax, x, y, z, x0, y0, trajectory)  # Dibujar robot en la nueva posición
    #t_prev = t

plt.ioff()  # Desactivar modo interactivo
plt.show()  # Mantener el gráfico al final

