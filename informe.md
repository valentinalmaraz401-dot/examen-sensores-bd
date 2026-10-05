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

## 7. Batch y Streaming

### Tipo de procesamiento que realizamos
Nuestro programa `analisis.py` realiza **procesamiento por lotes (batch)**.

**Justificación:** lee un conjunto finito de datos que ya estaba guardado (`data/sensores_industriales.csv`, 100,000 registros), lo procesa completo de principio a fin en una sola ejecución y entrega los resultados al terminar. No reacciona a lecturas nuevas conforme llegan: si el archivo cambia, hay que volver a ejecutar el programa. Como es un análisis posterior a la recolección, no se necesita una respuesta inmediata.

### Alerta pocos segundos después de una lectura mayor que 85 °C
Usaríamos **streaming** (procesamiento de cada evento conforme llega).

**Justificación:** aquí el valor del resultado depende de la *latencia*. Una alerta que llega al día siguiente ya no sirve para actuar sobre la máquina. Con streaming, cada lectura se evalúa al llegar (`temperatura_c > 85`) y, si cumple la regla, se envía una notificación en segundos. Podría implementarse con una cola de mensajes (por ejemplo, Apache Kafka) y un motor de procesamiento de flujos (por ejemplo, Apache Flink o Spark Structured Streaming). Con la ampliación a miles de sensores enviando datos cada segundo, un programa que vuelve a leer un archivo completo ya no sería viable.

Detalle de diseño: para evitar falsas alarmas por una lectura aislada, se podría exigir que la regla se cumpla en varias lecturas consecutivas del mismo sensor. Esto aumentaría un poco la latencia, pero mejoraría la veracidad de la alerta.

### Resumen al terminar el día
Usaríamos **batch**, programado una vez al día (por ejemplo, un proceso automático a medianoche).

**Justificación:** un resumen diario (promedio por planta, máximos, número de alertas) necesita *todas* las lecturas del día y no se consulta minuto a minuto. Esperar a que el día cierre permite procesar el conjunto completo en una sola ejecución, con menor costo de cómputo y con un resultado completo y consistente.

### Relación con el tiempo en que se necesita cada resultado

| Necesidad | Tiempo en que se requiere el resultado | Enfoque |
|---|---|---|
| Alerta por temperatura > 85 °C | Segundos | Streaming |
| Resumen del día | Horas (al cierre del día) | Batch |
| Análisis del examen sobre el CSV | Sin urgencia (análisis posterior) | Batch |

La decisión depende de cuánto vale la información con el paso del tiempo: lo que pide acción inmediata se procesa por flujo, y lo que se consulta después se procesa por lotes.

---

## 8. Arquitecturas Lambda y Kappa

### Escenario A: ruta por lotes para recalcular el historial + ruta rápida para lo reciente
**Arquitectura elegida: Lambda.**

**Justificación:** Lambda mantiene dos rutas en paralelo, que es justo lo que describe el escenario. La **capa de lotes** recalcula el historial completo con precisión, y la **capa de velocidad** procesa las mediciones recientes con baja latencia. Una **capa de servicio** combina ambos resultados para consultarlos. Su ventaja es que ofrece resultados rápidos de lo reciente y resultados completos después. Su desventaja es que obliga a mantener dos lógicas de procesamiento distintas.

```
          [ Sensores / Fuentes de datos ]
                       │
            ┌──────────┴───────────┐
            ▼                      ▼
   ┌─────────────────┐    ┌─────────────────┐
   │  CAPA DE LOTES  │    │CAPA DE VELOCIDAD│
   │ Recalcula todo  │    │ Procesa lo      │
   │ el historial    │    │ reciente rápido │
   └────────┬────────┘    └────────┬────────┘
            │                      │
            └──────────┬───────────┘
                       ▼
          ┌─────────────────────────┐
          │    CAPA DE SERVICIO     │
          │ Une ambos resultados    │
          │ para consulta           │
          └─────────────────────────┘
```

### Escenario B: una sola lógica de procesamiento + conservar las mediciones para reprocesar
**Arquitectura elegida: Kappa.**

