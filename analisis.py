import os
import pandas as pd

# Definición de rutas relativas obligatorias
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "sensores_industriales.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "alertas.csv")