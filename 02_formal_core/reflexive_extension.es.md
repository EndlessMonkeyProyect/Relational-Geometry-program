# Extensión reflexiva mínima y cierre de cuatro fases

## Hipótesis y resultado

Sea $V$ un espacio real finito-dimensional con producto interno y $J:V\to V$ lineal. Supóngase que la comparación $B(x,y)=\langle Jx,y\rangle$ es antisimétrica y que $J$ conserva la norma de todo vector.

La antisimetría implica $J^*=-J$. La preservación de norma y la polarización implican $J^*J=I$. Por tanto,

$$(-J)J=I,\qquad J^2=-I,\qquad J^4=I.$$

Además, $\langle n,Jn\rangle=0$ y $\|Jn\|=\|n\|$. Si $n\ne0$, los cuatro vectores $n,Jn,-n,-Jn$ son distintos y constituyen una órbita de longitud exactamente cuatro.

Esto conecta dos hipótesis precisas sobre la comparación con una geometría local: igual norma, ortogonalidad y cierre de fase. La revisión física se concentra en determinar qué sistemas realizan esas hipótesis.

## El módulo mínimo

Defina

$$M_J(n)=\operatorname{span}_{\mathbb R}\{J^r n:r\ge0\}=\operatorname{span}_{\mathbb R}\{n,Jn\}.$$

Si $Jn=\lambda n$ con $\lambda\in\mathbb R$, aplicar $J$ daría $-n=\lambda^2n$, imposible para $n\ne0$. Así, $\dim_{\mathbb R}M_J(n)=2$. Este plano es $J$-invariante, y todo subespacio $J$-invariante que contiene $n$ contiene también $Jn$: es la extensión invariante mínima generada por la novedad.

## Conservar lo heredado

Sea $H\subseteq V$ la información representada, $P$ su proyección ortogonal y $n=(I-P)q$ el residuo de una comparación. Si $PJ=JP$, entonces $J(I-P)=(I-P)J$. En consecuencia, $n,Jn\in H^\perp$ y, para $n\ne0$,

$$H^+=H\oplus M_J(n).$$

La conmutación es la condición que hace compatible la extensión con el sector heredado. La fórmula describe la actualización dada una comparación $q$; una dinámica especifica cómo selecciona esa comparación.

## Fase continua y representación completa

La identidad $J^2=-I$ permite calcular directamente

$$e^{\theta J}=\cos\theta\,I+\sin\theta\,J.$$

Esta interpolación tiene período $2\pi$. El plano rotatorio es una parte de la representación completa de funciones sobre las cuatro fases. Para $\mathcal H_4=\mathbb R^{\mathbb Z_4}$ y $(Pf)(a)=f(a-1)$,

$$\mathcal H_4=H_{\rm const}\oplus H_{\rm alt}\oplus H_{\rm rot},$$

con dimensiones $1,1,2$ y acciones $+I,-I,J$. Conservar los tres sectores mantiene todas las preguntas sobre las cuatro fases.

Procedencia: *Núcleo integrado*, §§11–17, y edición pública fuente 2.0.0, construcción $C_4$. El [desarrollo de segundo orden](phase_measure.es.md) construye dos coordenadas de fase. [Revisión R2](../REVIEW.md).
