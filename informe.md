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