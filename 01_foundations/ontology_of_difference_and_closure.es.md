# Ontología de la diferencia, el cierre y la incorporación

**Le Matt Ansatz Di Ego · Programa de Geometría Relacional · Edición 2.2.0**

La propuesta del programa es que una identidad puede estudiarse por las diferencias que conserva, las comparaciones que admite y la interfaz que permite reutilizarla. Una diferencia nueva requiere ampliar la descripción; una arquitectura de comparación determina cómo responde el sistema; un cierre suficiente permite que esa estructura actúe como nueva referencia.

Este documento es el punto de entrada conceptual del programa. Las definiciones organizan la propuesta; los resultados enlazados muestran realizaciones matemáticas concretas; los puentes físicos formulan mapas a observables. Cada nivel tiene su propia justificación.

## 1. De la referencia a la información

Como hipótesis generativa, se parte de una referencia sin diferencias acreditadas, no de una colección situada de antemano en espacio y tiempo. La normalización de esa referencia a uno es una convención representacional.

Una diferencia cuenta como información cuando eliminarla haría indistinguibles dos realizaciones que el contrato exige separar. El contrato declara preguntas, contextos y transformaciones admitidos. La indeterminación reúne las respuestas pertinentes todavía no excluidas; resolverla conserva sus consecuencias en una estructura reutilizable.

Una distinción binaria tiene capacidad de un bit. Dos distinciones binarias independientes admiten cuatro respuestas conjuntas. Estos conteos expresan capacidad de identificación; dimensión geométrica y frecuencia requieren sus propias construcciones.

## 2. Cierre, interfaz e identidad

Sea $X$ el dominio de realizaciones y $\Phi:X\to\Sigma$ una firma. El cierre es suficiencia respecto del contrato: cada pregunta admitida puede responderse a partir de $\Phi$. Una identidad es un cierre persistente bajo las transformaciones declaradas; puede tener dinámica interna mientras preserve su interfaz pertinente.

Para una relación de restricciones $R(I,B)$, con interior $I$ y frontera $B$,

$$\mathcal I_B(R)=\exists I\,R(I,B)$$

conserva exactamente las asignaciones admisibles de frontera. Es suficiente para contextos que interactúan sólo por $B$ mediante restricciones de ese tipo. Retener futuras variables compartidas hace posible la [composición exacta de interfaces](../02_formal_core/compatible_reclosure.es.md).

En el programa se adopta como criterio de una identidad nueva la conservación de procedencia junto con una diferencia pertinente adicional: herencia y novedad. Este criterio orienta las realizaciones; su persistencia debe comprobarse en cada dinámica.

## 3. La novedad exige representación

Una comparación $d$ amplía la firma a $(\Phi,d)$. Aporta información nueva exactamente cuando divide alguna clase anterior, es decir, cuando no existe $\bar d$ tal que $d=\bar d\circ\Phi$.

En un dominio finito con pesos estrictamente positivos, las funciones representables por cada firma forman espacios $H\subseteq H^+$. La descomposición ortogonal

$$H^+=H\oplus N,\qquad N=H^+\cap H^\perp$$

convierte la novedad en una dirección representacional verificable: $d$ es nueva si y sólo si $N\ne0$. El [criterio de novedad](../02_formal_core/closure_information.es.md) y la [incorporación dinámica](../02_formal_core/novelty_incorporation_and_dynamical_modes.es.md) precisan estos pasos.

Esta es la lectura operacional de una extensión de dimensión: capacidad adicional para conservar información que la firma anterior no representaba.

## 4. Comparación orientada y fase

En una realización real lineal, una comparación antisimétrica que conserva la norma induce un operador $J$ con $J^2=-I$. Para $x\ne0$,

$$x\longmapsto Jx\longmapsto-x\longmapsto-Jx\longmapsto x.$$

Se obtiene un plano invariante mínimo y una órbita de cuatro fases. Dos coordenadas de fase independientemente accesibles producen dieciséis firmas. La medida normalizada e invariante les asigna peso $1/16$.

Los resultados conectan hipótesis de comparación, geometría y medida. Sus demostraciones están en [extensión reflexiva](../02_formal_core/reflexive_extension.es.md) y [fase y medida](../02_formal_core/phase_measure.es.md).

## 5. De las relaciones al operador de respuesta

Una arquitectura puede responder a diferencias mediante un comparador lineal $C$. Con productos internos declarados,

$$K=\Gamma C^\dagger C,\qquad \Gamma>0,\qquad
\langle x,Kx\rangle=\Gamma\|Cx\|^2.$$

El operador registra la respuesta a diferencias detectables. En un grafo de comparaciones binarias, linealidad, localidad e invariancia ante una referencia común fuerzan la forma

$$C=DB,\qquad K=\Gamma B^\top D^2B,$$

donde $B$ es la incidencia orientada y $D$ contiene pesos reales; la segunda igualdad usa productos internos euclídeos. Una simetría transitiva sobre aristas, respetada por las conductancias $w_e^2$, reduce $K$ a un múltiplo del Laplaciano. La [nota del comparador local](../02_formal_core/local_comparators_and_relational_laplacian.es.md) da la prueba y las libertades que permanecen.

