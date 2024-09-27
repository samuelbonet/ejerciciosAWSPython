import seaborn as sns
import matplotlib.pyplot as plt

# Crear datos
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Crear el gráfico de líneas con Seaborn
sns.lineplot(x=x, y=y)

# Mostrar el gráfico
plt.show()

# Guardar el gráfico como un archivo PNG
plt.savefig("grafico.png")
