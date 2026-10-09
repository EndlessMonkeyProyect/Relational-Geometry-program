# Invitación a revisar y desarrollar el programa

**For international reviewers:** focused reviews in English or Spanish are welcome. Choose a question below, cite the relevant statement, and share a derivation, reproducible calculation, or proposed extension through this repository's Issues. Contributions are assessed by their evidence and stated scope.

El programa reúne resultados sobre información suficiente, composición, extensión reflexiva y comparación de tasas, junto con laboratorios computacionales y físicos. Buscamos revisión que ayude a verificar estos aportes, precisar su alcance y convertir las siguientes preguntas en resultados utilizables.

Cada revisión puede ser pequeña y completa: comprobar una identidad, reproducir un ejemplo, precisar una hipótesis o construir un caso nuevo. La invitación está abierta; la revisión externa y sus conclusiones se documentarán cuando existan, con su autoría y alcance.

## Trece puntos de entrada

| ID y especialidad | Pregunta concreta | Entregable útil |
|---|---|---|
| **R1 · Información y cápsulas**. Información, lógica, sistemas de restricciones. | ¿La cápsula conserva las distinciones necesarias para la familia de contextos declarada? ¿Cómo se comprueba su suficiencia? | Prueba de suficiencia con hipótesis explícitas, ejemplo mínimo o implementación contrastada con enumeración. |
| **R2 · Extensión reflexiva**. Álgebra y representaciones. | ¿Qué supuestos llevan a $J^2=-I$ y qué minimalidad satisface el módulo real correspondiente? | Verificación de la construcción, clasificación de sus casos y formulación precisa de la minimalidad. |
| **R3 · Fase, medida y realización**. Sistemas dinámicos, probabilidad y geometría. | ¿Cómo se conectan las dieciséis firmas de dos coordenadas de fase, la medida $1:15$ y las transiciones realizables bajo sus respectivos supuestos? | Cálculo reproducible de la representación y la medida; construcción explícita de las transiciones y condiciones para preservar la estructura. |
| **R4 · Recierre de compatibilidad y complejidad**. Algoritmos, compilación de conocimiento y pruebas. | ¿Qué representaciones realizan `Join`, `Project`, `Normalize`, `Empty` y `Read` con costos controlados? | Familia concreta con cotas de tamaño, tiempo y certificados; reproducción del contador truncado o de otra cápsula suficiente. |
| **R5 · Amplificación de vorticidad**. PDE, turbulencia y análisis numérico. | ¿Qué términos físicos mantienen el giro durante el crecimiento y cómo se verifica la ley en $G$ mediante un presupuesto independiente? | Derivación revisada o cálculo separado de deformación, viscosidad y forzamiento, con cierre del presupuesto y estudio de convergencia. |
| **R6 · $SU(2)$ y coercividad**. Teoría gauge y desigualdades funcionales. | ¿Qué comparaciones controlan la varianza en una medida y un sector definidos, y cómo dependen sus constantes de la escala? | Verificación del observable de incompatibilidad o cota de Poincaré en un sistema definido, con dependencias explícitas. |
| **R7 · Tasas, radio y observables**. Física matemática y modelado. | ¿Qué escala espacial independiente permite contrastar la relación entre radio y tasa en cada realización? | Definición operacional de escala y tasa, chequeo dimensional y predicción contrastable en un modelo o conjunto de datos. |
| **R8 · Comparadores e incorporación**. Grafos, álgebra lineal y análisis espectral. | ¿Qué axiomas seleccionan el comparador local y cuándo una distinción nueva se convierte en un modo dinámico nuevo? | Verificación de la factorización por incidencia, del bloque de acoplamiento y de los criterios espectrales en una familia explícita. |
| **R9 · Acción y contenido de cierre**. Mecánica discreta y teoría de la medida. | ¿Qué mapa conecta el contenido de firmas con el invariante canónico de un modo estable? | Construcción de un mapa que preserve las operaciones declaradas y distinga período, fase y acción. |
| **R10 · Herencia y factores primitivos**. Teoría de números. | ¿Cómo se articula la clasificación de factores nuevos en $2^n-1$ con firmas informativas y reglas de composición? | Revisión de la clasificación, extensión aritmética o realización formal que especifique qué estructura conserva. |
| **R11 · Identidad y dinámica colectiva**. Álgebra, información y sistemas dinámicos. | ¿Qué contrato hace suficiente una interfaz y cuándo porta por sí misma la evolución? | Contrato independiente, prueba de congruencia o invariancia del núcleo, y comparación entre canales visibles y modos ocultos. |
| **R12 · Representación predictiva en química**. Química de datos y validación estadística. | ¿Cuánto aporta la coordenada compacta frente a otras representaciones al separar selección y evaluación? | Trazabilidad bibliográfica de las energías, réplica LOEO y contraste independiente o anidado de fórmulas prefijadas. |
| **R13 · Crecimiento y memoria**. Simulación estocástica y reducción de modelos. | ¿Qué descriptores permanecen próximos bajo perturbaciones tempranas y cuáles predicen continuaciones? | Ensamble emparejado nuevo, tolerancias declaradas, estudio de tamaño y contraste entre descriptores y microestados. |

## Dónde empieza cada revisión

