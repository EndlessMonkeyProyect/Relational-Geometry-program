# Coordenadas compactas y energía de enlace

**Laboratorio exploratorio · incluido en 3.0.0-review · integración inicial del 6 de octubre de 2026**

Este laboratorio convierte una pregunta del programa en un contraste reproducible:
¿una coordenada que mejora una predicción aporta información nueva, o representa
de manera útil información ya disponible? En los 47 registros aportados, la
coordenada $r_V$ ofrece un ejemplo explícito de la segunda posibilidad. Esto da un
caso concreto para revisar el criterio de
[factorización de la información](../../02_formal_core/closure_information.es.md)
y distinguirlo de la [incorporación de novedad](../../02_formal_core/novelty_incorporation_and_dynamical_modes.es.md).

## Resultado reproducido

El objetivo de la tabla fuente es la **energía media de enlace simple**, en
kJ/mol. No es una colección de energías de disociación moleculares específicas.
Contiene 47 pares no orientados distintos de diez elementos:
C, N, O, F, Si, P, S, Cl, Br e I, de los grupos 14 a 17.

Con Ridge de parámetro $\alpha=1$ y estandarización aprendida dentro de cada
partición de entrenamiento, la reconstrucción obtiene:

| Características del modelo | RMSE por enlace, kJ/mol | RMSE por predicción, kJ/mol |
| --- | ---: | ---: |
| Diferencia de electronegatividad | 53,520874 | 55,049743 |
| Diferencia de electronegatividad y $r_{V,A}+r_{V,B}$ | 50,797514 | 52,080883 |
| Diferencia de electronegatividad y $1/(g_A-10)+1/(g_B-10)$ | 50,797514 | 52,080883 |
| Diferencia de electronegatividad y $1/(g_A-13)+1/(g_B-13)$ | 50,395337 | 51,803114 |

La reducción del primer RMSE al añadir $r_V$ es aproximadamente **5,09 %** respecto
de esta línea base simple. Las ocho filas del ranking suministrado también se
reproducen, incluidos RMSE, MAE y $R^2$. La comparación caracteriza esta muestra y
esta familia de modelos. No compara contra todos los modelos químicos posibles.

## Dos agregaciones de una misma validación

En cada partición *leave-one-element-out*, se excluyen del entrenamiento **todos**
los enlaces que contienen el elemento reservado. La media y la desviación
estándar poblacional de cada característica se calculan exclusivamente con las
filas de entrenamiento. El intercepto no se penaliza.

Un enlace heteronuclear A–B se predice dos veces: al reservar A y al reservar B.
Un enlace homonuclear se predice una vez. Hay **85 predicciones de prueba para
47 enlaces**. El programa conserva ambas maneras de resumirlas:

- **Por enlace:** primero promedia las predicciones de cada enlace y después
  calcula las métricas sobre los 47 enlaces. Esta convención reproduce el informe
  y los CSV aportados.
- **Por predicción:** concatena las 85 predicciones antes de calcular las
  métricas. Conserva el error de cada transferencia a un elemento reservado.

La primera métrica es una evaluación de predicciones promediadas. No debe
confundirse con la segunda, ni con la media de diez RMSE calculados por separado.
El promedio puede reducir errores opuestos y pondera cada enlace una vez. La
concatenación pondera dos veces cada enlace heteronuclear. Ninguna de estas
agrupaciones transforma las predicciones o enlaces en observaciones independientes.

## Papel formal de la coordenada

En todo el dominio aportado se verifica:

$$
r_V(g)=\frac{2}{g-10},
\qquad
r_{V,A}+r_{V,B}
=2\left(\frac{1}{g_A-10}+\frac{1}{g_B-10}\right).
$$

La igualdad también se obtiene algebraicamente si se adoptan las asignaciones del
informe $N_s=2$, $N_p=g-12$ y $r_V=N_s/(N_s+N_p)$. Se restringe aquí a los grupos
14–17 de la tabla. No se extrapola a todos los elementos.

Por tanto, $r_V$ **factoriza a través del grupo** en este dominio. La coordenada
es compacta y predictivamente aprovechable con el modelo elegido, pero no añade
una distinción que no pudiera recuperarse del grupo. Tras la estandarización por
partición, el factor positivo 2 produce las mismas características normalizadas
y las mismas predicciones Ridge. La equivalencia no depende de una búsqueda
numérica afortunada.

Este resultado aporta un banco de prueba para separar tres cuestiones:

1. **Contenido:** qué distinciones contiene una representación.
2. **Utilidad:** qué relaciones hace accesibles a una clase de modelos.
3. **Orientación de búsqueda:** cuánto trabajo ahorra proponer esa representación.

Se verifican las dos primeras en este ejemplo finito. Para medir la tercera
faltan trayectorias de búsqueda comparables y presupuestos de exploración
prefijados. La forma $1/(g-13)$ se evalúa aquí como fórmula ya seleccionada en el
informe, no como un nuevo descubrimiento independiente.

