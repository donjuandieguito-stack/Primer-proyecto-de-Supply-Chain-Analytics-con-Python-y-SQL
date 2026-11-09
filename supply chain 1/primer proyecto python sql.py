import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 0. Configuración inicial de estilos para portafolio
sns.set_theme(style="whitegrid")
os.makedirs("graficas_logistica", exist_ok=True)

print("--- CARGANDO DATASET DE SUPPLY CHAIN ---")

# Ruta exacta y blindada hacia tu archivo en Descargas
ruta_csv = "supply_chain_data.csv"
try:
  df = pd.read_csv(ruta_csv)
  print(
      "✅ ¡Archivo CSV cargado exitosamente! Total de registros:"
      f" {len(df)}\n"
  )
except FileNotFoundError:
  print(
      "❌ Error: No se encontró el archivo en la ruta de Descargas. Revisa que"
      " se llame 'supply_chain_data.csv'."
  )
  exit()

# 1. KPIs Generales de Ingeniería Industrial
print("--- 1. INDICADORES CLAVE (KPIs) ---")
print(f"• Total de SKUs analizados: {len(df)}")
print(f"• Costo de envío promedio: ${df['Shipping costs'].mean():.2f}")
print(f"• Tiempo de entrega promedio (Lead Time): {df['Lead times'].mean():.1f} días")
print(f"• Tasa de defectos promedio en calidad: {df['Defect rates'].mean():.2f}%")
print("\n")

print("--- 2. ANALIZANDO COSTOS POR TRANSPORTISTA (CARRIER) ---")
# Agrupar por transportista para ver cuál es más costoso o eficiente
analisis_transporte = (
    df.groupby("Shipping carriers")
    .agg({"Shipping costs": "mean", "Lead times": "mean", "SKU": "count"})
    .rename(columns={"SKU": "Total_Productos"})
)
print(analisis_transporte)
print("\n")

print("--- 3. GENERANDO GRÁFICA GERENCIAL DE COSTOS VS TIEMPOS ---")
# Crear una visualización avanzada para el portafolio
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Lead times",
    y="Shipping costs",
    hue="Shipping carriers",
    style="Product type",
    s=100,
    palette="deep",
)

plt.title(
    "Relación: Tiempos de Entrega vs Costos de Envío por Transportista",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Tiempo de Entrega (Lead Time - Días)", fontsize=11)
plt.ylabel("Costo de Envío ($)", fontsize=11)
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

# Guardar la gráfica en la carpeta
ruta_img = "graficas_logistica/costos_vs_tiempos.png"
plt.tight_layout()
plt.savefig(ruta_img, dpi=300)
plt.show()

print(f"✅ ¡Gráfica avanzada guardada exitosamente en '{ruta_img}'!")