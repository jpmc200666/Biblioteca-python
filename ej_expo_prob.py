import random
import matplotlib.pyplot as plt

# Simulación
lanzamientos = 10000
resultados = []

for _ in range(lanzamientos):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    resultados.append(dado1 + dado2)

# Valores posibles
sumas = list(range(2, 13))
frecuencias = [resultados.count(s) for s in sumas]

# Probabilidades experimentales
probabilidades = [resultados.count(s) / lanzamientos for s in sumas]

# ======================
# Diagrama de líneas
# ======================
plt.figure()
plt.plot(sumas, probabilidades, marker='o')
plt.title("Distribución de probabilidad de la suma de dos dados")
plt.xlabel("Suma de los dados")
plt.ylabel("Probabilidad")
plt.grid(True)
plt.show()

# ======================
# Diagrama de barras
# ======================
plt.figure()
plt.bar(sumas, frecuencias)
plt.title("Diagrama de barras: suma de dos dados")
plt.xlabel("Suma")
plt.ylabel("Frecuencia")
plt.show()