- **R1:** [Información, cierre y cápsulas](02_formal_core/closure_information.es.md).
- **R2:** [Extensión reflexiva](02_formal_core/reflexive_extension.es.md).
- **R3:** [Fase y medida](02_formal_core/phase_measure.es.md).
- **R4:** [Interfaces suficientes y recierre](02_formal_core/compatible_reclosure.es.md) y [rama computacional](05_computation/README.md).
- **R5:** [Laboratorio Navier–Stokes](03_navier_stokes/README.md), [manuscrito](03_navier_stokes/manuscript.md) y [procedencia de datos](03_navier_stokes/data/README.md).
- **R6:** [Rama Yang–Mills](06_yang_mills/README.md).
- **R7:** [Puentes físicos](publication/physical_bridges.es.md).
- **R8:** [Comparadores locales](02_formal_core/local_comparators_and_relational_laplacian.es.md) e [incorporación de novedad](02_formal_core/novelty_incorporation_and_dynamical_modes.es.md).
- **R9:** [Acción relacional, fase y contenido](02_formal_core/relational_action_and_phase.es.md).
- **R10:** [Herencia armónica y novedad](02_formal_core/harmonic_inheritance_and_novelty.es.md).
- **R11:** [Identidad contextual](02_formal_core/contextual_identity_and_scale_promotion.es.md), [canales informativos](02_formal_core/redistributive_closure_and_information_channels.es.md) y [dinámica en cocientes](02_formal_core/collective_dynamics_on_quotients.es.md).
- **R12:** [Coordenadas compactas y energía de enlace](07_emergence_laboratory/chemistry/README.es.md).
- **R13:** [Forma colectiva y memoria de un sesgo transitorio](07_emergence_laboratory/growth/README.es.md).

La [ontología de diferencia y cierre](01_foundations/ontology_of_difference_and_closure.es.md) conecta las rutas. Los [criterios de control global](02_formal_core/novelty_and_global_control.es.md) precisan los próximos objetivos cuantitativos de R4 y R6.

## Entradas de la edición integrada

- **R4 / R11:** [Recierre contextual y recursos](02_formal_core/contextual_reclosure_and_resource_cost.es.md): acción de continuaciones, congruencia, fibras y costos de la política completa.
- **R8 / R9:** [Contrato finito y pesos](02_formal_core/finite_comparison_contract_and_modal_weights.es.md): escala del comparador, eventos diagonales, medida y dinámica seleccionadas.
- **R5 / R6:** [Cierre relativo y control uniforme](02_formal_core/relative_closure_and_uniform_control.es.md): constantes finitas, control de escala y condiciones de paso a conclusiones globales.
- **R7:** [Puentes físicos](publication/physical_bridges.es.md): diccionario de masa, radio, frecuencia y momento, y un observable independiente para la hipótesis de comparación electromagnética.

### Nuevas conexiones de la v3

- **R3 / R8:** [Resolución y pesos](02_formal_core/resolution_and_modal_weights.es.md): métrica, referencia, composición e incidencia.
- **R4:** [SAT y representación](05_computation/contextual_sat_and_representation_cost.es.md): canonización, tamaño codificado y esquema completo de tablas.
- **R7 / R11:** [Espines](publication/spin_composition_and_relational_information.es.md): interfaz del par, continuaciones, medición y correlaciones.
- **R7:** [Protón](publication/proton_radius_hypothesis.es.md) y [gravedad](publication/composition_dependent_gravity_constraints.es.md): mapas a observables y protocolos condicionales.
- **R12:** [Protocolo químico](07_emergence_laboratory/chemistry/validation_protocol.es.md): objetivos, referencias simples y evaluación independiente.

## Cómo entregar una revisión

Abra un **Issue** del repositorio con la plantilla «Revisión de un resultado» y el ID correspondiente. Identifique el archivo y la sección, formule la pregunta y adjunte el argumento o la evidencia que permita comprobar su conclusión. Si hay código, incluya el comando y el entorno necesario para reproducirlo.

Una observación que precisa una hipótesis y una reproducción que confirma un cálculo son aportes distintos y ambos son valiosos. En cada caso registraremos qué se revisó, con qué método y hasta dónde llega el resultado. Las ampliaciones pueden proponerse como un Issue o un pull request siguiendo [CONTRIBUTING](CONTRIBUTING.md).

La revisión de una parte se atribuye a esa parte. El reconocimiento de contribuciones se acordará con sus autores; una participación puntual no se presentará como aval externo del programa completo.

## Criterios de revisión

Toda revisión debe usar [STATUS_CANONICAL](STATUS_CANONICAL.md) y separar definición, prueba condicional, realización y puente físico. Las hipótesis y el alcance forman parte de cada enunciado público; las notas de exploración permanecen internas.

Prioridades: (1) identidad como solución antes de acreditación; (2) novedad frente a producto completo; (3) minimal frente a least y costo de testigos; (4) ausencia de derivación de $b=4$; (5) $q=2n_{\rm amp}$ y puentes protónicos A/B; (6) fase frente a acción; (7) coercividad, multiescala y automatizabilidad como obligaciones distintas. El entregable debe identificar una hipótesis, comprobar una implicación o aportar un contraejemplo con dominio explícito.

No se solicita certificar experimentalmente el programa por un ajuste numérico. Para física, fijar antes mapa, parámetros y observable; para química, añadir baselines y separar selección de evaluación. [Resumen de la v3](publication/UPDATE_3_0.md).
