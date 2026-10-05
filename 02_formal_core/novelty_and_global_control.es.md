# Incorporación de novedad y condiciones de control global

**Le Matt Ansatz Di Ego · Arquitectura transversal y resultados condicionales**

El programa distingue registrar una diferencia, incorporarla a una representación y controlar sus consecuencias globales. Esta estructura organiza preguntas comunes, mientras cada dominio conserva sus objetos y sus criterios de éxito.

## 1. Núcleo compartido

En la realización finita de [incorporación](novelty_incorporation_and_dynamical_modes.es.md), una comparación nueva produce $H^+=H\oplus N$. Un comparador definido independientemente de la conclusión buscada determina $K=C^\dagger C\ge0$; el bloque $PKQ$ mide mezcla entre sectores.

El principio programático es conservar herencia y novedad en una interfaz reutilizable. Para convertirlo en un teorema global hay que especificar qué significa residuo, qué regla actúa sobre él y qué cota controla el resultado.

## 2. Control analítico: detección y coercividad

Sea $\rho$ una probabilidad, con forma relacional $\mathcal D[f]=\|Cf\|^2$ sobre un dominio declarado. Para $f$ centrado, suponga

$$\operatorname{Var}_\rho(f)\le A\,\mathcal D[f],
\qquad \mathcal D[f]\le B\,\mathcal E[f].$$

Entonces, por composición,

$$\boxed{\operatorname{Var}_\rho(f)\le AB\,\mathcal E[f]}.$$

Si $\mathcal E$ es la forma cerrada de un generador autoadjunto no negativo con núcleo de constantes, esta cota da un gap de al menos $1/(AB)$ en el sector ortogonal a constantes.

En una familia de sistemas, un resultado uniforme requiere controlar $A$ y $B$ uniformemente. El núcleo identifica qué se detecta; la cota mide con qué intensidad se controla. En dimensión finita, un núcleo correcto da una constante para ese sistema, que todavía puede deteriorarse al aumentar el tamaño.

La [rama Yang–Mills](../06_yang_mills/README.md) debe declarar medida, sector gauge-invariante, forma física y límites continuo/volumen. El Laplaciano escalar de un grafo es una realización de referencia, no una sustitución del comparador gauge.

## 3. Control algorítmico: descenso con longitud acotada

Sea una entrada de longitud $n$ y un estado acreditado de tamaño polinómico. Suponga:

1. Un potencial entero no negativo $\Delta$ con $\Delta_0\le p(n)$.
2. $\Delta=0$ implica una decisión correcta con certificado recuperable.
3. Para todo estado alcanzable no terminal, una política uniforme construye y verifica un paso en tiempo $q(n)$ y reduce $\Delta$ al menos en uno.
4. La política conserva el tamaño polinómico, incluye el costo de evaluar su información y no dispone de un oráculo para la decisión buscada.

**Teorema condicional.** El proceso termina en a lo sumo $p(n)$ pasos y tiempo $O(p(n)q(n))$, además del costo polinómico de inicialización y lectura del resultado.

Prueba: el potencial no puede descender más de $\Delta_0$ veces sin alcanzar cero. Sumar el costo de cada paso da la cota.

Un potencial real estrictamente decreciente necesita una condición adicional para dar esta conclusión, por ejemplo un decremento mínimo con cociente inicial/decremento polinómico. Un orden bien fundado garantiza terminación pero requiere también una cota de longitud para establecer eficiencia.

En [computación](../05_computation/README.md), la energía $\|C_{\rm acr}x\|^2$ puede ser un ingrediente candidato junto con profundidad, anchura y memoria. Definirla exige elegir una representación, productos internos y operaciones efectivamente construibles. La existencia de una representación semántica suficiente y el costo de encontrar el siguiente paso son obligaciones distintas.

## 4. Correspondencias útiles

| Capa | Yang–Mills | Computación |
|---|---|---|
| Objeto pertinente | Función o diferencia gauge-invariante | Restricción, respuesta o compatibilidad lógica |
| Comparador | Forma relacional en un dominio analítico | Operación acreditable en una representación finita |
| Control cuantitativo | Constantes coercivas y comparación de formas | Tamaño, costo por paso y número de pasos |
| Escala o límite | Volumen, malla y dinámica física | Longitud de entrada y uniformidad del algoritmo |
| Revisión siguiente | Construir el comparador y estimar sus constantes | Construir la política y acotar recursos |

La correspondencia es metodológica: no afirma equivalencia entre problemas, identidad de operadores ni transferencia automática de soluciones.

## 5. Preguntas que conectan el programa

¿Qué invariancias del contrato restringen el comparador? ¿Qué información debe conservar una interfaz para componerlo? ¿Cómo cambia el control al incorporar nuevos sectores?

El [teorema del comparador local](local_comparators_and_relational_laplacian.es.md) resuelve una realización escalar concreta, y la [separación de recursos](causal_propagation_and_closure_resources.es.md) identifica qué aporta la localidad. Estos objetos permiten organizar revisiones específicas y comparables.

Procedencia: integración de los desarrollos del autor sobre incorporación y estructura transversal, con condiciones cuantitativas explícitas. [Ontología del programa](../01_foundations/ontology_of_difference_and_closure.es.md).
