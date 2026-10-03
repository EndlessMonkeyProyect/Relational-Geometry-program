# Programa de Geometría Relacional

**Cómo la información distinguible sostiene geometría, identidad y composición**

Le Matt Ansatz Di Ego · [English](README.md) · [Invitación a revisión](REVIEW.md)

El Programa de Geometría Relacional desarrolla un lenguaje común para una pregunta concreta: **¿qué información debe conservar un sistema para distinguir estados, mantener su identidad y componerse con otros sistemas?** Su punto de partida son las diferencias y comparaciones; desde ellas construye las representaciones necesarias para conservar información.

El aporte es una arquitectura conceptual acompañada de resultados matemáticos explícitos y laboratorios computacionales. Permite conectar preguntas sobre información y geometría con objetos que se pueden calcular, verificar y ampliar. Este repositorio busca hacer visibles esas contribuciones y facilitar la revisión de sus conexiones y aplicaciones.

## Aportes principales

| Aporte | Resultado | Importancia |
|---|---|---|
| **Información y cierre** | Una firma agrupa estados según las preguntas que pueden responder. Una comparación aporta información nueva exactamente cuando no factoriza por la firma anterior. | Ofrece un criterio operacional de novedad y descripción suficiente. |
| **Extensión reflexiva mínima** | Una comparación lineal antisimétrica que conserva la norma induce $J^2=-I$. Una novedad no nula genera un plano real mínimo y una órbita de cuatro fases. | Conecta reglas de comparación explícitas con dimensión, ortogonalidad y cierre de fase. |
| **Dieciséis firmas y medida invariante** | Dos coordenadas de cuatro fases accesibles independientemente producen $\mathbb Z_4^2$. La medida local normalizada e invariante da $1/16$ a una firma y $15/16$ a su complemento. | Explicita la cadena entre estructura de fase, conteo y medida, con hipótesis revisables. |
| **Composición exacta de cápsulas** | Unir relaciones compatibles y eliminar variables interiores conserva la relación completa accesible desde la frontera. | Da una base para componer restricciones y reutilizar interfaces en computación. |
| **Observables de Navier–Stokes** | Identidades exactas separan amplificación de vorticidad y cambio de orientación; una ley expresa la evolución transversal por unidad de crecimiento logarítmico. | Proporciona diagnósticos medibles y una pregunta concreta sobre presión, viscosidad y forzamiento. |
| **Observable relacional no abeliano** | Un observable del conmutador en $SU(2)$ cuantifica cuánto dejan de conmutar dos holonomías. | Aporta un objeto calculable y una ruta precisa hacia preguntas de coercividad en Yang–Mills. |

El alcance acompaña a cada aporte: las afirmaciones algebraicas incluyen sus hipótesis; los cálculos incluyen su protocolo; las interpretaciones físicas identifican el mapa a observables que debe revisarse. El [registro de resultados](04_results/RESULTS_REGISTER.md) enlaza cada contribución con su desarrollo.

## Por dónde entrar

- **Para conocer la propuesta:** [presentación breve](publication/PROGRAM_OVERVIEW.es.md) y [núcleo integrado](publication/relational_geometry_core.es.md).
- **Para revisar las pruebas:** [información y cierre](02_formal_core/closure_information.es.md), [extensión reflexiva](02_formal_core/reflexive_extension.es.md), [fases y medida](02_formal_core/phase_measure.es.md) y [teorema de composición](02_formal_core/compatible_reclosure.es.md).
- **Para explorar aplicaciones:** [computación](05_computation/README.md), [Navier–Stokes](03_navier_stokes/README.md), [Yang–Mills](06_yang_mills/README.md) y [objetivos físicos](publication/physical_bridges.es.md).
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
