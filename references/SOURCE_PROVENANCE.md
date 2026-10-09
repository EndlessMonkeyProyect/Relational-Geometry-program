# Procedencia de la edición para revisión

Esta edición integra los materiales suministrados por el autor y la rama Navier–Stokes del repositorio. Los documentos de desarrollo se usaron como fuentes de contenido; sus instrucciones para otras conversaciones y sus recomendaciones de trabajo se trataron como material documental. Las evaluaciones internas no equivalen a revisión externa.

| Fuente suministrada | Aporte incorporado |
|---|---|
| Núcleo integrado del Programa de Geometría Relacional, versión 1.0, 2 de octubre de 2026 | Información, cápsulas, extensión reflexiva, identidad, incertidumbre y agenda física |
| Hilo canónico de cierre, localidad y escala relacional, versión 1 | Fronteras suficientes, composición y cadena condicional hacia tasas y escala |
| MF63B recierre acreditado de compatibilidad, versión 1 | Prueba de composición exacta y formulación de acreditación |
| Auditoría MF63B, versión 1 | Precisión del alcance semántico y del objetivo de complejidad |
| Continuidad P vs NP del programa relacional, versión 1 | Cápsulas, contador truncado y programa de descenso acreditado |
| Continuidad Yang–Mills del programa relacional, versión 1 | Testigo Q8, observable SU(2), descriptor de red y programa de coercividad |
| Control gaussiano U1 por bloques | Cálculo matricial reproducible y comparación con variantes masivas |
| Ediciones públicas fuente 2.0.0, español e inglés | Representación de fase de segundo orden, medida invariante, pruebas finitas y puentes físicos |
| Repositorio público previo, versión 1.0.0 | Dinámica de comparadores, laboratorio Navier–Stokes, datos derivados y bibliografía |

## Decisiones de integración

### Ampliación del 5 de octubre de 2026

La ontología pasa a ser el punto de entrada, y los desarrollos se integran por contenido, no como una secuencia de códigos de trabajo.

| Material aportado | Destino y tratamiento |
|---|---|
| Ontología canónica ampliada v0.3 | [Diferencia, cierre e incorporación](../01_foundations/ontology_of_difference_and_closure.es.md): separa hipótesis generativa, definiciones, realizaciones y mapas físicos |
| Acción relacional, comparación de acciones y contenido de cierre (MF65–67) | [Acción y fase](../02_formal_core/relational_action_and_phase.es.md): coordenadas canónicas, interpolación declarada y contenido uniforme |
| Factores armónicos primitivos (MF69) | [Herencia y novedad](../02_formal_core/harmonic_inheritance_and_novelty.es.md): clasificación aritmética y realización por valuaciones |
| Normalización causal y cierre global (MF44B) | [Propagación y recursos](../02_formal_core/causal_propagation_and_closure_resources.es.md): localidad, interfaz y costo de acreditación |
| Novedad irreducible y operador de incorporación (MF70–71) | [Incorporación y modos](../02_formal_core/novelty_incorporation_and_dynamical_modes.es.md): espacios finitos con pesos positivos, acoplamiento y criterio espectral |
| Estructura transversal de incorporación (MF72) | [Control global](../02_formal_core/novelty_and_global_control.es.md): dos criterios cuantitativos condicionales, analítico y algorítmico |
| Canonicidad del comparador local (MF73) | [Comparadores y Laplaciano](../02_formal_core/local_comparators_and_relational_laplacian.es.md): teorema escalar gráfico, hipótesis de simetría y compatibilidad de ciclos |
| Parche de presupuesto Navier–Stokes | [Presupuesto instantáneo](../03_navier_stokes/docs/instantaneous_budget.md), scripts y trece tablas CSV aportadas; controles pequeños ejecutados localmente |

La integración corrige normalizaciones, explicita hipótesis y añade pruebas reproducibles. La identidad $K=\Gamma C^\dagger C$ exige productos internos declarados; estabilidad oscilatoria y periodicidad exacta se distinguen; la clasificación aritmética atribuye el teorema clásico de divisores primitivos. Las condiciones globales no se presentan como soluciones de Yang–Mills o P vs NP.

