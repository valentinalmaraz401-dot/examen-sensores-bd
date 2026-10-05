# Examen Práctico: Manejo Masivo de Datos

## Descripción

Este proyecto consiste en el procesamiento y análisis de 100,000 mediciones simuladas provenientes de sensores industriales de temperatura y vibración, distribuidos en cuatro plantas industriales.

Mediante el uso de Python y la biblioteca Pandas, se procesan los datos para identificar mediciones que superen un límite de temperatura establecido. Como resultado, se genera un archivo CSV independiente que contiene las lecturas identificadas como alertas.

El proyecto tiene fines académicos y permite aplicar conocimientos de manejo masivo de datos, procesamiento de información y control de versiones mediante Git y GitHub.

## 1. Objetivo

Desarrollar un programa en Python que permita procesar y analizar un conjunto de 100,000 registros de sensores industriales, con el propósito de identificar mediciones que superen un límite de temperatura de 85 °C y generar un archivo con los registros que cumplan esta condición.

Los objetivos específicos son:

* Procesar grandes cantidades de información utilizando Pandas.
* Leer y analizar archivos en formato CSV.
* Identificar mediciones que superen el límite de temperatura establecido.
* Generar un archivo independiente con las alertas detectadas.
* Aplicar herramientas de control de versiones mediante Git y GitHub.

## 2. Datos utilizados

El proyecto utiliza un conjunto de datos simulado que representa mediciones obtenidas de sensores industriales ubicados en cuatro plantas.

El dataset contiene 100,000 registros que incluyen información sobre la fecha y hora de las mediciones, la identificación de los sensores, la planta correspondiente, la temperatura y el nivel de vibración.

El archivo de entrada se encuentra en la siguiente ubicación:

`data/sensores_industriales.csv`

Los datos son simulados y se utilizan exclusivamente con fines académicos.

## 3. Columnas del dataset

El archivo `sensores_industriales.csv` contiene las siguientes columnas:

| Columna          | Descripción                                                     |
| ---------------- | --------------------------------------------------------------- |
| `id_registro`    | Identificador único de cada medición.                           |
| `fecha_hora`     | Fecha y hora en la que se realizó la lectura.                   |
| `id_sensor`      | Identificador del sensor que registró la medición.              |
| `planta`         | Planta industrial donde se encuentra el sensor.                 |
| `temperatura_c`  | Temperatura registrada en grados Celsius (°C).                  |
| `vibracion_mm_s` | Nivel de vibración registrado en milímetros por segundo (mm/s). |

## 4. Criterio de alertas

Para identificar las mediciones que requieren atención, se establece un límite de temperatura de 85 °C.

Una medición se considera una alerta cuando cumple la siguiente condición:

```python
datos["temperatura_c"] > 85
```

El programa filtra los registros que superan este valor y los almacena en un archivo independiente llamado `alertas.csv`.

El archivo generado se guarda en:

`resultados/alertas.csv`

Este criterio se establece con fines demostrativos y no representa necesariamente un límite operativo real para equipos industriales.

## 5. Estructura de carpetas

La estructura del proyecto es la siguiente:

```text
examen-sensores-bd/
│
├── data/
│   └── sensores_industriales.csv
│
├── resultados/
│   └── alertas.csv
│
├── analisis.py
├── requirements.txt
├── .gitignore
└── README.md
```

Descripción de los elementos:

* `data/`: contiene el dataset original con las mediciones simuladas.
* `resultados/`: almacena el archivo CSV generado con las alertas.
* `analisis.py`: contiene el código principal para procesar y analizar los datos.
* `requirements.txt`: especifica las dependencias necesarias para ejecutar el programa.
* `.gitignore`: define los archivos y carpetas que Git debe ignorar.
* `README.md`: contiene la documentación e instrucciones del proyecto.

El entorno virtual `venv/` se crea localmente durante la instalación y normalmente no se incluye en el repositorio de GitHub.

