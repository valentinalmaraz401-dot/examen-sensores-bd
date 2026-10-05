import os
import pandas as pd

# Definición de rutas relativas obligatorias
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "sensores_industriales.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "alertas.csv")

def ejecutar_analisis():
    if not os.path.exists(CSV_PATH):
        print(f"Error: No se encontró el archivo de datos en {CSV_PATH}")
        return

    # Cargar el dataset
    df = pd.read_csv(CSV_PATH)

    print("=== RESULTADOS DEL ANÁLISIS DE SENSORES INDUSTRIALES ===")

    # 1. Cantidad de registros y de sensores distintos (1 pto)
    total_registros = len(df)
    sensores_unicos = df["id_sensor"].nunique()
    print(f"1. Total de registros: {total_registros:,}")
    print(f"   Sensores únicos identificados: {sensores_unicos}")

    # 2. Temperatura promedio de cada planta (2 ptos)
    print("\n2. Temperatura promedio por planta:")
    temp_promedio = df.groupby("planta")["temperatura_c"].mean()
    for planta, promedio in temp_promedio.items():
        print(f"   - {planta}: {promedio:.2f} °C")

    # 3. Temperatura máxima, sensor(es) y fecha(s) correspondientes (1 pto - incluye empates)
    max_temp_val = df["temperatura_c"].max()
    max_temp_rows = df[df["temperatura_c"] == max_temp_val]
    print(f"\n3. Temperatura máxima registrada: {max_temp_val} °C")
    for idx, row in max_temp_rows.iterrows():
        print(f"   - Sensor: {row['id_sensor']} | Fecha: {row['fecha_hora']} | Planta: {row['planta']}")

if __name__ == "__main__":
    ejecutar_analisis()