**Justificación:** Kappa elimina la ruta por lotes y procesa todo como flujo de eventos con una única lógica. Los eventos se conservan en un **registro inmutable** (log), por ejemplo Kafka. Si cambia una regla (por ejemplo, el umbral de alerta) o se detecta un error, se vuelve a leer el registro desde el inicio con el mismo código. Es más simple de mantener que Lambda porque solo hay una lógica que cuidar.

```
          [ Sensores / Fuentes de datos ]
                       │
                       ▼
       ┌───────────────────────────────┐
       │ REGISTRO INMUTABLE DE EVENTOS │
       │ (conserva todo el historial)  │
       └───────────────┬───────────────┘
                       ▼
       ┌───────────────────────────────┐
       │    PROCESAMIENTO DE FLUJO     │
       │       (una sola lógica)       │
       └───────────────┬───────────────┘
                       ▼
       ┌───────────────────────────────┐
       │       CAPA DE SERVICIO        │
       │      (vistas de salida)       │
       └───────────────────────────────┘
```

Para reprocesar, se vuelve a leer el registro inmutable desde el inicio con la misma lógica de flujo, sin crear una ruta aparte.

---

## 9. Analítica descriptiva, predictiva y prescriptiva

### Descriptiva (hallazgos reales de nuestro análisis)
1. **Alertas por planta:** se registraron **6,954 lecturas** con temperatura mayor que 85 °C, de un total de 100,000 (6.95 %). La planta con más alertas fue **Planta_3**, con **1,777 alertas** (25.55 % del total de alertas).
2. **Temperatura máxima:** el valor más alto fue **104.99 °C** y hubo **empate entre 4 lecturas**:
   - sensor S023, Planta_3, 01/09/26 22:23
   - sensor S019, Planta_2, 02/09/26 13:11
   - sensor S014, Planta_2, 02/09/26 15:23
   - sensor S030, Planta_3, 02/09/26 16:02

   (Las fechas se muestran tal como las imprime el programa.)

**Observación sobre los datos:** las temperaturas promedio por planta son casi iguales (Planta_1 = 66.62 °C, Planta_2 = 66.53 °C, Planta_3 = 66.77 °C, Planta_4 = 66.67 °C). Además, el 25.55 % de alertas de Planta_3 está muy cerca del 25 % que se esperaría si las alertas se repartieran por igual entre las 4 plantas. Por eso la diferencia entre plantas es pequeña y no basta para concluir que Planta_3 sea más riesgosa.

### Predictiva
**Pregunta:** ¿Qué máquinas tienen mayor probabilidad de presentar una falla en las próximas 48 horas si su temperatura y su vibración aumentan de forma sostenida?

**Datos adicionales necesarios** (el CSV actual no los contiene):
1. Historial de fallas y mantenimientos (fechas y tipo de falla), para saber qué lecturas anteceden a una falla real.
2. Identificación de la máquina asociada a cada sensor, con su modelo, edad y especificaciones del fabricante. El CSV solo identifica sensores y plantas.
3. Condiciones de operación: carga de trabajo, horas de uso y temperatura ambiente.
4. Series de tiempo más largas, para detectar tendencias y no solo lecturas sueltas.

Sin el punto 1 no se puede entrenar ni validar un modelo. Una lectura por encima de 85 °C es una alerta del ejercicio, pero por sí sola no demuestra que una máquina vaya a fallar.

### Prescriptiva
**Riesgo previsto:** que los sensores con las lecturas máximas (S023, S019, S014 y S030, todos con 104.99 °C) y la Planta_3, que concentra más alertas, sigan mostrando temperaturas altas de forma repetida.

**Acción propuesta:** programar una inspección técnica de los equipos asociados a esos cuatro sensores antes del siguiente turno de producción. Se priorizarían S023 y S030, porque pertenecen a Planta_3, que además es la planta con más alertas.

**Información que revisaríamos antes de decidir:**
1. Si las lecturas altas son picos aislados o una tendencia sostenida, por ejemplo contando las alertas por sensor, porque una sola lectura máxima no indica un patrón.
2. Si la vibración también aumenta en esos mismos momentos. Nuestro análisis no la incluyó.
3. Si los sensores funcionan bien o están descalibrados, comparándolos con otros sensores de la misma planta.
4. El historial de mantenimiento de las máquinas y la fecha de su última revisión.
5. El costo de detener la producción frente al costo de una posible falla, y la disponibilidad de técnicos y refacciones.