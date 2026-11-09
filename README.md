# Proyecto Final de Programación - Análisis Dataset BMW

**Integrantes:**
- Santiago Morales (Integrante A - Ítems Impares)
- Santiago Rodríguez (Integrante B - Ítems Pares)

## Estructura del Proyecto
- `/cuadernos/`: Contiene los cuadernos de Jupyter individuales (`parte_santiago_morales.ipynb` y `parte_santiago_rodriguez.ipynb`).
- `/datos/`: Contiene el dataset original `bmw.csv`.
- `analisis.py`: Script final con la integración completa del código.

## Diccionario de Datos (`bmw.csv`)
| Columna | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `model` | Texto (string) | Modelo del vehículo (ej. 3 Series, 1 Series, X3). |
| `year` | Entero (int) | Año de fabricación del vehículo. |
| `price` | Numérico (float) | Precio de venta del vehículo (USD). |
| `transmission` | Texto (string) | Tipo de transmisión (Manual, Automatic, Semi-Auto). |
| `mileage` | Entero (int) | Millaje acumulado del vehículo. |
| `fuelType` | Texto (string) | Tipo de combustible (Petrol, Diesel, Hybrid, etc.). |
| `tax` | Entero (int) | Impuesto sobre el vehículo. |
| `mpg` | Numérico (float) | Rendimiento en millas por galón. |
| `engineSize` | Numérico (float) | Tamaño/cilindraje del motor en litros (ej. 2.0). |