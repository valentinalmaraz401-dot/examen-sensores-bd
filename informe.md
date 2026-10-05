# Parte II. Aplicación al caso de Big Data

## Introducción

El presente informe aplica conceptos fundamentales de Big Data al proyecto de análisis de sensores industriales. El proyecto utiliza un archivo CSV con 100,000 registros de mediciones de sensores de temperatura y vibración correspondientes a cuatro plantas industriales.

El objetivo del análisis es identificar patrones y situaciones que puedan representar alertas de temperatura, utilizando Python y Pandas para procesar los datos. En particular, se considera como alerta una lectura de temperatura superior a 85 °C.

Los resultados obtenidos permiten relacionar el proyecto con conceptos como las cinco V de Big Data, procesamiento Batch y Streaming, arquitecturas Lambda y Kappa, y los diferentes tipos de analítica.

---

# 5. Las 5 V aplicadas al proyecto

Las cinco V de Big Data son Volumen, Velocidad, Variedad, Veracidad y Valor. Estas características permiten analizar cómo un sistema de sensores puede manejar grandes cantidades de información y convertirla en datos útiles para la toma de decisiones.

## Tabla de las 5 V

| V | Aplicación al proyecto | Ejemplo concreto | Situación |
|---|---|---|---|
| Volumen | El sistema puede generar una gran cantidad de mediciones conforme aumenta el número de sensores y el tiempo de operación. | El archivo actual contiene 100,000 registros de sensores. | Presente |
| Velocidad | Los sensores pueden generar nuevas mediciones constantemente, por lo que el sistema podría necesitar procesarlas rápidamente. | Recibir una medición y generar una alerta cuando la temperatura supere los 85 °C. | Futuro |
| Variedad | Las mediciones pueden complementarse con diferentes tipos de información además del CSV. | Incorporar mensajes JSON, fotografías de máquinas y reportes de mantenimiento. | Futuro |
| Veracidad | Es necesario comprobar que los datos sean correctos, consistentes y confiables antes de utilizarlos para tomar decisiones. | Detectar valores incorrectos, datos faltantes o mediciones fuera de rangos razonables. | Presente y futuro |
| Valor | El análisis debe convertir las mediciones en información útil para la empresa. | Identificar que Planta_3 concentra la mayor cantidad de alertas de temperatura. | Presente |

## Volumen

El volumen se refiere a la cantidad de datos que puede generar y almacenar un sistema.

En el proyecto actual se cuenta con un archivo CSV de 100,000 registros de mediciones industriales. Cada registro contiene información como el identificador del sensor, la planta, la fecha y hora, la temperatura y la vibración.

Aunque 100,000 registros representan un conjunto considerable para el ejercicio, esta cantidad por sí sola no significa que el sistema sea Big Data. El volumen podría aumentar considerablemente si se agregan más sensores, más plantas o mediciones durante periodos más largos.

Por ejemplo, una empresa que tenga cientos o miles de sensores funcionando continuamente podría generar millones de registros diariamente.

**Situación del ejemplo:** Presente.

## Velocidad

La velocidad representa la rapidez con la que se generan, reciben y procesan los datos.

Actualmente, el proyecto trabaja con un archivo CSV que ya contiene las mediciones almacenadas. Por esta razón, el análisis se realiza después de que los datos han sido generados y guardados.

En una futura ampliación, los sensores podrían enviar mediciones continuamente y el sistema podría procesarlas prácticamente en tiempo real. Por ejemplo, cuando un sensor registre una temperatura superior a 85 °C, el sistema podría generar una alerta pocos segundos después de recibir la medición.

**Situación del ejemplo:** El procesamiento en tiempo real sería una ampliación futura.

## Variedad

La variedad se refiere a la existencia de diferentes tipos y formatos de datos.

Actualmente, el proyecto utiliza principalmente información estructurada almacenada en un archivo CSV. Sin embargo, un sistema industrial real podría incorporar diferentes fuentes de información.

Por ejemplo:

- Datos de sensores almacenados en CSV.
- Mensajes enviados por sensores mediante JSON.
- Fotografías de las máquinas.
- Reportes de mantenimiento escritos por técnicos.

Estos datos podrían combinarse para obtener un análisis más completo del estado de las máquinas.

**Situación del ejemplo:** El CSV está presente actualmente; JSON, fotografías y textos serían una futura expansión.

## Veracidad

