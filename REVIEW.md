# Invitación a revisar y desarrollar el programa

**For international reviewers:** focused reviews in English or Spanish are welcome. Choose a question below, cite the relevant statement, and share a derivation, reproducible calculation, or proposed extension through this repository's Issues. Contributions are assessed by their evidence and stated scope.

El programa reúne resultados sobre información suficiente, composición, extensión reflexiva y comparación de tasas, junto con laboratorios computacionales y físicos. Buscamos revisión que ayude a verificar estos aportes, precisar su alcance y convertir las siguientes preguntas en resultados utilizables.

Cada revisión puede ser pequeña y completa: comprobar una identidad, reproducir un ejemplo, precisar una hipótesis o construir un caso nuevo. La invitación está abierta; la revisión externa y sus conclusiones se documentarán cuando existan, con su autoría y alcance.

## Siete puntos de entrada

| ID y especialidad | Pregunta concreta | Entregable útil |
|---|---|---|
| **R1 · Información y cápsulas**. Información, lógica, sistemas de restricciones. | ¿La cápsula conserva las distinciones necesarias para la familia de contextos declarada? ¿Cómo se comprueba su suficiencia? | Prueba de suficiencia con hipótesis explícitas, ejemplo mínimo o implementación contrastada con enumeración. |
| **R2 · Extensión reflexiva**. Álgebra y representaciones. | ¿Qué supuestos llevan a $J^2=-I$ y qué minimalidad satisface el módulo real correspondiente? | Verificación de la construcción, clasificación de sus casos y formulación precisa de la minimalidad. |
| **R3 · Fase, medida y realización**. Sistemas dinámicos, probabilidad y geometría. | ¿Cómo se conectan las dieciséis firmas de dos coordenadas de fase, la medida $1:15$ y las transiciones realizables bajo sus respectivos supuestos? | Cálculo reproducible de la representación y la medida; construcción explícita de las transiciones y condiciones para preservar la estructura. |
| **R4 · Recierre MF63B y complejidad**. Algoritmos, compilación de conocimiento y pruebas. | ¿Qué representaciones realizan `Join`, `Project`, `Normalize`, `Empty` y `Read` con costos controlados? | Familia concreta con cotas de tamaño, tiempo y certificados; reproducción del contador truncado o de otra cápsula suficiente. |
| **R5 · Amplificación de vorticidad**. PDE, turbulencia y análisis numérico. | ¿Qué términos físicos mantienen el giro durante el crecimiento y cómo se verifica la ley en $G$ mediante un presupuesto independiente? | Derivación revisada o cálculo separado de deformación, viscosidad y forzamiento, con cierre del presupuesto y estudio de convergencia. |
| **R6 · $SU(2)$ y coercividad**. Teoría gauge y desigualdades funcionales. | ¿Qué comparaciones controlan la varianza en una medida y un sector definidos, y cómo dependen sus constantes de la escala? | Verificación del observable de incompatibilidad o cota de Poincaré en un sistema definido, con dependencias explícitas. |
| **R7 · Tasas, radio y observables**. Física matemática y modelado. | ¿Qué escala espacial independiente permite contrastar la relación entre radio y tasa en cada realización? | Definición operacional de escala y tasa, chequeo dimensional y predicción contrastable en un modelo o conjunto de datos. |

## Dónde empieza cada revisión

- **R1:** [Información, cierre y cápsulas](02_formal_core/closure_information.es.md).
- **R2:** [Extensión reflexiva](02_formal_core/reflexive_extension.es.md).
- **R3:** [Fase y medida](02_formal_core/phase_measure.es.md).
- **R4:** [Interfaces suficientes y recierre](02_formal_core/compatible_reclosure.es.md) y [rama computacional](05_computation/README.md).
- **R5:** [Laboratorio Navier–Stokes](03_navier_stokes/README.md), [manuscrito](03_navier_stokes/manuscript.md) y [procedencia de datos](03_navier_stokes/data/README.md).
- **R6:** [Rama Yang–Mills](06_yang_mills/README.md).
- **R7:** [Puentes físicos](publication/physical_bridges.es.md).

## Cómo entregar una revisión

Abra un **Issue** del repositorio con la plantilla «Revisión de un resultado» y el ID correspondiente. Identifique el archivo y la sección, formule la pregunta y adjunte el argumento o la evidencia que permita comprobar su conclusión. Si hay código, incluya el comando y el entorno necesario para reproducirlo.

Una observación que precisa una hipótesis y una reproducción que confirma un cálculo son aportes distintos y ambos son valiosos. En cada caso registraremos qué se revisó, con qué método y hasta dónde llega el resultado. Las ampliaciones pueden proponerse como un Issue o un pull request siguiendo [CONTRIBUTING](CONTRIBUTING.md).

La revisión de una parte se atribuye a esa parte. El reconocimiento de contribuciones se acordará con sus autores; una participación puntual no se presentará como aval externo del programa completo.