Las tablas del parche se conservan sin modificar sus valores. Su reproducción completa de producción se distingue de los controles ejecutados en esta edición. La precisión, la resolución y el significado de las estadísticas se documentan en la nota del presupuesto.

El historial de exploración y las auditorías de rutas permanecen internos. La exposición pública conserva las condiciones necesarias para interpretar justamente cada resultado.

La exposición principal sigue los resultados y sus preguntas de revisión. Cada nota matemática es autosuficiente para comprobar el argumento que presenta. Los originales y los registros de trabajo se conservan en el archivo local del autor; la distribución pública se genera a partir de una selección explícita de archivos.

En la forma hermítica compleja se explicita la conjugación: $B(fg,h)=B(f,\overline g h)$. La composición retiene las variables que usarán factores posteriores. La acreditación computacional se formula con certificados disponibles y verificables. Se distingue la capacidad de cuatro bits del índice de profundidad de una construcción.

El número protónico se mantiene como objetivo documental de un puente condicional, y la revisión de antecedentes queda identificada en su alcance. La integración v3 añade fuentes puntuales para el radio protónico, la frecuencia hiperfina y el contraste MICROSCOPE, sin reivindicar prioridad universal.

## Huellas de las fuentes suministradas

SHA-256 de los nueve archivos originales, para identificar exactamente el material integrado:

```text
FE31C698FB18478AD931657542D3FB3FBF0894D30AB40A620752E62EB5169F9F  AUDITORIA_MF63B_v1.md
954E3115A4B0DB85D7A73F7C71B09FDAE281BA6C4DA4294EEDB10B465F192088  MF63B_recierre_acreditado_compatibilidad_v1.md
7D03158162BAB197A125460B578DE2217B01BCD26ADE8C4E124AD1C7D6170C83  Nucleo_integrado_programa_geometria_relacional_v1_0.docx
1819D198F0787A6888636E2FED06110791822FF3C814EC932F5EFB1DF2CE5A2D  Hilo_canonico_cierre_localidad_escala_relacional_v1.md
FAFB5AA4604554E31CCCDC442590A70FD73E1804BC2BE8E9D316A17CBF13B6CC  control_gaussiano_U1_bloques.py
3AF2B29A7D76A14CD8097685B3D01BD42F42E0A93B2B6A7AAA45D8A8C959AA23  continuidad_P_vs_NP_programa_relacional_formalizada_v1.md
35C32DE4B08A1DFF8A8609AC3D5383DB4C9520CAD0B41C88FF0265696C6FAE58  continuidad_Yang_Mills_programa_relacional_formalizada_v1.md
2D6032A28B38B523E720CBFF48CCEDE738CF24BD46E273BA71E451987D25564A  relational_geometry_program_public_v2_0_0.zip
DFD773F972D44695504F6EE21742201ACB0B51D0A7F5BE869332E6165F3E7BC6  relational_geometry_program_public_v2_0_0_EN.zip
```

SHA-256 de las once fuentes distintas de la ampliación. Los códigos se conservan aquí sólo como referencias de procedencia; los archivos públicos tienen nombres descriptivos.

