# Computación: interfaces suficientes y cierres reutilizables

La rama computacional desarrolla una forma de resolver y componer problemas conservando en cada frontera la información que sigue siendo relevante. Su resultado estructural es un recierre exacto: la compatibilidad entre dos bloques puede convertirse en una nueva interfaz y participar en la siguiente composición.

Esta arquitectura conecta una pregunta concreta —qué información necesita el contexto exterior— con otra computacional —cuánto cuesta construir, almacenar y utilizar esa información—. La documentación ofrece identidades demostradas, un caso económico completo y un objetivo preciso para investigar la decisión de 3-SAT.

## Resultados disponibles

| Resultado | Qué permite | Alcance |
|---|---|---|
| Interfaz $\Gamma_R(B)=\exists I\,R(I,B)$ | Conservar exactamente las realizaciones posibles de frontera | Relaciones booleanas; contextos conectados sólo por la frontera declarada |
| Compatibilidad $K_{AB}=B_A\land B_B$ | Componer bloques a partir de sus interfaces | Interiores disjuntos y frontera común explícita |
| Recierre $\exists I\,K_{AB}$ | Usar la composición como entrada de una nueva capa | Proyección exacta; conservación de variables todavía necesarias |
| Asociación semántica | Elegir órdenes de composición con la misma relación exterior | Frontera final fija y eliminación válida |
| Contador truncado | Acumular y combinar información suficiente de umbral | Bloques disjuntos; representación por capas de $O(n(k+1))$ nodos |

Las pruebas completas están en [Interfaces suficientes y recierre exacto](../02_formal_core/compatible_reclosure.es.md).

## La composición en una fórmula

Para bloques $F_A(X,S)$ y $F_B(S,Y)$ con interiores disjuntos:

$$
\underbrace{(\exists X\,F_A)\land(\exists Y\,F_B)}_{\text{compatibilidad de interfaces}}
=\underbrace{\exists X,Y\,(F_A\land F_B)}_{\text{interfaz del sistema compuesto}}.
$$

Si parte de $S$ pasa a ser interior, se cuantifica de nuevo sobre ella. La nueva relación conserva exactamente la información que ve la frontera restante. Esto permite construir una jerarquía de cierres con una misma regla de composición.

En una implementación, una cápsula es la representación elegida para esa relación. El contrato operacional comprende:

- `Join`: combinar relaciones compatibles en sus variables compartidas;
- `Project`: eliminar variables interiores preservando la relación exterior;
- `Normalize`: convertirla a la representación admitida;
- `Empty`: decidir si tiene alguna realización;
- `Read`: recuperar la respuesta o el testigo especificado por el contrato.

Cada familia de cápsulas debe declarar el tamaño de su representación y el costo de estas operaciones. Así se puede comparar una misma idea de suficiencia en distintos lenguajes y algoritmos.

## Caso completo: una cápsula contador

Para decidir $x_1+\cdots+x_n\le k$, con bits $x_i$ y $0\le k\le n$, basta conservar:

$$
q_i=\min\left(k+1,\sum_{j=1}^{i}x_j\right).
$$

El estado indica la suma exacta mientras importa para el umbral y conserva una única marca cuando ya se superó. Para cualquier continuación común, dos prefijos con el mismo estado producen la misma respuesta. Esta es una memoria suficiente verificable.

La transición $q\mapsto\min(k+1,q+x)$ tiene a lo sumo $k+2$ estados por capa. Para bloques disjuntos, la operación:

$$
q_A\oplus_k q_B=\min(k+1,q_A+q_B)
$$

es asociativa. El ejemplo realiza las tres propiedades buscadas: suficiencia, reutilización y costo acotado. Su prueba y sus cotas, incluido $k=0$, se encuentran en la [sección del contador](../02_formal_core/compatible_reclosure.es.md#5-una-realización-económica-contador-truncado).

## Acreditación: progreso que puede comprobarse

La segunda línea de trabajo estudia cómo una arquitectura construye evidencia reutilizable. Un estado operativo conserva relaciones, sus certificados y los cierres ya disponibles. Una regla puede añadir una relación $r$ cuando un verificador declarado acepta su certificado $w$:

$$
\operatorname{Verify}_{\mathcal D}(A,r,w)=1.
$$

En la versión operativa, «acreditado» significa que el certificado está disponible y ha sido verificado. La búsqueda de ese certificado es una tarea adicional cuyo costo se registra. Esto permite describir el progreso mediante evidencia efectivamente construida.

Una referencia de extensión $z_r\leftrightarrow r$ permite compartir una representación y su derivación. Una estructura DAG conserva una sola copia y agrega enlaces a ella. Su utilidad se mide por el trabajo que evita y por las operaciones que permite realizar después.

La distinción entre novedad de una firma y progreso de acreditación ofrece una pregunta de investigación concreta: ¿puede una consecuencia ya determinada por el problema reducir el trabajo pendiente cuando se dispone de una derivación reutilizable?

## Objetivo de complejidad

El siguiente objetivo es construir un sistema uniforme de recierre, con reglas verificables y una política explícita, que decida toda 3-CNF manteniendo cotas polinómicas en el tamaño de entrada para:

- la memoria y el número total de pasos;
- la selección de cada paso y la generación de sus certificados;
- las operaciones de las cápsulas, las bifurcaciones y la lectura final.

Una construcción con estas propiedades daría un algoritmo polinómico para 3-SAT y, por su NP-completitud, establecería $P=NP$. En el estado presentado, esa construcción universal es el objetivo abierto; los resultados disponibles fijan su semántica de composición y sus obligaciones operacionales.

El **Lema de Descenso Acreditado** propone una vía verificable: encontrar un entero $\Delta(A,Q)$, calculable desde el estado explícito, tal que $0\le\Delta\le p(N)$, el valor cero acredite la respuesta y una política uniforme encuentre en tiempo polinómico un paso que lo reduzca siempre que sea positivo. Si cada paso añade tamaño polinómico y preserva lo acreditado, habrá a lo sumo $p(N)$ pasos. La construcción de ese potencial y de esa política es la parte pendiente.

## Revisión solicitada

Buscamos revisión en composición relacional, compilación de conocimiento, algoritmos de restricciones y complejidad de pruebas. Hay tareas abordables con resultados independientes:

- verificar las demostraciones y los contratos de frontera de esta rama;
- reproducir el contador y proponer otras familias con interfaces económicas;
- implementar un formato de certificados y medir por separado construcción, verificación y reutilización;
- estudiar una política concreta y demostrar su cota sobre una familia explícita;
- ensayar la misma política en familias estructuradas y mezclas de restricciones, registrando tamaño de interfaces, certificados, pasos y bifurcaciones.

Para entregar observaciones o proponer una colaboración, véase [Revisión del programa](../REVIEW.md).

Procedencia: *MF-63B — Recierre acreditado de compatibilidad*, §§2–5, 7–9, 12–15; *Programa Relacional — Rama P vs NP*, §§5–12 y 16–27. Estas notas públicas reúnen y precisan el contenido de esas fuentes; no representan una certificación externa.
