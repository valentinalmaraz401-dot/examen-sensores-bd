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

    # 4. Lecturas con temperatura mayor que 85 °C (1 pto)
    df_alertas = df[df["temperatura_c"] > 85]
    total_alertas = len(df_alertas)
    print(f"\n4. Cantidad de lecturas con alerta (> 85 °C): {total_alertas}")

    # 5. Planta con más alertas de temperatura (1 pto - incluye empates)
    print("\n5. Planta(s) con mayor cantidad de alertas:")
    alertas_por_planta = df_alertas["planta"].value_counts()
    if not alertas_por_planta.empty:
        max_alertas_count = alertas_por_planta.max()
        plantas_top = alertas_por_planta[alertas_por_planta == max_alertas_count]
        for planta, count in plantas_top.items():
            print(f"   - {planta}: {count} alertas")

if __name__ == "__main__":
    ejecutar_analisis()