| Referencia de fuente | SHA-256 |
|---|---|
| Ontología v0.3 (las dos copias aportadas coinciden) | 1CF85778D78844FDD69CC92D2573DA70F3B7F23224DD5DFDFA9AC39139941F43 |
| MF44B | A077BAFC51F008522A6B37203A600D47FB62706C9FBFD8F652BA78BE36B7FEFC |
| MF65 | 535BDB8938A6FCBDC4B0BCE3B354FB7D04F9E23A1A863589B5DACC40DC98718E |
| MF66 | B6FC259AE4582B7ECD48263E51C3F6A8B5438188BE9914AE57B89206527B9F40 |
| MF67 | 58941E0D14854C6BA633A618D3541CF4C59C985CE7115C0B126824775CFFAA83 |
| MF69 | DD8BFEC2B3006186EA7D1A51A6184A59C3317E47245E12ED1F7F6B6290C36AEC |
| MF70 | C6A749D3ABB9DCC758F2629D8D6292907D090067A6E58976294A63D35B332B6C |
| MF71 | 3B41A76FBAEA76B63DA81EC8D871594A609C227881A0066D0D1D166EA0E545DB |
| MF72 | AA2DBC2C97F43ADC9E191702B9AC4A03ED5AE7E7B1B9BDB3F1CEADA39A05091A |
| MF73 | EB1224BD048062F5F2406394F9548A01E8148617054CC44C50DD584756B69140 |
| Parche de presupuesto Navier–Stokes | 704A5F7C17AB679C44C908B001221259042006A7B4E6109EB3BE6FF9894CDF29 |

## Integración canónica local 2.4 — 6 de octubre de 2026

La revisión editorial del 6 de octubre incorpora las precisiones del autor sobre identidad, notación, cierre y puentes físicos. Las versiones previas y auditorías se preservan localmente; la distribución presenta los resultados vigentes con sus condiciones. Esta revisión no incorpora nuevos datos externos.

Se integraron los contratos de identidad, independencia, comparación y acreditación desde el corpus del autor. La exposición pública contiene las formulaciones autosuficientes seleccionadas; sus archivos de trabajo se preservan por separado.

Las bibliografías externas existentes se conservan en [EXTERNAL_SOURCES](EXTERNAL_SOURCES.md). Esa integración anterior no actualizó constantes; las referencias externas añadidas en v3 se identifican a continuación.


## Integración pública v3 — 9 de octubre de 2026

La edición integra resultados seleccionados de la revisión 5.9 y del lenguaje LV2. Los dos documentos aportados como LV2 y LV2.1 coinciden byte por byte. La revisión de contenido se concentra en cierre contextual, comparación finita, control uniforme y los desarrollos de resolución, espines, SAT y correspondencias físicas. No se importa en bloque el archivo fuente.

| Desarrollo | Destino público |
|---|---|
| Interfaz, congruencia y recursos | [Recierre y costo](../02_formal_core/contextual_reclosure_and_resource_cost.es.md) |
| Contrato finito y selección modal | [Comparación finita](../02_formal_core/finite_comparison_contract_and_modal_weights.es.md) |
| Control relativo y escala | [Control uniforme](../02_formal_core/relative_closure_and_uniform_control.es.md) |
| Resolución respecto de la referencia | [Resolución y pesos](../02_formal_core/resolution_and_modal_weights.es.md) |
| Composición de espines | [Información relacional en espines](../publication/spin_composition_and_relational_information.es.md) |
| Economía contextual SAT | [Representación y costo](../05_computation/contextual_sat_and_representation_cost.es.md) |
| Correspondencias y validación | [Protón](../publication/proton_radius_hypothesis.es.md), [gravedad](../publication/composition_dependent_gravity_constraints.es.md), [protocolo químico](../07_emergence_laboratory/chemistry/validation_protocol.es.md) |

Huellas SHA-256 de los paquetes fuente preservados por el autor:

- Revisión 5.9: 39EF7F8EEC742844CCCBCE2F0B1CF0983915838D420828D922FBAB58684E2470.
- Paquete LV2: 80B16BDAAFFE7FB1571A8AE1D67DD221EC177791C27FE34AA2A2990F6C9ABAB4.
- Documento de lenguaje LV2: 63FA79605434E3E873420FB931914B12EE9060A3E5A99DAAE9A139A0A1C42AFC.

Las notas físicas enlazan fuentes primarias específicas: Trinhammer–Bohr (2019), CODATA 2022, Kramida (2010) y MICROSCOPE (2022). Los valores se identifican por su fuente y fecha, sin presentarlos como predicciones nuevas del programa. El [informe de reproducción](../04_results/REPRODUCTION_REPORT.md) delimita la verificación ejecutada.
