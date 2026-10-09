# Protocolo de validación de descriptores químicos

**Le Matt Ansatz Di Ego · Comparaciones reproducibles y objetivos separados**

El laboratorio evalúa si una representación compacta conserva información
útil para un objetivo químico declarado. El protocolo permite comparar
descriptores con referencias sencillas y distinguir interpretación estructural
de rendimiento predictivo.

## 1. Declarar objeto, dato y pregunta

Cada experimento identifica su unidad de observación, variable objetivo,
dominio químico, bibliografía de datos y versión. Se separan, en particular:

- el [ensayo de 47 enlaces](README.es.md), con energías de enlace y validación
  dejando elementos fuera según su contrato;
- un protocolo de propiedades atómicas sobre 40 elementos de los grupos 1, 2
  y 13–18, períodos 2–6, con ionización o radio covalente como objetivos;
- las hipótesis de independencia de semilla, que requieren su propio diseño.

Estos dominios no son réplicas intercambiables. Esta nota publica el método;
no incorpora un nuevo conjunto de datos ni atribuye a un ensayo los resultados
de otro.

## 2. Tipar el descriptor

Para ocupaciones de valencia declaradas,

$$r_V^{\rm chem}=\frac{N_s}{N_s+N_p}.$$

En la convención s/p indicada, vale 1 en los grupos 1 y 2 y $2/v$ en el bloque p,
con $v=N_s+N_p$. Es una función del grupo: conserva una reparametrización de esa
información y agrupa algunos valores. Su rendimiento depende del modelo y de la
pregunta elegidos. Este descriptor se distingue del
[peso geométrico respecto de una referencia](../../02_formal_core/resolution_and_modal_weights.es.md)
y de una fracción de frecuencias físicas.

## 3. Referencias y validación

Fijar antes de la evaluación:

1. Referencias: media del conjunto de entrenamiento, grupo, período, conteo de
   valencia, inverso de ese conteo e indicador de bloque, según el objetivo.
2. Familia de modelos, regularización e interacciones permitidas.
3. Partición de entrenamiento y evaluación: por elemento, enlace o familia,
   según el tipo de generalización que se pretende medir.
4. Métrica primaria, ponderación de observaciones repetidas e incertidumbre.
5. Regla para seleccionar modelos y un conjunto independiente o validación
   anidada cuando esa selección usa los propios datos.

Toda estandarización, imputación y selección ajustada al objetivo se aprende
exclusivamente en entrenamiento. Se guardan predicciones por observación y por
partición, no sólo promedios globales. Para modelos por período, también se
declaran las filas de entrenamiento disponibles y el rango de la matriz de diseño.

## 4. Comunicación del resultado

Una correlación describe una asociación en un dominio. Una mejora predictiva
se reporta respecto de una referencia, una métrica y una evaluación concretas.
El valor de una coordenada como interpretación y su ventaja predictiva son
preguntas distintas. La evidencia debe delimitar ambas con justicia.

El siguiente aporte verificable puede ser una fuente bibliográfica trazable,
una réplica, un descriptor prefijado o una evaluación independiente. Esta es
la ruta de revisión R12 del [programa](../../REVIEW.md).
