# Acción relacional, forma canónica rotatoria y contenido de cierre

**Le Matt Ansatz Di Ego · Resultado exacto en la dinámica cuadrática declarada**

Esta nota conecta la recurrencia del comparador con una forma canónica explícita y un invariante de acción. Distinguir fase y contenido de la órbita permite formular con precisión el puente hacia selección de amplitudes.

## 1. Principio variacional

En un espacio real euclídeo finito, sea $K=K^\top$. Para extremos fijos,

$$\mathscr S[x]=\frac12\sum_n
\left(\|x_{n+1}-x_n\|^2-\langle x_n,Kx_n\rangle\right).$$

La variación respecto de un punto interior da

$$x_n-x_{n-1}-(x_{n+1}-x_n)-Kx_n=0,$$

y por tanto $x_{n+1}-2x_n+x_{n-1}=-Kx_n$. El funcional se toma adimensional en esta realización. La [dinámica de segundo orden](second_order_dynamics.md) incluye un paso general y el límite continuo.

Para un autovector real de norma uno, $Ku=\kappa u$, la amplitud $a_n$ satisface

$$a_{n+1}=(2-\kappa)a_n-a_{n-1}.$$

En $0<\kappa<4$, fijamos $\Omega\in(0,\pi)$ con $c=\cos\Omega=1-\kappa/2$ y $s=\sin\Omega>0$.

## 2. Forma canónica exacta

El lagrangiano modal es $L_d(a,b)=\tfrac12(b-a)^2-\tfrac\kappa2a^2$. Su momento discreto es $p_n=a_n-a_{n-1}$. Definimos

$$Q_{c,n}=\sqrt{s}\,a_n,\qquad
P_{c,n}=\frac{c\,a_n-a_{n-1}}{\sqrt{s}}
=\frac{p_n+(c-1)a_n}{\sqrt{s}}.$$

El determinante del cambio de $(a,p)$ a $(Q_c,P_c)$ vale uno; en particular

$$dQ_c\wedge dP_c=da\wedge dp.$$

Sustituir la recurrencia da

$$\binom{Q_{c,n+1}}{P_{c,n+1}}
=\begin{pmatrix}c&s\\-s&c\end{pmatrix}
\binom{Q_{c,n}}{P_{c,n}}.$$

Así, la evolución es una rotación canónica exacta y

$$\boxed{\mathcal J=\frac{Q_c^2+P_c^2}{2}
=\frac{a_n^2+a_{n-1}^2-2c\,a_na_{n-1}}{2s}}$$

es positivo para una órbita no nula e invariante por actualización. La construcción está vinculada a la normalización del lagrangiano, no sólo a la forma de la elipse.

El marco de momento y forma simpléctica discretos es estándar; véase [Marsden y West, §1.5](https://lagrange.mechse.illinois.edu/pubs/MaWe2001/MaWe2001.pdf). Aquí se explicita su realización en la recurrencia del programa.

## 3. Fase, retorno y área

Para $\mathcal J>0$, escriba $Q_c=\sqrt{2\mathcal J}\cos\theta$ y $P_c=-\sqrt{2\mathcal J}\sin\theta$. Entonces $\theta_{n+1}=\theta_n+\Omega$ módulo $2\pi$.

Hay retorno exacto tras $T$ pasos si $T\Omega=2\pi m$ para algún entero $m$. La estabilidad oscilatoria y la periodicidad exacta son propiedades distintas: esta última requiere una fase racional respecto de $2\pi$.

Declaramos la interpolación circular $\theta(t)=\theta_0+\Omega t$. Sobre $m$ vueltas,

$$\boxed{\mathcal A_{\rm circ}=\oint P_c\,dQ_c=2\pi m\mathcal J}.$$

La prueba es integrar $2\mathcal J\sin^2\theta\,d\theta$. Si se elige en cambio la interpolación por segmentos entre los mismos $T$ puntos, el área orientada, contada con multiplicidad, es

$$\mathcal A_{\rm pol}=T\mathcal J\sin\Omega.$$

Estas convenciones especifican qué área se calcula. Para una vuelta de cuatro pasos son $2\pi\mathcal J$ y $4\mathcal J$.

## 4. Contenido aditivo de firmas

Sea $\Sigma$ un conjunto de $N$ firmas, con acción transitiva de un grupo. Supóngase que $\mathfrak J$ es no negativo, aditivo sobre subconjuntos disjuntos, invariante bajo el grupo y normalizado por $\mathfrak J(\Sigma)=J_{\rm tot}$.

La transitividad iguala el contenido de cada singleton a $j_0$. La aditividad da $Nj_0=J_{\rm tot}$, luego

$$\boxed{\mathfrak J(A)=|A|J_{\rm tot}/N}.$$

La medida de [dieciséis firmas](phase_measure.es.md) es el caso $N=16$ con normalización unitaria. El teorema fija contenido relativo en un soporte declarado.

## 5. Selección condicional de amplitudes

Si una realización construye un mapa de órbitas a subconjuntos $A\subseteq\Sigma$ y demuestra $\mathcal J=\mathfrak J(A)$ con $N,J_{\rm tot}$ fijos, entonces

$$\mathcal J=\frac{k}{N}J_{\rm tot},\qquad
Q_c^2+P_c^2=2\frac{k}{N}J_{\rm tot},\qquad k=0,\ldots,N.$$

Es un criterio exacto de selección finita bajo esa compatibilidad. La tarea es construir el mapa preservando contenido, composición y simetrías, independientemente de los valores que se pretende seleccionar. Una interfaz que determina $\mathcal J$ debe conservar información sobre amplitud además de fase.

Una escala física $S_0$ convierte $\mathcal J$ y $\mathcal A_{\rm circ}$ en magnitudes de acción. Su identificación con constantes físicas pertenece al [puente a observables](../publication/physical_bridges.es.md).

## 6. Revisión y controles

Las pruebas en [acción y estructura armónica](../tests/test_action_and_harmonic_structure.py) verifican el cambio canónico, la rotación, la invariancia, áreas y contenidos en ejemplos. Las demostraciones anteriores tienen alcance general bajo sus hipótesis.

Procedencia: integración corregida de los desarrollos de acción variacional, acción simpléctica y contenido de cierre del autor. [Ontología](../01_foundations/ontology_of_difference_and_closure.es.md).
