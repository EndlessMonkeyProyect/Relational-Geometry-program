# Forma colectiva y memoria de un sesgo transitorio

Este laboratorio estudia cómo una perturbación direccional temprana y una regla
de crecimiento común producen formas finales próximas en ciertos descriptores.
Aporta una prueba concreta de la distinción entre historia de formación y
descripción colectiva: las dos pueden estudiarse por separado.

**Estado:** experimento computacional exploratorio y reanálisis reproducible de
datos aportados. No es una simulación atomística. La proximidad a tamaño finito
no establece un límite de convergencia ni una identidad colectiva acreditada.

## Papel en el programa

La [identidad contextual](../../02_formal_core/contextual_identity_and_scale_promotion.es.md)
pregunta qué consultas y operaciones puede resolver una interfaz colectiva.
Este laboratorio ofrece candidatos medibles para esa interfaz y conserva el
acceso al microestado en las nuevas ejecuciones. El paso siguiente será comprobar
qué predicciones de continuación puede sostener esa descripción.

La [dinámica en cocientes](../../02_formal_core/collective_dynamics_on_quotients.es.md)
formula un criterio exacto de autonomía en un sector lineal. Aquí la dinámica es
estocástica y el espacio de sitios ocupados cambia: ese resultado no se aplica
directamente. Haría falta demostrar suficiencia predictiva o un cierre
probabilístico para una clase declarada de continuaciones.

## Modelo y términos

Ambas condiciones empiezan en el mismo sitio ocupado, (0,0). Lo que cambia es un
campo direccional temporal, no la geometría inicial. Por eso las condiciones del
módulo se llaman **sin sesgo** y **con sesgo transitorio**. Las etiquetas históricas
sin_semilla/con_semilla se preservan intactas en los CSV originales. La semilla
pseudoaleatoria es un tercer objeto distinto: un identificador del flujo de azar.

En cada adición se elige un sitio de la frontera de ocho vecinos con probabilidad
proporcional a exp(βs), donde

\[
s(x,y,t)=-\max(|x|,|y|)+0.35\,b_8(x,y)+a(t)\cos(2\theta),\qquad
a(t)=A\,e^{-t/\tau}.
\]

Aquí b8 cuenta vecinos ocupados, θ se mide desde el origen fijo y t=1 selecciona
el segundo sitio. El término radial de Chebyshev favorece una envolvente cuadrada.
La regla combina un vínculo local con una preferencia radial global. La simetría
cuádruple del medio está puesta en la regla, no descubierta a partir de una
dinámica isotrópica. β=3 y el coeficiente de enlace 0,35 se conservan.

El crecimiento se detiene en un número de sitios fijado. No se evalúa una condición
de equilibrio. El decaimiento exponencial nunca se anula exactamente en tiempo
finito; el nuevo parámetro opcional --cutoff permite retirar el campo por completo
desde un paso de adición declarado, manteniendo la regla restante.

## Datos aportados y reanálisis

Los archivos de data/ son copias exactas, verificadas por SHA256:

| Archivo | Contenido |
|---|---|
| [supplied_growth_trace.csv](data/supplied_growth_trace.csv) | 560 filas: 40 pares y siete tamaños, de 50 a 3200 sitios |
| [supplied_final_runs.csv](data/supplied_final_runs.csv) | 80 realizaciones finales: 40 por condición, a 3200 sitios |
| [supplied_unpaired_comparison.csv](data/supplied_unpaired_comparison.csv) | Comparación original; sus intervalos remuestrean condiciones por separado |

El protocolo aportado usa A=6, τ=300, β=3, el mismo flujo
random.Random(1000+run) por pareja y selección sobre una frontera almacenada como
set. Se validaron unicidad y correspondencia de identificadores, cobertura de
los siete tamaños, igualdad entre cada última traza y su fila final y las medias
de la comparación original. No se volvieron a ejecutar las 80 trayectorias de
3200 sitios durante esta integración.

