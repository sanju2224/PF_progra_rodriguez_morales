import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. Carga e inspección inicial (Integrante A)
# ==========================================
df = pd.read_csv("datos/bmw.csv", sep=";")

print("--- INFORMACIÓN DEL DATAFRAME ---")
df.info()
print("\n--- ESTADÍSTICOS DESCRIPTIVOS ---")
print(df.describe())

# ==========================================
# 2. Limpieza y validación inicial (Punto 2)
# ==========================================
df['price'] = df['price'].astype(str).str.replace('$', '', regex=False).str.replace('.', '', regex=False).astype(float)
df['engineSize'] = df['engineSize'] / 10.0

print("\n--- VALORES NULOS Y DUPLICADOS ---")
print("Valores nulos por columna:")
print(df.isnull().sum())
print("Total de registros duplicados:", df.duplicated().sum())

# Visualización: Mapa de calor de valores faltantes
plt.figure(figsize=(8, 5))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Mapa de calor de valores faltantes")
plt.show()

# ==========================================
# 3. Identificación de outliers (Integrante A - Punto 3)
# ==========================================
q1 = np.percentile(df['price'], 25)
q3 = np.percentile(df['price'], 75)
iqr = q3 - q1
limite = q3 + 1.5 * iqr

plt.figure(figsize=(8, 4))
sns.boxplot(x=df['price'])
plt.axvline(limite, color='red', linestyle='--', label=f'Límite Outlier: {limite:.2f}')
plt.title("Outliers en precios")
plt.legend()
plt.show()

# ==========================================
# 4. Normalización y duplicados (Punto 4)
# ==========================================
df['model'] = df['model'].astype(str).str.strip()
df['transmission'] = df['transmission'].astype(str).str.strip()
df['fuelType'] = df['fuelType'].astype(str).str.strip()

# Eliminación de registros duplicados
df = df.drop_duplicates()

# ==========================================
# 5. Creación de variables (Integrante A - Punto 5)
# ==========================================
df['antiguedad'] = 2026 - df['year']

precio, anios = sp.symbols('precio anios')
formula = precio / (0.95**anios)
calc_precio = sp.lambdify((precio, anios), formula, 'numpy')
df['precio_original'] = calc_precio(df['price'], df['antiguedad']).round(2)

print("\nMuestra de variables creadas (antigüedad y precio original):")
print(df[['model', 'price', 'antiguedad', 'precio_original']].head())

# ==========================================
# 6. Consultas y filtros específicos (Punto 6)
# ==========================================
r1 = df[(df['transmission'] == 'Automatic') & (df['price'] > 50000)].shape[0]
r2 = df[(df['year'] == 2020) & (df['mileage'] < 5000)].shape[0]
r3 = df[df['engineSize'] >= 3.0].shape[0]
r4 = df[(df['fuelType'] == 'Diesel') & (df['model'] == '1 Series')].shape[0]
r5 = df[df['price'] < 10000].shape[0]

print("\n--- Resultados de Consultas (Punto 6) ---")
print("1. Autos automáticos de más de $50,000:", r1)
print("2. Autos 2020 con menos de 5,000 millas:", r2)
print("3. Autos con motor de 3.0L o superior:", r3)
print("4. Autos Serie 1 con motor Diesel:", r4)
print("5. Autos económicos por debajo de $10,000:", r5)

# ==========================================
# 7. Agrupación con groupby (Integrante A - Punto 7)
# ==========================================
print("\n--- Análisis por Transmisión ---")
print(df.groupby('transmission')['price'].agg(['mean', 'max']).round(2))
print("Conclusión: Las transmisiones Semi-Auto alcanzan los precios mas altos y el mayor promedio.")

print("\n--- Modelos con mayor oferta ---")
print(df.groupby('model').size().sort_values(ascending=False).head(5))
print("Conclusión: El 3 Series y el 1 Series son los modelos con mayor oferta.")

print("\n--- Promedio por Año de Fabricación ---")
print(df.groupby('year')[['price', 'mileage']].mean().sort_index(ascending=False).head(5).round(2))
print("Conclusión: Los modelos mas recientes tienen mayor precio y menor kilometraje promedio.")

print("\n--- Eficiencia (mpg) por Tamaño de Motor ---")
print(df.groupby('engineSize')['mpg'].mean().sort_index().head(5).round(2))
print("Conclusión: Los motores de menor tamaño tienen una eficiencia de combustible mucho mayor.")

print("\n--- Impuestos Promedio por Tipo de Combustible ---")
print(df.groupby('fuelType')['tax'].mean().round(2))
print("Conclusión: Los vehiculos hibridos pagan los impuestos promedio mas bajos frente a gasolina y diesel.")

# ==========================================
# 9. Conclusiones Finales (Integrante A)
# ==========================================
print("\n" + "="*50)
print("9. CONCLUSIONES FINALES DEL ANÁLISIS")
print("="*50)
print("1. Depreciación regida por desgaste y antigüedad: El año de fabricación y el kilometraje acumulado son los predictores más determinantes en la pérdida de valor.")
print("2. Prima de valor por confort y eficiencia: Se paga un precio superior por transmisiones automáticas y alternativas de eficiencia energética.")
print("3. Alta concentración de la oferta: El inventario disponible está fuertemente dominado por modelos específicos como la Serie 3 y Serie 1.")
print("4. Impacto de la configuración en la retención de valor: Características premium o sostenibles protegen mejor el valor de reventa a lo largo del tiempo.")
print("5. Comportamiento predecible del mercado: Se confirma como un mercado de segunda mano maduro y racional.")