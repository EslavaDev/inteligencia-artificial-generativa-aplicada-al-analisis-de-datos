import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Gestión de errores de importación
try:
    from ctgan import CTGAN
except ImportError:
    print("Advertencia: CTGAN no está instalado. Se usarán datos sintéticos simulados.")
    CTGAN = None

#Creación del dataset original
data = pd.DataFrame({
    "edad": [28, 34, 45, 39, 31, 50, 29, 41, 36, 48],
    "ingresos_mensuales": [2200, 2800, 3200, 2900, 2500, 3500, 2400, 3000, 2700, 3400],
    "pais": ["ES", "ES", "DE", "FR", "IT", "DE", "ES", "FR", "IT", "DE"],
    "tipo_cliente": [
        "nuevo", "fidelizado", "fidelizado", "nuevo", "nuevo",
        "fidelizado", "nuevo", "fidelizado", "nuevo", "fidelizado"
    ],
    "num_productos": [1, 2, 3, 2, 1, 4, 1, 2, 2, 3]
})

print("=== Datos originales (Head) ===")
print(data.head())

#Configuración

categorical_columns = ["pais", "tipo_cliente"]
np.random.seed(42)

#Generación de datos sintéticos

if CTGAN is not None:
    print("\nEntrenando modelo CTGAN...")
    model = CTGAN(epochs=300, verbose=False)
    model.fit(data, discrete_columns=categorical_columns)
    synthetic_data = model.sample(10)
else:
    print("\nUsando datos sintéticos simulados para visualización")

    synthetic_data = data.copy()
    synthetic_data["edad"] = synthetic_data["edad"] + np.random.randint(-3, 4, size=len(data))
    synthetic_data["ingresos_mensuales"] = synthetic_data["ingresos_mensuales"] * np.random.uniform(
        0.9, 1.1, size=len(data)
    )

print("\n=== Datos sintéticos generados ===")
print(synthetic_data)

#Visualización comparativa
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Scatterplot: Edad vs Ingresos
sns.scatterplot(
    data=data,
    x="edad",
    y="ingresos_mensuales",
    label="Reales",
    ax=axes[0]
)
sns.scatterplot(
    data=synthetic_data,
    x="edad",
    y="ingresos_mensuales",
    label="Sintéticos",
    marker="X",
    ax=axes[0]
)
axes[0].set_title("Relación Edad vs Ingresos")
axes[0].legend()

#Histograma de ingresos
sns.histplot(
    data["ingresos_mensuales"],
    kde=True,
    stat="density",
    alpha=0.4,
    label="Reales",
    ax=axes[1]
)
sns.histplot(
    synthetic_data["ingresos_mensuales"],
    kde=True,
    stat="density",
    alpha=0.4,
    label="Sintéticos",
    ax=axes[1]
)
axes[1].set_title("Distribución de Ingresos (Histograma)")
axes[1].legend()

plt.tight_layout()
plt.show()

#Estadísticas comparativas

print("\n=== Validación Estadística ===")
print(f"Media Edad     -> Real: {data['edad'].mean():.2f} | Sintético: {synthetic_data['edad'].mean():.2f}")
print(f"Std Dev Edad   -> Real: {data['edad'].std():.2f}  | Sintético: {synthetic_data['edad'].std():.2f}")

diff_ingresos = (
    abs(data["ingresos_mensuales"].mean() - synthetic_data["ingresos_mensuales"].mean())
    / data["ingresos_mensuales"].mean()
    * 100
)
print(f"Diferencia % en media de Ingresos: {diff_ingresos:.2f}%")
