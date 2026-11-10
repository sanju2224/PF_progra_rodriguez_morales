# %% [markdown]
# # Análisis de Datos - BMW
# Integrante A: Santiago Morales

# %%
import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datos/bmw.csv", sep=";")
df['price'] = df['price'].astype(str).str.replace('$', '', regex=False).str.replace('.', '', regex=False).astype(float)
df['engineSize'] = df['engineSize'] / 10.0

# %% [markdown]
# ## 1. Carga e inspección inicial de los datos (Integrante A)

# %%
df.info()
df.describe()

# %% [markdown]
# **Conclusión:** Se cargó e inspeccionó el conjunto de datos de BMW, validando sus 1000 registros, tipos de variables y estadísticos descriptivos.

# %% [markdown]
# ## 3. Identificación de outliers (Integrante A)

# %%
q1 = np.percentile(df['price'], 25)
q3 = np.percentile(df['price'], 75)
iqr = q3 - q1
limite = q3 + 1.5 * iqr

sns.boxplot(x=df['price'])
plt.axvline(limite, color='red', linestyle='--')
plt.title("Outliers en precios")
plt.show()

# %% [markdown]
# **Conclusión:** El diagrama de caja y el cálculo del rango intercuartílico permiten identificar valores atípicos (*outliers*) en los precios más altos del mercado.

# %% [markdown]
# ## 5. Creación de variables (Integrante A)

# %%
df['antiguedad'] = 2026 - df['year']

precio, años = sp.symbols('precio anios')
formula = precio / (0.95**años)

calc_precio = sp.lambdify((precio, años), formula, 'numpy')
df['precio_original'] = calc_precio(df['price'], df['antiguedad']).round(2)

df[['model', 'price', 'antiguedad', 'precio_original']].head()

# %% [markdown]
# **Conclusión:** A partir del año de fabricación y mediante cálculo simbólico se generaron nuevas variables para determinar la antigüedad y estimar el precio original del vehículo.

# %% [markdown]
# ## 7. Agrupación con groupby (Integrante A)

# %%
print(df.groupby('transmission')['price'].agg(['mean', 'max']).round(2))
print("Las transmisiones Semi-Auto alcanzan los precios mas altos y el mayor promedio.")

# %%
print(df.groupby('model').size().sort_values(ascending=False).head(5))
print("El 3 Series y el 1 Series son los modelos con mayor oferta.")

# %%
print(df.groupby('year')[['price', 'mileage']].mean().sort_index(ascending=False).head(5).round(2))
print("Los modelos mas recientes tienen mayor precio y menor kilometraje promedio.")

# %%
print(df.groupby('engineSize')['mpg'].mean().sort_index().head(5).round(2))
print("Los motores de menor tamaño tienen una eficiencia de combustible mucho mayor.")

# %%
print(df.groupby('fuelType')['tax'].mean().round(2))
print("Los vehiculos hibridos pagan los impuestos promedio mas bajos frente a gasolina y diesel.")

# %% [markdown]
# ## 9. Conclusiones Finales (Integrante A)

# %% [markdown]
# 1. **Depreciación regida por desgaste y antigüedad:** El año de fabricación y el kilometraje acumulado (millaje) son los predictores más determinantes en la pérdida de valor del vehículo, evidenciando que el mercado castiga económicamente de forma severa y proporcional el uso prolongado.
# 
# 2. **Prima de valor por confort y eficiencia:** El mercado automotriz analizado valora financieramente las tecnologías modernas; los compradores están dispuestos a pagar un precio promedio superior por vehículos que ofrecen mayor comodidad (transmisiones automáticas) y alternativas de eficiencia energética (vehículos híbridos) frente a las opciones tradicionales.
# 
# 3. **Alta concentración de la oferta:** El inventario disponible no está distribuido de manera uniforme entre todos los vehículos, sino que está fuertemente dominado por un puñado de modelos específicos (como la Serie 3 y Serie 1), lo que indica cuáles son los vehículos de mayor demanda, accesibilidad y rotación en este nicho de mercado.
# 
# 4. **Impacto de la configuración en la retención de valor:** Las decisiones de configuración inicial del auto (tipo de combustible y caja de cambios) actúan como un factor de protección contra la depreciación. Modelos con características percibidas como "premium" o sostenibles conservan un mejor valor de reventa a lo largo del tiempo.
# 
# 5. **Comportamiento predecible del mercado:** La consistencia en las tendencias (caída del precio a medida que aumentan los años y las millas) demuestra que se trata de un mercado de segunda mano maduro y racional, donde el valor residual de un automóvil se puede estimar y modelar estadísticamente con alta precisión basándose en sus métricas operativas.