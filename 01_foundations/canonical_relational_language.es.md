# Lenguaje canónico: cierre, resolución y composición

**Le Matt Ansatz Di Ego · v3.0.0-review**

El programa parte de una pregunta común: **¿qué debe conservar una descripción
para seguir siendo suficiente cuando participa en nuevas relaciones?** Este
documento conecta la ontología, los resultados formales y las aplicaciones.
Las pruebas y los contratos completos están en las notas enlazadas.

## 1. De la ontología al objeto formal

La [ontología de diferencia y cierre](ontology_of_difference_and_closure.es.md)
propone totalidad, referencia, reflexión y diferencia como orden conceptual.
La totalidad no es un objeto contado ni una magnitud física. La diferencia
precede a su representación numérica; la comparación permite reconocerla.

En el desarrollo matemático se declara un conjunto de estados, preguntas,
continuaciones y operaciones. Esta elección proporciona una realización de
la idea ontológica: sus propiedades se deducen de ese contrato explícito.

Una **singularidad relacional** es una diferencia cerrada reutilizable como
unidad. El término no significa una divergencia de una ecuación ni una
singularidad gravitatoria. **Recierre** designa su participación resuelta en
una nueva comparación.

## 2. Cierre suficiente, composición y residuo

Para una pregunta Q y continuaciones c admitidas, la equivalencia contextual es

$$x\equiv_Q y\iff Q(x\cdot c)=Q(y\cdot c)\quad\text{para todo }c.$$

El cociente conserva exactamente las distinciones de ese contrato. Una
interfaz suficiente determina su clase; una composición se define sobre
clases cuando respeta la equivalencia de sus entradas.

Al ampliar las preguntas aparece una proyección del cociente fino al grueso.
Sus fibras identifican las distinciones que el contrato fino todavía conserva.
En el caso finito, la mayor fibra determina el tamaño mínimo de un alfabeto
residual que permita reconstruir la clase fina junto con la gruesa.
[Pruebas de recierre y recursos](../02_formal_core/contextual_reclosure_and_resource_cost.es.md).

Un residuo contextual es relativo a esas preguntas. Interpretarlo como energía,
radiación o un grado de libertad físico exige especificar el sistema y su dinámica.

## 3. Resolución respecto de una referencia

En una realización finita de N alternativas, represente un estado mediante
probabilidades p, con producto interno euclídeo y dirección uniforme
$u=(1,\ldots,1)/\sqrt N$. Defina

$$C_2(p)=\sum_i p_i^2,\qquad
\mathcal R(p)=\log_2(NC_2(p)).$$

La proyección sobre u determina exactamente

$$\boxed{r_{\rm ref}=\frac1{NC_2(p)}=2^{-\mathcal R(p)}}.$$

El complemento es el espacio de suma cero, también imagen de la incidencia
de un grafo conexo sobre las alternativas. Para una distribución completamente
concentrada, $\tan^2\theta=N-1$ coincide con el rango de esa incidencia.

En estados uniformes sobre M alternativas, $r_{\rm ref}=M/N$. Si $N/M=2^n$,
se obtiene una realización de peso $2^{-n}$. En composiciones independientes,
la resolución se suma y el peso se multiplica. Para registros binarios, las
paridades de Walsh dan una base explícita de comparaciones.
[Contrato, demostraciones y versión cuántica](../02_formal_core/resolution_and_modal_weights.es.md).

La reflexión asociada es una operación del espacio vectorial de comparación.
Una preparación o evolución física debe además preservar su dominio de estados.
La métrica, el espacio y la preparación pertenecen al modelo.

## 4. Una realización cuántica concreta

Para dos espines preparados independientemente con vectores de Bloch n y m,

$$P(F=1)=\frac{3+n\cdot m}{4}.$$

El producto escalar es una interfaz suficiente del par para esa pregunta.
Para reutilizar un espín frente a cualquier compañero, el contrato conserva
su vector de Bloch. El singlete muestra estructura en correlaciones con
marginales de máxima mezcla; la quiralidad de tres espines aporta una consulta
ternaria adicional a los productos escalares de parejas.

Son resultados en mecánica cuántica estándar organizados mediante el lenguaje
del programa. Estados, probabilidades, registros medidos y transiciones físicas
tienen tipos distintos. La [nota de espines](../publication/spin_composition_and_relational_information.es.md)
los construye explícitamente, incluyendo el ejemplo hiperfino con frecuencia
tomada de una fuente experimental.

## 5. La economía de una realización

Construir, almacenar, actualizar y consultar una interfaz son tareas distintas.
Se cuentan también la política de continuaciones y sus representaciones.

Para el contrato de CNF con frontera nombrada, una realización canónica
uniformemente polinómica existe si y sólo si P=NP. Esta caracterización fija
el alcance del blanco computacional. El lenguaje de tablas densas proporciona
otro resultado concreto: en un esquema completo sin reducción de ámbitos,
el mayor mensaje tiene $2^{w^*}$ entradas, donde $w^*$ es la anchura inducida.
[Caracterización y controles finitos](../05_computation/contextual_sat_and_representation_cost.es.md).

## 6. Notación tipada

| Símbolo o término | Objeto declarado |
|---|---|
| Clase contextual $[x]_Q$ | Respuestas invariantes bajo las continuaciones del contrato |
| Singularidad relacional | Unidad de comparación reutilizable en el lenguaje ontológico |
| Residuo contextual | Fibra de una proyección entre contratos refinados |
| $C_2(p)$ | Autocoincidencia de una distribución |
| $\mathcal R$ | Resolución definida mediante autocoincidencia o pureza |
| $r_{\rm ref}$ | Peso geométrico de proyección respecto de una referencia |
| $p_A$ | Probabilidad de un evento A |
| $P(F)$ | Probabilidad de un sector de espín para un estado cuántico |
| $r_V^{\rm freq}$ | Razón de frecuencias al cuadrado en un puente físico |
| $r_V^{\rm chem}$ | Descriptor de ocupaciones electrónicas del laboratorio |
| $q$ | Exponente modal adoptado en $r_V^{\rm freq}=2^{-q}$ |
| Radio relacional | Escala de distinguibilidad que requiere un mapa para convertirse en observable |

Los índices de profundidad, bits, dimensión y orden de un operador se definen
por separado. Una coincidencia numérica puede motivar una correspondencia;
la correspondencia se acredita especificando las operaciones que preserva.

## 7. Papel de las ramas y próxima revisión

Los [comparadores y modos](../02_formal_core/novelty_incorporation_and_dynamical_modes.es.md)
y la [dinámica colectiva](../02_formal_core/collective_dynamics_on_quotients.es.md)
construyen respuestas bajo condiciones explícitas. Las ramas de fluidos y
teoría gauge necesitan sus propias cotas y límites. Química y crecimiento
declaran datos, representaciones y protocolos de evaluación.

Los [puentes físicos](../publication/physical_bridges.es.md) fijan qué magnitud
formal se compara con qué observable. La luz como primer espacio físico de
comparación permanece como hipótesis organizadora; el protón y la gravedad
tienen notas de correspondencia y contraste específicas.

La [v3](../publication/UPDATE_3_0.md) conecta estas piezas sin convertir una
aplicación en aval de todas las demás. El [registro de resultados](../04_results/RESULTS_REGISTER.md)
y las [rutas de revisión](../REVIEW.md) permiten elegir un aporte concreto,
comprobarlo y extenderlo.
