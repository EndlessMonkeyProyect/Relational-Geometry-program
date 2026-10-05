# Comparadores locales, Laplaciano relacional y compatibilidad de escalas

**Le Matt Ansatz Di Ego · Teorema en el sector gráfico lineal**

Una arquitectura de comparaciones binarias restringe la forma de su comparador. El resultado permite pasar de relaciones declaradas a una respuesta cuadrática, con pesos y normalización identificados explícitamente.

## 1. Hipótesis y forma local

Sea $\mathcal G=(V,E)$ un grafo finito sin lazos, con una orientación convencional por arista. Se usan productos internos euclídeos en $\mathbb R^V$ y $\mathbb R^E$. Un comparador $C:\mathbb R^V\to\mathbb R^E$ cumple:

1. Linealidad.
2. Localidad: $(Cf)_{i\to j}$ depende sólo de $f_i,f_j$.
3. Invariancia de referencia: $C(f+c\mathbf1)=Cf$.
4. Covariancia de orientación: reorientar una arista cambia el signo de su respuesta.

**Teorema.** Existen pesos reales $w_e$ tales que

$$\boxed{(Cf)_{i\to j}=w_e(f_j-f_i),\qquad C=DB},$$

donde $(Bf)_{i\to j}=f_j-f_i$ y $D=\operatorname{diag}(w_e)$.

Prueba: linealidad y localidad dan $a_ef_i+b_ef_j$. La invariancia sobre constantes exige $a_e+b_e=0$. Tomar $w_e=b_e$ da la fórmula; la covariancia especifica cómo se representa al reorientar. Las tres primeras hipótesis ya fuerzan la diferencia ponderada.

## 2. Respuesta, núcleo y simetría

Con $W=D^2$ y $\Gamma>0$,

$$K=\Gamma C^\top C=\Gamma B^\top WB,\qquad
f^\top Kf=\Gamma\sum_e w_e^2(f_j-f_i)^2.$$

Por tanto $K\ge0$ y $K\mathbf1=0$. Si las aristas de peso no nulo conectan el grafo, $\ker K=\operatorname{span}(\mathbf1)$: anular la suma obliga a igualdad en cada relación, y la conectividad propaga esa igualdad.

Si además se exige que las conductancias $w_e^2$ sean invariantes bajo un grupo de automorfismos, hay un parámetro por órbita de aristas. Si la acción es transitiva y el peso común es no nulo,

$$\boxed{K=\gamma L_{\mathcal G},\qquad L_{\mathcal G}=B^\top B,\quad\gamma=\Gamma w^2>0}.$$

Los signos de $w_e$ pueden absorberse en convenciones de salida; la conclusión sobre $K$ no depende de ellos. La simetría del grafo y la exigencia de que los pesos la respeten son hipótesis separadas.

Se usa el Laplaciano combinatorio, no el normalizado por grados. Con otros productos internos debe recalcularse el adjunto. La factorización por incidencia y sus propiedades espectrales pertenecen a la teoría estándar; véase [Chung, capítulo 1](https://fanchung.ucsd.edu/research/cb/ch1.pdf). La contribución aquí es hacer explícita su función en la arquitectura relacional.

## 3. Comparación de escalas positivas

Para $\ell_i>0$, elija una referencia $\ell_{\rm ref}$ y defina $s_i=\log(\ell_i/\ell_{\rm ref})$. Entonces

$$ (Bs)_{i\to j}=\log(\ell_j/\ell_i).$$

Una reescala global $\ell_i\mapsto\lambda\ell_i$ añade una constante a $s$ y conserva $Bs$. Las razones se componen sumando sus logaritmos.

Si una relación tiene objetivo $q_e>0$, sea $\tau_e=\log q_e$. El funcional de incompatibilidad

$$\mathcal D(s)=\tfrac12(Bs-\tau)^\top W(Bs-\tau)$$

tiene

$$\nabla\mathcal D=B^\top W(Bs-\tau),\qquad
\nabla^2\mathcal D=B^\top WB.$$

Así la arquitectura determina la respuesta cuadrática y $\tau$ especifica el objetivo de cierre. Para $W>0$ y grafo conectado, el minimizador es único módulo una constante.

## 4. Criterio exacto de compatibilidad

**Teorema.** Existe cierre exacto $Bs=\tau$ si y sólo si la suma orientada de $\tau_e$ en todo ciclo es cero; equivalentemente, el producto orientado de razones objetivo es uno.

Necesidad: las diferencias $s_j-s_i$ telescopan. Suficiencia: fije $s$ en una raíz y extiéndalo sumando $\tau$ por caminos. La condición de ciclos hace independiente la elección del camino. En un grafo conectado, todas las soluciones difieren por una constante.

Ejemplo: con aristas $1\to2$, $2\to3$, $1\to3$, los objetivos $2,3,6$ son compatibles. La solución relativa es $(\ell_1,\ell_2,\ell_3)=(1,2,6)\ell_{\rm ref}$. Cambiar el tercer objetivo a 5 deja un residuo de ciclo $\log(6/5)$, que el ajuste cuadrático puede medir.

## 5. Incorporación y alcance

Dados los sectores heredado y nuevo con proyecciones $P,Q$, el acoplamiento $PKQ$ queda calculado a partir del grafo, los pesos y esos sectores. Si las aristas de peso no nulo conectan el grafo y hay al menos dos vértices, elegir $0<\Gamma\lambda_{\max}(C^\top C)<4$ da una recurrencia oscilatoria estable en el complemento de constantes. La elección de escala dinámica se declara, no se oculta en el grafo.

El resultado obtiene $C$ a partir de una arquitectura binaria escalar lineal. Las [ramas de control global](novelty_and_global_control.es.md) deben construir sus comparadores con sus propias invariancias: gauge, lógicas o de otra naturaleza.

Pruebas: [comparadores e incorporación](../tests/test_comparators_and_incorporation.py). Procedencia: desarrollo del autor sobre canonicidad local y comparador de escala. [Ontología](../01_foundations/ontology_of_difference_and_closure.es.md).