### Proximidad morfológica a tamaño finito

Las medias originales coinciden con el recálculo. Los intervalos siguientes son
un **reanálisis nuevo**, por percentiles, con 4000 remuestreos de los 40 pares y
semilla de bootstrap 42. La diferencia es con sesgo menos sin sesgo.

| Descriptor final | Sin sesgo | Con sesgo | Diferencia | IC exploratorio 95 % por pares |
|---|---:|---:|---:|---:|
| M2 | -0,00007704 | 0,00013001 | 0,00020705 | [-0,00066918; 0,00108411] |
| Q4 | 0,13878741 | 0,13907567 | 0,00028826 | [-0,00056846; 0,00118358] |
| Aspecto | 1,01570629 | 1,01353600 | -0,00217030 | [-0,00657139; 0,00220811] |
| Compactación | 0,95240825 | 0,95355357 | 0,00114531 | [-0,00667758; 0,00886853] |
| Perímetro | 268,75 | 271,35 | 2,60 | [-0,50; 5,70] |

M2 es la media angular de cos(2θ), Q4 el módulo de la media de exp(4iθ), con
coordenadas centradas en el centroide y omitiendo los puntos coincidentes con él.
El aspecto es lado mayor/lado menor de la caja envolvente, la compactación es
sitios ocupados/área de esa caja, y el perímetro cuenta aristas de cuatro vecinos.
Los primeros cuatro descriptores son adimensionales; el perímetro se expresa en
aristas de la red.

El remuestreo elige identificadores de pareja y conserva juntas sus dos
condiciones. Eso respeta el uso de flujos pseudoaleatorios emparejados. Las
diferencias entre intervalos nuevos y originales son metodológicas, no cambios
en los datos aportados. Son intervalos exploratorios por descriptor, sin ajuste
de cobertura simultánea. Que incluyan cero no prueba equivalencia. Un ensayo de
equivalencia requiere márgenes y protocolo definidos antes de observar el
resultado.

### Anisotropía firmada y amplitud entre realizaciones

M2 puede cancelarse al promediar signos opuestos. El reanálisis informa por
separado la media firmada, la media del valor absoluto y la raíz cuadrática media
(RMS) entre realizaciones.

| Condición y tamaño | Media firmada M2 | Media de \|M2\| | RMS de M2 |
|---|---:|---:|---:|
| Con sesgo, 50 sitios | 0,71420551 | 0,71420551 | 0,71445962 |
| Con sesgo, 3200 sitios | 0,00013001 | 0,00158212 | 0,00183512 |
| Sin sesgo, 3200 sitios | -0,00007704 | 0,00155943 | 0,00195696 |

Los tres cálculos documentan una fuerte disminución de este descriptor
direccional en el ensamble con sesgo. El porcentaje de descenso de su media
firmada no mide el porcentaje de información histórica perdido.

El informe aportado declara Jaccard microscópico medio 0,976287 y 0/40 pares
idénticos. Esos dos resultados permanecen **reportados, no recalculados**: los CSV
contienen descriptores, no las listas de sitios necesarias para verificarlos.
Las nuevas ejecuciones sí conservan esas listas y calculan ambos diagnósticos.

## Módulo reproducible

[scripts/transient_bias_growth.py](scripts/transient_bias_growth.py) deriva del
código aportado y define un nuevo protocolo, ordered-frontier-v1. Ordena
lexicográficamente candidatos y sitios antes de las operaciones que dependen
del orden. Mantiene la ley de probabilidades, pero cambia el acoplamiento entre
números pseudoaleatorios y sitios frente al orden del set original. Por ello un
mismo identificador de azar no garantiza la misma trayectoria que el código
aportado. Se registran versión de Python, NumPy y parámetros para cada ejecución.

Además del orden determinista, el módulo incorpora remuestreo por pares,
separación de las tres estadísticas de M2, corte exacto opcional del campo,
diagnósticos de microestado y validación de entradas. No necesita pandas.