## Reproducir

Desde la raíz del repositorio, con Python y NumPy:

~~~bash
python 07_emergence_laboratory/chemistry/reproduce_bond_energy.py
python 07_emergence_laboratory/chemistry/reproduce_bond_energy.py --json
python -m unittest discover -s tests -p test_chemical_seed_benchmark.py -v
~~~

El programa no escribe archivos. La salida JSON incluye índices de entrenamiento
y prueba, medias, escalas, coeficientes, predicciones individuales y métricas de
ambas agregaciones. Se puede usar otra tabla compatible con el argumento:

~~~text
--dataset ruta/a/tabla.csv
~~~

sin reemplazar el conjunto fuente.

El [script](reproduce_bond_energy.py) es una **reconstrucción nueva y transparente**
de los modelos fijos y la agregación compatible con los resultados. El código
original del experimento químico no se incluyó entre los materiales recibidos.
No utiliza scikit-learn y no ejecuta búsqueda de fórmulas, permutaciones ni
bootstrap.

## Datos preservados y procedencia pendiente

Los tres CSV se conservan byte por byte, incluidos nombres originales de columnas
y precisión numérica. Los nombres de archivo del repositorio describen su función:

| Archivo local | Fuente aportada | Papel |
| --- | --- | --- |
| [bond_energy_dataset.csv](data/bond_energy_dataset.csv) | chemical_seed_independence_dataset.csv | Observaciones y descriptores suministrados |
| [supplied_model_results.csv](data/supplied_model_results.csv) | chemical_seed_independence_results.csv | Resumen del informe, incluida una fila de permutaciones no reproducida |
| [supplied_feature_ranking.csv](data/supplied_feature_ranking.csv) | chemical_seed_feature_ranking.csv | Ranking de ocho descriptores suministrado |

SHA-256 de las copias y de sus fuentes:

~~~text
bond_energy_dataset.csv
d866c96c14178402c3a8a974f09977d2facc43f0e45abceab22d3642961e4244
supplied_model_results.csv
25c29054a1c9a0ddb61c9dff77807fe87cfdbdf4af96dad7fc474762cfbf9656
supplied_feature_ranking.csv
ee03aa8f95b0c4c8dbb29a86107f697d9cd088b0b985760277985dbc68ddfe55
~~~

Las columnas de radio se expresan en pm y la energía en kJ/mol. Las columnas
de grupo y período son índices. Las columnas $P$, $r_V$, sus combinaciones y
la etiqueta **both_prime_weight** se conservan como descriptores suministrados,
no como magnitudes físicas establecidas ni como definiciones nuevas de primalidad.

El informe y el protocolo aportados describen la construcción y la pregunta, pero
la tabla no incluye una referencia bibliográfica completa por energía ni su
incertidumbre o contexto molecular. Completar esa trazabilidad es necesario para
una réplica química externa. No se han inventado fuentes ni valores faltantes.

## Alcance y siguiente contraste

Los ocho descriptores y la fórmula genérica se seleccionaron usando el mismo
corpus de validación que informa sus resultados. Ajustar el escalador dentro de
cada partición evita una filtración de ese ajuste, pero **no elimina el optimismo
por seleccionar una fórmula con los mismos resultados que luego se comunican**.
El siguiente contraste debe fijar previamente las fórmulas y evaluarlas en datos
nuevos, o usar validación anidada para separar selección y evaluación. También
debe justificar la dependencia entre enlaces que comparten elementos.

El informe fuente atribuye resultados a 500 permutaciones y a un bootstrap. No
se aportaron las realizaciones, las semillas ni el código correspondiente, por
lo que aquí no se verifican su distribución, su intervalo ni la excepcionalidad
de la semilla. La fila-resumen queda preservada como resultado **suministrado**,
no como cálculo ejecutado por este laboratorio.

El aporte verificable al programa es la equivalencia de información y la utilidad
predictiva de una coordenada compacta en un ejemplo concreto. Es un punto de
partida para estudiar representaciones y diseño de búsqueda, no una ley química
nueva ni una validación física general del programa.

## Convención canónica de descriptores

[CONDICIONAL] $r_V$, $P$ y $P3$ se tratan como descriptores exploratorios; no se atribuye a $P3$ una implementación ausente de los scripts. $d_{balance}$ se conserva como señal exploratoria, no como ley establecida; no se incorpora un resultado sin datos y protocolo. El corpus suministrado no acredita aquí una evaluación independiente de esos dos últimos descriptores.

[CONDICIONAL] La utilidad de una coordenada que factoriza por grupo, conteo electrónico, $Z$ u ocupaciones se contrasta frente a baselines, ablaciones y evaluación independiente o anidada. La tabla actual permite controles por grupo; ampliar $Z$ o las ocupaciones exige datos trazables. La validación física del programa requiere evidencia adicional.
