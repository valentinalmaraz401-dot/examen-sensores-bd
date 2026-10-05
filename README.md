# Examen Práctico — Manejo Masivo de Datos

## Objetivo del Proyecto
Analizar 100,000 mediciones de sensores de temperatura y vibración distribuidos en cuatro plantas industriales para identificar anomalías operativas, exportar registros de alerta y evaluar estrategias de escalabilidad bajo arquitecturas Big Data.

## Descripción de los Datos
El archivo de datos contiene las siguientes columnas:
* `id_registro`: Identificador único de cada medición.
* `fecha_hora`: Fecha y hora de la lectura.
* `id_sensor`: Identificador del sensor.
* `planta`: Planta industrial donde está instalado el sensor.
* `temperatura_c`: Temperatura registrada en grados Celsius (°C).
* `vibracion_mm_s`: Vibración registrada en milímetros por segundo (mm/s).

> **Aviso Importante:** Todos los datos procesados en este proyecto son **simulados** con fines exclusivamente didácticos y académicos.

## Estructura del Repositorio
```text
├── data/
│   └── sensores_industriales.csv   # Dataset original simulado
├── resultados/
│   └── alertas.csv                 # Lecturas filtradas con temperatura > 85 °C
├── .gitignore                      # Configuración de exclusiones de Git
├── analisis.py                     # Script principal de análisis
├── README.md                       # Documentación del proyecto
└── requirements.txt                # Dependencias del proyecto (pandas)

## Requisitos Previos
* Python 3.8 o superior.
* Git.

## Comandos para Instalar y Ejecutar el Proyecto

1. **Clonar el repositorio:**
   ```powershell
   git clone [https://github.com/valentinalmaraz401-dot/examen-sensores-bd.git](https://github.com/valentinalmaraz401-dot/examen-sensores-bd.git)
   cd examen-sensores-bd

2. **Crear y activar el entorno virtual (venv)**
python -m venv venv
.\venv\Scripts\Activate.ps1

3. **Instalar dependencias**
pip install -r requirements.txt

3. **Ejecutar el script de análisis**
python analisis.py