La veracidad se refiere a qué tan confiables, correctos y consistentes son los datos utilizados.

Para un sistema de sensores industriales es importante verificar que las mediciones sean razonables y que no existan errores causados por sensores defectuosos, problemas de comunicación o datos incompletos.

Por ejemplo, si un sensor registra una temperatura extremadamente diferente a las mediciones anteriores, sería necesario revisar si se trata de una situación real o de un error de medición.

En este proyecto los datos son simulados para fines académicos, por lo que los resultados permiten demostrar el funcionamiento del análisis, pero no deben interpretarse como evidencia real del comportamiento de una máquina industrial.

**Situación del ejemplo:** Presente como consideración del análisis y relevante para una futura implementación real.

## Valor

El valor representa la utilidad que se obtiene al analizar los datos.

El proyecto transforma las mediciones de los sensores en información que puede ayudar a identificar situaciones que requieren atención.

Por ejemplo, el análisis identificó 6,954 lecturas con una temperatura superior a 85 °C. Además, Planta_3 presentó la mayor cantidad de alertas, con 1,777 lecturas.

Esta información podría utilizarse como punto de partida para investigar qué está ocurriendo en una determinada planta y decidir si es necesario realizar una revisión.

**Situación del ejemplo:** Presente.

---

# 6. Tipos de datos y procesamiento tradicional

Los sistemas industriales pueden trabajar con diferentes tipos de datos. No todos los datos tienen la misma estructura ni se procesan de la misma manera.

## Clasificación de los datos

| Tipo de dato | Clasificación | Justificación |
|---|---|---|
| CSV de sensores | Estructurado | Tiene filas y columnas con campos definidos, como sensor, planta, temperatura y vibración. |
| Mensaje JSON de un sensor | Semiestructurado | Tiene una estructura organizada mediante claves y valores, pero no utiliza una tabla tradicional. |
| Fotografía de una máquina | No estructurado | Es información visual que no está organizada originalmente en filas y columnas. |
| Texto libre de un reporte de mantenimiento | No estructurado | Contiene información escrita libremente y no tiene una estructura tabular fija. |

## CSV de sensores

El archivo CSV utilizado en el proyecto es un ejemplo de datos estructurados porque cada registro tiene una estructura definida mediante columnas.

Las columnas utilizadas son:

- `id_registro`
- `fecha_hora`
- `id_sensor`
- `planta`
- `temperatura_c`
- `vibracion_mm_s`

Esta estructura permite que Pandas pueda leer, filtrar, agrupar y analizar los datos fácilmente.

## JSON

Un mensaje JSON de un sensor sería un ejemplo de dato semiestructurado.

Por ejemplo, un sensor podría enviar información con una estructura similar a:

```json
{
  "id_sensor": "S023",
  "planta": "Planta_3",
  "temperatura_c": 87.4,
  "vibracion_mm_s": 4.2
}
```
Aunque los datos están organizados mediante claves y valores, no tienen necesariamente la estructura de una tabla CSV.

### Fotografía

Una fotografía de una máquina es un dato no estructurado porque contiene información visual.

Por ejemplo, una cámara podría tomar fotografías de una máquina para posteriormente utilizar técnicas de procesamiento de imágenes para identificar daños, desgaste o alguna condición anormal.

### Texto de mantenimiento

Un reporte de mantenimiento escrito por un técnico también puede considerarse un dato no estructurado.

Por ejemplo:

> *"Durante la revisión se detectó un aumento de temperatura y ruido inusual en el motor."*

Este tipo de información podría analizarse posteriormente mediante técnicas de procesamiento de lenguaje natural.

---

## ¿Por qué 100,000 registros no son automáticamente Big Data?

Tener 100,000 registros no significa automáticamente que un conjunto de datos sea Big Data.

El concepto de Big Data no depende únicamente de la cantidad de registros. También se consideran características como el volumen, la velocidad, la variedad, la veracidad y el valor de los datos.

Un archivo de 100,000 registros puede ser procesado fácilmente en una computadora convencional utilizando Python y Pandas[cite: 5]. Sin embargo, si el sistema comienza a recibir millones de registros continuamente desde miles de sensores, la situación puede requerir tecnologías especializadas para almacenamiento y procesamiento distribuido.

Por lo tanto, en este proyecto los 100,000 registros representan un ejercicio de manejo masivo de datos, pero no se debe afirmar que la cantidad por sí sola convierte al archivo en Big Data.