Respecto de $H^+=H\oplus N$, el bloque $PKQ$ mide acoplamiento entre herencia y novedad. Un modo integrado tiene componentes en ambos sectores. Aparecer, acoplarse y persistir son propiedades distintas que ahora pueden comprobarse con objetos explícitos.

## 6. Recurrencia, ritmo y acción

La realización cuadrática discreta usa

$$x_{n+1}-2x_n+x_{n-1}=-Kx_n.$$

Para un autovalor $0<\kappa<4$, el modo es una rotación de fase $\Omega=\arccos(1-\kappa/2)$ por actualización. Un ritmo recurrente permite comparar cambios; un reloj físico añade una duración $\tau_0$ por actualización.

La dinámica posee una acción variacional y, en coordenadas canónicas modales, un invariante $\mathcal J=(Q_c^2+P_c^2)/2$. Sobre la interpolación circular declarada, $m$ vueltas encierran acción $2\pi m\mathcal J$. La [nota de acción y fase](../02_formal_core/relational_action_and_phase.es.md) distingue la fase, el contenido de la órbita y la curva usada para medir área.

La medida sobre firmas ofrece a su vez un contenido finito $\mathfrak J(A)=|A|J_{\rm tot}/N$. Si una realización establece $\mathcal J=\mathfrak J(A)$, selecciona amplitudes específicas. Construir ese mapa es una pregunta concreta de investigación.

## 7. Herencia aritmética y escala relativa

En la familia declarada $M_n=2^n-1$, las valuaciones primas separan factores heredados y factores que aparecen por primera vez. La [clasificación de herencia y novedad](../02_formal_core/harmonic_inheritance_and_novelty.es.md) identifica el primer caso mixto en $n=4$ y caracteriza toda la familia usando un teorema clásico de divisores primitivos.

Esta realización describe repertorios multiplicativos. Para conectarlos con modos se necesita un mapa explícito a comparaciones y un operador dinámico. La [incorporación](../02_formal_core/novelty_incorporation_and_dynamical_modes.es.md) permite preguntar si ese mapa añade dimensión, mezcla o un autovalor diferente.

Para escalas positivas $\ell_i$, la comparación relativa

$$s_i=\log(\ell_i/\ell_{\rm ref}),\qquad
(Bs)_{i\to j}=\log(\ell_j/\ell_i)$$

es independiente de una reescala global. Las razones se componen sumando sus logaritmos; la compatibilidad en ciclos determina si pueden coexistir en un cierre común.

## 8. Localidad y laboratorios

Una actualización local de radio $r$ sólo puede transmitir una diferencia a distancia de grafo $rn$ tras $n$ pasos. La [separación de recursos](../02_formal_core/causal_propagation_and_closure_resources.es.md) distingue ese transporte de la anchura de interfaces, las rondas de acreditación y el costo del cálculo.

| Laboratorio | Pregunta propia | Objeto disponible |
|---|---|---|
| [Computación](../05_computation/README.md) | ¿Cómo componer y acreditar cierres con costos controlados? | Interfaces exactas, contador truncado y condiciones de descenso |
| [Yang–Mills](../06_yang_mills/README.md) | ¿Qué comparaciones controlan cuantitativamente toda diferencia pertinente? | Observable $SU(2)$, control gaussiano y programa de coercividad |
| [Navier–Stokes](../03_navier_stokes/README.md) | ¿Qué sostiene el crecimiento y el giro de la vorticidad? | Identidades materiales y presupuesto presión–viscosidad–forzamiento |

La [estructura transversal](../02_formal_core/novelty_and_global_control.es.md) organiza estas preguntas sin identificar sus operadores ni sus conclusiones.

## 9. Mapa a observables y próxima revisión

Una realización física debe especificar cómo mide longitud, duración y acción. Si establece una escala de acción $S_0$, el área física es $S_0\mathcal A_{\rm rel}$; una fase física puede entonces escribirse como $\exp(i\mathcal A_{\rm phys}/\hbar)$. Cada cociente debe ser dimensionalmente consistente.

Los [puentes físicos](../publication/physical_bridges.es.md) estudian relaciones entre tasa, longitud y observables. El interés del programa está en la cadena de obligaciones verificables: información suficiente, representación, respuesta, recurrencia y escala medida.

### Notación de enlace

| Símbolo | Significado |
|---|---|
| $X,\Phi,\Sigma$ | Realizaciones, firma y respuestas de la firma |
| $H,N,P,Q$ | Sector heredado, novedad y sus proyecciones |
| $J$ | Operador de comparación orientada, $J^2=-I$ |
| $B,C,K$ | Incidencia de grafo, comparador y respuesta dinámica |
| $\Omega,\mathcal J,\mathfrak J$ | Fase por paso, acción modal y contenido de firmas |
| $\ell_i,\tau_0,S_0$ | Escala de longitud, duración por paso y unidad física de acción |

Procedencia: ontología ampliada v0.3 y desarrollos sobre acción, novedad y comparadores aportados por el autor, integrados en esta edición. Véase [procedencia](../references/SOURCE_PROVENANCE.md). [Preguntas de revisión](../REVIEW.md).