## 6. Tecnologías

| Tecnología         | Uso                                                                     |
| ------------------ | ----------------------------------------------------------------------- |
| Python             | Lenguaje de programación utilizado para desarrollar el proyecto.        |
| Pandas             | Lectura, manipulación, filtrado y procesamiento de datos.               |
| CSV                | Formato utilizado para almacenar los datos originales y los resultados. |
| Git                | Control de versiones del código.                                        |
| GitHub             | Alojamiento del repositorio y administración del proyecto.              |
| Visual Studio Code | Editor de código recomendado para trabajar en el proyecto.              |

## 7. Requisitos previos

Para instalar y ejecutar el proyecto se requiere:

* Python 3.8 o superior.
* Git instalado y configurado.
* pip para instalar las dependencias de Python.
* Acceso a una terminal, como PowerShell en Windows.
* Conexión a internet para clonar el repositorio e instalar las dependencias.

Se recomienda utilizar un entorno virtual para mantener aisladas las bibliotecas del proyecto.

## 8. Instalación

Primero, se debe clonar el repositorio desde GitHub.

Abrir PowerShell y ejecutar el siguiente comando:

```powershell
git clone https://github.com/valentinalmaraz401-dot/examen-sensores-bd.git
```

Después, ingresar a la carpeta del proyecto:

```powershell
cd examen-sensores-bd
```

Una vez dentro del directorio, se podrán realizar los pasos necesarios para configurar el entorno y ejecutar el programa.

## 9. Creación del entorno virtual

Para crear un entorno virtual de Python, ejecutar:

```powershell
python -m venv venv
```

Este comando genera una carpeta llamada `venv`, que contiene un entorno aislado para instalar las bibliotecas necesarias sin afectar otras instalaciones de Python.

## 10. Activación del entorno

En Windows PowerShell, activar el entorno virtual mediante el siguiente comando:

```powershell
.\venv\Scripts\Activate.ps1
```

Cuando el entorno se activa correctamente, la terminal mostrará el nombre `venv` al inicio de la línea de comandos, por ejemplo:

```text
(venv) PS C:\...\examen-sensores-bd>
```

Si PowerShell bloquea la ejecución del script de activación, se pueden consultar las políticas de ejecución de Windows y utilizar una alternativa permitida por el sistema.

## 11. Instalación de dependencias

Con el entorno virtual activado, instalar las bibliotecas especificadas en el archivo `requirements.txt`:

```powershell
pip install -r requirements.txt
```

Este comando instala las dependencias necesarias para que el programa pueda ejecutarse correctamente.

La biblioteca principal utilizada para el procesamiento de datos es Pandas.

## 12. Ejecución

Para iniciar el análisis, ejecutar el siguiente comando desde la carpeta principal del proyecto:

```powershell
python analisis.py
```

El programa leerá el archivo original ubicado en `data/sensores_industriales.csv`, procesará las mediciones y aplicará el criterio de temperatura establecido.

Al finalizar, se generará el archivo de resultados en:

```text
resultados/alertas.csv
```

## 13. Funcionamiento

El programa realiza el procesamiento de los datos mediante las siguientes etapas:

1. **Lectura de datos:** se utiliza Pandas para cargar el archivo `sensores_industriales.csv`.
2. **Procesamiento:** se accede a los registros y a las columnas necesarias para realizar el análisis.
3. **Filtrado:** se identifican las mediciones cuya temperatura supera los 85 °C.
4. **Generación de alertas:** se separan los registros que cumplen la condición establecida.
5. **Exportación:** se guardan las mediciones filtradas en el archivo `resultados/alertas.csv`.

El flujo general del proyecto es:

```text
sensores_industriales.csv
          |
          v
   Lectura con Pandas
          |
          v
 Procesamiento de datos
          |
          v
  Filtro de temperatura
     temperatura > 85 °C
          |
          v
   Generación de alertas
          |
          v
 resultados/alertas.csv
```

