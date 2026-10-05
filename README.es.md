# Programa de Geometría Relacional

**De la diferencia al cierre: información, incorporación, dinámica y escala**

Le Matt Ansatz Di Ego · [English](README.md) · [Invitación a revisión](REVIEW.md)

El Programa de Geometría Relacional desarrolla un lenguaje común para una pregunta concreta: **¿qué información debe conservar un sistema para distinguir estados, mantener su identidad y componerse con otros sistemas?** Su punto de partida son las diferencias y comparaciones; desde ellas construye las representaciones necesarias para conservar información.

El aporte es una arquitectura conceptual acompañada de resultados matemáticos explícitos y laboratorios computacionales. Permite conectar preguntas sobre información y geometría con objetos que se pueden calcular, verificar y ampliar. Este repositorio busca hacer visibles esas contribuciones y facilitar la revisión de sus conexiones y aplicaciones.

La [ontología de la diferencia, el cierre y la incorporación](01_foundations/ontology_of_difference_and_closure.es.md) organiza la lectura: una diferencia requiere representación; una arquitectura de comparación determina una respuesta; la dinámica permite estudiar recurrencia y persistencia; un mapa a observables da significado físico a la escala.

**Actualización 2.2.0-review · 5 de octubre de 2026.** Se integran comparadores locales, incorporación de novedad, acción y fase, clasificación armónica y un presupuesto computacional de vorticidad. [Qué incorpora esta edición](publication/UPDATE_2_2.md).

La edición anterior 2.1.0-review está [archivada en Zenodo](https://doi.org/10.5281/zenodo.23123168). Ese DOI identifica el depósito anterior, no esta actualización de GitHub.

## Aportes principales

| Aporte | Resultado | Importancia |
|---|---|---|
| **Información y cierre** | Una firma agrupa estados según las preguntas que pueden responder. Una comparación aporta información nueva exactamente cuando no factoriza por la firma anterior. | Ofrece un criterio operacional de novedad y descripción suficiente. |
| **Extensión reflexiva mínima** | Una comparación lineal antisimétrica que conserva la norma induce $J^2=-I$. Una novedad no nula genera un plano real mínimo y una órbita de cuatro fases. | Conecta reglas de comparación explícitas con dimensión, ortogonalidad y cierre de fase. |
| **Dieciséis firmas y medida invariante** | Dos coordenadas de cuatro fases accesibles independientemente producen $\mathbb Z_4^2$. La medida local normalizada e invariante da $1/16$ a una firma y $15/16$ a su complemento. | Explicita la cadena entre estructura de fase, conteo y medida, con hipótesis revisables. |
| **Composición exacta de cápsulas** | Unir relaciones compatibles y eliminar variables interiores conserva la relación completa accesible desde la frontera. | Da una base para componer restricciones y reutilizar interfaces en computación. |
| **Comparador local y respuesta** | Localidad, linealidad e invariancia de referencia fuerzan diferencias ponderadas en un grafo; su forma cuadrática es un Laplaciano ponderado. | Conecta relaciones declaradas con un operador calculable, razones de escala y compatibilidad de ciclos. |
| **Incorporación y acción** | El bloque entre herencia y novedad mide mezcla; los modos en la banda estable admiten una rotación canónica y un invariante de acción. | Separa nueva información, acoplamiento, ritmo y contenido de una órbita. |
| **Herencia armónica** | La familia de firmas multiplicativas tiene una clasificación completa en factores heredados y primitivos, apoyada en aritmética clásica. | Hace comprobable el criterio de repetición y ampliación de repertorio. |
| **Observables y presupuesto de Navier–Stokes** | Identidades exactas separan amplificación y giro; el nuevo laboratorio calcula presión, viscosidad y forzamiento por separado. | Añade tablas DNS aportadas y controles reproducibles de cierre, precisión y resolución, con alcance documentado. |
| **Observable relacional no abeliano** | Un observable del conmutador en $SU(2)$ cuantifica cuánto dejan de conmutar dos holonomías. | Aporta un objeto calculable y una ruta precisa hacia preguntas de coercividad en Yang–Mills. |

El alcance acompaña a cada aporte: las afirmaciones algebraicas incluyen sus hipótesis; los cálculos incluyen su protocolo; las interpretaciones físicas identifican el mapa a observables que debe revisarse. El [registro de resultados](04_results/RESULTS_REGISTER.md) enlaza cada contribución con su desarrollo.

## Por dónde entrar

- **Para conocer la propuesta:** [ontología rectora](01_foundations/ontology_of_difference_and_closure.es.md), [presentación breve](publication/PROGRAM_OVERVIEW.es.md) y [núcleo integrado](publication/relational_geometry_core.es.md).
- **Para revisar las pruebas:** [información y cierre](02_formal_core/closure_information.es.md), [extensión reflexiva](02_formal_core/reflexive_extension.es.md), [fases y medida](02_formal_core/phase_measure.es.md) y [teorema de composición](02_formal_core/compatible_reclosure.es.md).
- **Para explorar aplicaciones:** [computación](05_computation/README.md), [Navier–Stokes](03_navier_stokes/README.md), [Yang–Mills](06_yang_mills/README.md) y [objetivos físicos](publication/physical_bridges.es.md).
- **Para seguir la actualización:** [comparadores locales](02_formal_core/local_comparators_and_relational_laplacian.es.md), [incorporación y modos](02_formal_core/novelty_incorporation_and_dynamical_modes.es.md), [acción y fase](02_formal_core/relational_action_and_phase.es.md), [novedad armónica](02_formal_core/harmonic_inheritance_and_novelty.es.md) y [control global](02_formal_core/novelty_and_global_control.es.md).
- **Para aportar una revisión:** elija una [pregunta concreta](REVIEW.md). Verificar una prueba, una implementación o un puente físico ya es una contribución útil.

El programa propone una arquitectura compartida; cada dominio aporta sus objetos, hipótesis y evidencia. Las cotas de complejidad, la selección dinámica de comparaciones y la conversión de medida formal en observables físicos constituyen objetivos de investigación definidos.

## Reproducibilidad

Con Python 3.11 o posterior, desde la raíz del repositorio:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python 03_navier_stokes/scripts/restricted_euler_benchmark.py
python 03_navier_stokes/scripts/review_checks.py
python 06_yang_mills/scripts/gaussian_control.py --quick
python tools/public_release.py
```

Las pruebas comprueban ejemplos finitos, consistencia algebraica e integridad de la distribución. Las demostraciones y sus hipótesis están en los documentos. Véanse el [estado del programa](STATUS.md), la [guía de colaboración](CONTRIBUTING.md) y los [términos de uso](NOTICE.md).