Desde la raíz del repositorio:

~~~shell
python 07_emergence_laboratory/growth/scripts/transient_bias_growth.py --reanalyze-supplied
python 07_emergence_laboratory/growth/scripts/transient_bias_growth.py
~~~

El primer comando sólo lee y verifica los CSV aportados. El segundo ejecuta una
prueba rápida nueva: 8 pares, 400 sitios, τ=37,5, A=6 y β=3. Escalar τ por
400/3200 conserva la razón tamaño final/τ, pero no convierte el ensayo pequeño
en una reproducción del de 3200 sitios. Ninguno escribe archivos por defecto.

Para una retirada exacta del campo y exportación explícita a una carpeta nueva:

~~~shell
python 07_emergence_laboratory/growth/scripts/transient_bias_growth.py --cutoff 100 --output-dir internal/growth_runs/cutoff_100
~~~

Se guardan resumen JSON, filas finales, trazas, comparación por pares, resúmenes
de M2, diagnósticos por pareja y listas de sitios. Nunca se sobrescriben archivos
existentes. Si se quiere repetir la escala original con el protocolo nuevo:

~~~shell
python 07_emergence_laboratory/growth/scripts/transient_bias_growth.py --n-runs 40 --n-sites 3200 --decay-tau 300 --seed 1000
~~~

Ese comando genera un **nuevo** ensamble y puede tardar más; no es el utilizado
para certificar los CSV históricos.

### Verificación local de esta integración

El 6 de octubre de 2026 pasaron ocho pruebas automatizadas: geometría y simetría,
repetibilidad y conectividad, corte exacto, remuestreo emparejado, cancelación de
signos, integridad de los CSV, exportación explícita sin sobrescritura y CLI sin
escrituras por defecto.

También se ejecutó el ensayo rápido de 8 pares y 400 sitios con 1000 remuestreos
(Python 3.12.14, NumPy 2.3.5): Q4 medio 0,12190681 sin sesgo y 0,12010586 con
sesgo; Jaccard medio 0,93535104 y 0/8 pares exactamente iguales. Es un control de
ejecución y una observación del protocolo nuevo, no una réplica confirmatoria.

~~~shell
python -B -m unittest discover -s tests -p test_seed_bias_growth.py -v
~~~

## Contrastes siguientes

1. Declarar un margen de proximidad por descriptor y contrastarlo en ensambles
   nuevos, con incertidumbre por parejas.
2. Aumentar tamaños y variar fuerza, duración y retirada exacta del campo.
3. Cambiar la regla radial y la simetría del medio para separar lo impuesto por la
   regla de lo que persiste entre reglas.
4. Elegir consultas futuras y probar si dos microestados con descriptores próximos
   tienen distribuciones de continuación próximas. La similitud de cinco números
   no acredita por sí sola suficiencia contextual.

## Trazabilidad de fuentes

El código deriva de experiment_seed_independence_crystal.py y la interpretación
de los datos se contrastó con rosi_seed_independence_report.md. Los nombres
históricos se conservan aquí para rastrear los archivos, no como nombres del
módulo integrado.

| Fuente | SHA256 |
|---|---|
| Código aportado | 2b283384f857bcbc2c0cdd02c4174e806e119c2782c001a239d45f4cf2ec66c2 |
| Informe aportado | 2e75dc51130c459de0bcc276f758e02f7a43db9e9b2dfee4841c0f32f0467da6 |
| Traza aportada | 2f090ce8f9828f64af922eee69b9db661053c8c15f1dc8dd8baaeaa4f3202edb |
| Finales aportados | 81b17b0eb7540529c0a834f1aa0001f0ed773914b1a5d6329091c22811f912d2 |
| Comparación original no emparejada | da42f19afdf917e836ea6876258f950f68388bcd53f9ddabf24baac5868fb20b |
