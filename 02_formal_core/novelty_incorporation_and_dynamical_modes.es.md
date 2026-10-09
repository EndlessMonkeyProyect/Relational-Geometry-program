# Incorporación de novedad y modos dinámicos

**Le Matt Ansatz Di Ego · Representación finita y dinámica lineal declarada**

La novedad describe qué información requiere una nueva representación. La incorporación estudia cómo esa información participa en la respuesta y la recurrencia de una arquitectura. Esta distinción une el criterio informacional del programa con operadores calculables.

## 1. Ampliación representacional

Sea $X$ finito con pesos $\mu(x)>0$ y producto interno $\langle f,g\rangle=\sum_x\mu(x)f(x)g(x)$. Dada una firma $\Phi:X\to\Sigma$, defina

$$H=\{f:f=\bar f\circ\Phi\},\qquad
H^+=\{f:f=\bar f\circ(\Phi,d)\},\qquad N=H^+\cap H^\perp.$$

Entonces $H^+=H\oplus N$. Además,

$$\boxed{d\text{ no factoriza por }\Phi\iff N\ne0}.$$

Prueba: si $d$ factoriza, las particiones y sus espacios de funciones coinciden. Si divide una fibra, el indicador de una nueva clase pertenece a $H^+$ pero no a $H$; su proyección ortogonal residual es no nula. La positividad de los pesos impide que esa distinción desaparezca en norma.

[DERIVADO] La dimensión añadida al espacio de funciones es el incremento del número de clases realizables. [DEFINICIÓN] Una coordenada independiente del dominio exige además imagen producto completa; ese requisito no se sigue del incremento representacional. La [nota de información](closure_information.es.md) desarrolla el criterio sin requerir dinámica.

## 2. Operador de respuesta

Fije un comparador lineal $C:H^+\to Y$, productos internos y $\Gamma>0$:

$$K=\Gamma C^\dagger C,\qquad
\langle x,Kx\rangle=\Gamma\|Cx\|^2,\qquad
\ker K=\ker C.$$

La respuesta es positiva semidefinida y está determinada una vez declarado el comparador y su escala. La [construcción local en grafos](local_comparators_and_relational_laplacian.es.md) restringe la elección de $C$ desde axiomas explícitos.

Sean $P,Q$ las proyecciones a $H,N$. Con $P+Q=I$,

$$K=\begin{pmatrix}A&M\\M^\dagger&D\end{pmatrix},\qquad M=PKQ:N\to H.$$

El bloque $M$ mide intercambio lineal entre ambos sectores. La recurrencia considerada es $x_{n+1}-2x_n+x_{n-1}=-Kx_n$.

## 3. Autonomía y acoplamiento

Por autoadjunción,

$$[K,Q]=\begin{pmatrix}0&M\\-M^\dagger&0\end{pmatrix}.$$

Así son equivalentes: $[K,Q]=0$, $M=0$, invariancia de $H$ e invariancia de $N$. Las dos capas iniciales en un sector permanecen allí exactamente bajo esa autonomía.

La cantidad $\alpha_{\rm inc}=\|M\|$ es un diagnóstico de mezcla relativo a los productos internos elegidos. Cuando el denominador es positivo,

$$\eta_{\rm inc}=\frac{\|M\|}{\sqrt{\|A\|\|D\|}}$$

permite comparar la fuerza relativa del acoplamiento. Para $K\ge0$, Cauchy–Schwarz en la forma de $K$ da $\|M\|^2\le\|A\|\|D\|$, por lo que $0\le\eta_{\rm inc}\le1$. Es un cociente de normas, no una probabilidad.

Un autovector $u$ es integrado respecto de esta descomposición si $Pu\ne0$ y $Qu\ne0$. Un bloque $M\ne0$ garantiza que alguna dirección espectral mezcla sectores, pero su recurrencia y el contrato de identidad todavía deben examinarse. En un autovalor degenerado pueden elegirse vectores mixtos incluso cuando $M=0$; por eso se informa el acoplamiento además del vector.

## 4. Ritmo estable y espectro

Para $Ku=\kappa u$, la amplitud satisface $a_{n+1}=(2-\kappa)a_n-a_{n-1}$. En

$$0<\kappa<4,\qquad
\Omega(\kappa)=\arccos(1-\kappa/2)\in(0,\pi),$$

las raíces características son distintas y de módulo uno. Cada solución modal es acotada y tiene la [forma canónica rotatoria](relational_action_and_phase.es.md). El retorno exacto exige además $\Omega/(2\pi)\in\mathbb Q$.

Los extremos $\kappa=0,4$ tienen raíces repetidas y soluciones genéricas con crecimiento lineal en $n$. Fuera de $[0,4]$ existe una dirección exponencialmente creciente y otra decreciente. Estas afirmaciones clasifican soluciones de la recurrencia, no estabilidad física de partículas.

Si $M=0$, escriba $\Sigma_H=\operatorname{spec}(A)$, $\Sigma_N=\operatorname{spec}(D)$. Un nuevo ritmo oscilatorio autónomo aparece exactamente cuando

$$\boxed{(\Sigma_N\setminus\Sigma_H)\cap(0,4)\ne\varnothing}.$$

La función $\Omega(\kappa)$ es inyectiva en esa banda. Un nuevo sector puede también aumentar la multiplicidad de un ritmo ya presente.

## 5. Ejemplo de incorporación calculable

Con $H=\operatorname{span}(e_1)$, $N=\operatorname{span}(e_2)$ y

$$K=\begin{pmatrix}2&b\\b&2\end{pmatrix},\qquad 0<|b|<2,$$

los autovalores $2+b,2-b$ están en la banda estable, y los vectores $(1,1)/\sqrt2$, $(1,-1)/\sqrt2$ son integrados. El acoplamiento determina dos fases distintas. Como $K>0$, existe un comparador $C=K^{1/2}$ para $\Gamma=1$; para obtenerlo desde relaciones primitivas hay que declarar la arquitectura, como hace la nota gráfica.

Este ejemplo separa con claridad representación, mezcla y recurrencia. Una identidad persistente añade un contrato que esa evolución conserve.

## 6. Escala y aplicaciones

Un mapa físico puede asignar $\omega=\Omega/\tau_0$ y una longitud $\ell=v_*/\omega$; esos parámetros requieren significado operacional. La [rama aritmética](harmonic_inheritance_and_novelty.es.md) aporta firmas y valuaciones; conectarlas con $C$ exige un mapa acreditado, no sólo etiquetar autovalores.

Las [condiciones de control global](novelty_and_global_control.es.md) distinguen la aplicación analítica y la computacional. La ontología orienta la cadena; las reglas de cada dominio determinan sus resultados.

Pruebas: [comparadores e incorporación](../tests/test_comparators_and_incorporation.py). Procedencia: desarrollos del autor sobre novedad representacional y operador de incorporación, integrados con hipótesis finitas explícitas.