---

## Limitaciones al aumentar la escala

Si la cantidad de datos aumenta considerablemente, pueden aparecer diferentes limitaciones:

* **Consumo de recursos:** Mayor consumo de memoria RAM.
* **Capacidad:** Mayor espacio necesario para almacenamiento.
* **Rendimiento:** Mayor tiempo de procesamiento.
* **Infraestructura:** Dificultades para procesar los datos en una sola computadora.
* **Escalabilidad:** Necesidad de procesamiento distribuido.
* **Ingesta:** Necesidad de sistemas capaces de recibir datos en tiempo real.
* **Consultas:** Mayor complejidad para almacenar y consultar grandes cantidades de información.
* **Gobernanza:** Necesidad de mecanismos para controlar la calidad y confiabilidad de los datos.

# 7. Batch y Streaming

## Procesamiento actual

El programa actual utiliza un procesamiento de tipo **Batch**, debido a que trabaja con un archivo CSV que contiene los datos previamente almacenados.

El programa carga todos los registros del archivo `sensores_industriales.csv`, realiza los cálculos correspondientes y posteriormente genera el archivo `alertas.csv` con las lecturas que cumplen la condición establecida.

El proceso actual puede representarse de la siguiente manera:

```text
Archivo CSV
     |
     v
Carga de datos con Pandas
     |
     v
Procesamiento de los registros
     |
     v
Identificación de alertas
     |
     v
Archivo alertas.csv
```

Este tipo de procesamiento es adecuado para el proyecto actual porque no es necesario responder inmediatamente cuando se genera cada medición. Los datos pueden analizarse después de haber sido almacenados.

---

## Alerta en pocos segundos

Si la empresa necesitara generar una alerta pocos segundos después de que un sensor registre una temperatura superior a **85 °C**, sería necesario utilizar un procesamiento de tipo **Streaming**.

En este caso, los sensores enviarían las mediciones continuamente y el sistema procesaría cada dato conforme fuera recibido.

El proceso podría funcionar de la siguiente manera:

```text
Sensor
   |
   v
Nueva medición
   |
   v
Sistema de Streaming
   |
   v
¿Temperatura > 85 °C?
   |
   +------ Sí ------> Generar alerta
   |
   +------ No ------> Continuar monitoreo
```

De esta manera, el sistema no tendría que esperar a que se complete un archivo para realizar el análisis. Cada nueva medición podría evaluarse inmediatamente.

---

## Resumen diario

Para generar un resumen diario de las mediciones, sería adecuado utilizar nuevamente un procesamiento **Batch**.

Al finalizar el día, el sistema podría tomar todas las mediciones almacenadas y calcular diferentes estadísticas, por ejemplo:

* Temperatura promedio por planta.
* Temperatura máxima registrada.
* Cantidad de alertas.
* Planta con mayor cantidad de alertas.
* Cantidad de mediciones por sensor.
* Promedio de vibración por planta.

El proceso podría representarse de la siguiente manera:

```text
Datos almacenados durante el día
              |
              v
       Procesamiento Batch
              |
              v
     Cálculos y estadísticas
              |
              v
         Resumen diario
```

El procesamiento Batch resulta apropiado porque el resumen no necesita generarse inmediatamente después de cada medición. Puede ejecutarse una vez al día utilizando todos los datos acumulados.

---

## Relación con el tiempo de respuesta

La elección entre Batch y Streaming depende principalmente del tiempo de respuesta que requiere la situación.

| Situación | Tipo de procesamiento | Justificación |
| :--- | :--- | :--- |
| **Analizar el archivo histórico de sensores** | Batch | Los datos ya están almacenados y no requieren una respuesta inmediata. |
| **Generar un resumen diario** | Batch | El análisis puede realizarse periódicamente al finalizar el día. |
| **Detectar una temperatura mayor a 85 °C en pocos segundos** | Streaming | La alerta requiere una respuesta rápida después de recibir la medición. |
| **Analizar grandes cantidades de datos históricos** | Batch | Permite procesar un conjunto completo de información almacenada. |

> **Conclusión:** Batch es adecuado cuando los datos pueden procesarse en grupos y no existe una necesidad inmediata de respuesta. En cambio, Streaming es más adecuado cuando las decisiones dependen de información que está llegando continuamente y se requiere una respuesta rápida.