## 14. Resultado esperado

Después de ejecutar el programa, se espera obtener un archivo denominado `alertas.csv`, que contenga únicamente las mediciones cuya temperatura sea superior a 85 °C.

El archivo de entrada original se conserva sin modificaciones, mientras que los registros filtrados se almacenan de forma independiente para facilitar su consulta y análisis.

La cantidad de alertas dependerá de los valores presentes en el dataset.

## 15. Archivos principales

| Archivo                          | Descripción                                                                |
| -------------------------------- | -------------------------------------------------------------------------- |
| `analisis.py`                    | Script principal encargado de leer, procesar y filtrar los datos.          |
| `data/sensores_industriales.csv` | Dataset original con 100,000 mediciones simuladas.                         |
| `resultados/alertas.csv`         | Archivo de salida con las mediciones que superan los 85 °C.                |
| `requirements.txt`               | Archivo que contiene las dependencias del proyecto.                        |
| `.gitignore`                     | Archivo que indica qué elementos deben excluirse del control de versiones. |
| `README.md`                      | Documento que describe el proyecto y explica cómo instalarlo y ejecutarlo. |

El archivo `resultados/alertas.csv` se genera al ejecutar el programa, por lo que puede no estar presente antes de la primera ejecución.

## 16. Reproducibilidad

Para reproducir el análisis desde cero en un equipo con Python y Git instalados, se deben ejecutar los siguientes comandos en PowerShell:

```powershell
git clone https://github.com/valentinalmaraz401-dot/examen-sensores-bd.git

cd examen-sensores-bd

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python analisis.py
```

Al finalizar, el archivo de resultados se encontrará en la carpeta `resultados/`.

La reproducibilidad depende de contar con el dataset original y las versiones de las dependencias requeridas por el proyecto.

## 17. Comandos de Git

Git se utiliza para llevar un control de las modificaciones realizadas en los archivos del proyecto y para sincronizar los cambios con GitHub.

Consultar el estado del repositorio:

```powershell
git status
```

Agregar todos los cambios:

```powershell
git add .
```

Crear un commit:

```powershell
git commit -m "Actualización del proyecto"
```

Enviar los cambios al repositorio remoto:

```powershell
git push
```

Actualizar el repositorio local con los cambios remotos:

```powershell
git pull
```

Estos comandos permiten mantener actualizado el proyecto y registrar las modificaciones realizadas durante su desarrollo.

## 18. Consideraciones

* Los datos utilizados son simulados y no corresponden a mediciones reales de instalaciones industriales.
* El límite de 85 °C se utiliza únicamente como criterio académico para demostrar el filtrado de información.
* El archivo original debe conservarse para evitar la pérdida de los datos de entrada.
* El archivo `alertas.csv` se genera como resultado del procesamiento.
* El entorno virtual `venv/` es local y se recomienda excluirlo del repositorio mediante `.gitignore`.
* Los resultados dependen de los registros contenidos en el dataset.
* Las alertas generadas no constituyen un diagnóstico definitivo del estado de una máquina o instalación industrial.

## 19. Resumen

El proyecto permite aplicar técnicas de manejo masivo de datos mediante el procesamiento de 100,000 mediciones simuladas de sensores industriales.

A través de Python y Pandas, se leen los datos, se filtran las mediciones cuya temperatura supera los 85 °C y se genera un archivo CSV independiente con las alertas identificadas.

Además, el proyecto utiliza Git y GitHub para el control de versiones, la organización de los archivos y el almacenamiento del código fuente.

Con este ejercicio se aplican conocimientos de lectura, procesamiento, filtrado y exportación de datos, así como herramientas fundamentales para el desarrollo de proyectos de análisis de información.

## 20. Autores

**Valentín Almaraz Martinez y Alberto Saul Lopez Crespo**

 **Manejo Masivo de Datos**.

Repositorio: https://github.com/valentinalmaraz401-dot/examen-sensores-bd
