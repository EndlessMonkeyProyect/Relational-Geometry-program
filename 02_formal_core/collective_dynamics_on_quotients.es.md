# Dinámica colectiva y cierre exacto en cocientes

**Le Matt Ansatz Di Ego · Interfaz lineal y recurrencia de dos capas**

Integración local: 6 de octubre de 2026 · Integrado en v3.0.0-review.

Una descripción colectiva adquiere un papel dinámico preciso cuando permite continuar la evolución sin reconstruir el estado interno. Esta nota convierte esa suficiencia en una condición algebraica verificable: el operador de respuesta debe respetar las clases que identifica la interfaz.

La conexión con la [identidad contextual y promoción de escala](contextual_identity_and_scale_promotion.es.md) es directa: aquí se declara un contexto particular, formado por una dinámica lineal, una interfaz y todas las parejas iniciales posibles. El teorema utiliza el descenso estándar de operadores a cocientes; su función en el programa es articular ese resultado con la identidad colectiva, no atribuirle una prioridad matemática nueva.

## 1. Datos y significado de autonomía

Sean $V,W$ espacios vectoriales reales de dimensión finita, $T:V\to W$ lineal y sobreyectiva y $K:V\to V$ lineal. La dinámica microscópica es

$$x_{n+1}=2x_n-x_{n-1}-Kx_n,\qquad y_n=Tx_n.$$

Se admite cualquier pareja inicial $(x_{-1},x_0)\in V^2$. Dos estados pertenecen a la misma clase colectiva cuando tienen igual imagen por $T$; sus diferencias forman $N=\ker T$.

**Autonomía de dos capas:** dos soluciones con iguales $(y_{-1},y_0)$ tienen iguales $y_n$ para todo $n\geq0$. Por tanto, conocer las dos capas colectivas basta para predecir el futuro colectivo. Esta definición no presupone una ley efectiva lineal.

## 2. Teorema de cierre por la interfaz

Son equivalentes:

1. Hay autonomía de dos capas para todas las parejas iniciales.
2. Existe una función $F:W\times W\to W$, no supuesta lineal, tal que todas las soluciones satisfacen $y_{n+1}=F(y_n,y_{n-1})$.
3. El núcleo es invariante: $K(\ker T)\subseteq\ker T$.
4. Existe un único operador lineal $\bar K:W\to W$ con

$$\boxed{TK=\bar KT}.$$

En ese caso, la ley efectiva queda necesariamente determinada en todo $W^2$:

$$\boxed{y_{n+1}=2y_n-y_{n-1}-\bar Ky_n}.$$

### Prueba

**1 implica 3.** Para $h\in\ker T$, compare las parejas iniciales $(0,0)$ y $(0,h)$. Ambas tienen $(y_{-1},y_0)=(0,0)$, pero sus siguientes observaciones son $0$ y $-TKh$. La autonomía exige $TKh=0$.

**3 implica 4.** Defina $\bar K(Tx)=TKx$. Si $Tx=Tx'$, entonces $x-x'\in\ker T$ y la invariancia da $TKx=TKx'$. La definición es consistente y lineal. La sobreyectividad de $T$ garantiza existencia en todo $W$ y unicidad.

**4 implica 2.** Aplicar $T$ a la recurrencia microscópica produce la ley efectiva indicada.

**2 implica 1.** La recurrencia determina inductivamente el futuro observado a partir de las dos capas iniciales.

Finalmente, cada pareja $(y,z)\in W^2$ tiene levantamientos independientes en $V$. Por ello, cualquier función $F$ válida para todas las parejas debe coincidir con $2y-z-\bar Ky$ en todo su dominio. Permitir una ley no lineal no amplía aquí las posibilidades. $\square$

Si $T$ no es sobreyectiva, la misma construcción determina el operador sólo sobre $\operatorname{im}T$; su extensión a un espacio $W$ mayor no es única.

## 3. Dos capas y memoria

Para $W\ne\{0\}$, conocer sólo $y_n$ no basta en general: manteniendo esa capa fija y variando $y_{n-1}$, cambia el siguiente valor por el término $-y_{n-1}$. El estado colectivo de esta dinámica es la pareja $(y_n,y_{n-1})$.

Si falla la condición del teorema, no existe cierre exacto **de segundo orden con esas dos capas**, para todas las preparaciones. Esto no descarta una descripción con más memoria, una interfaz ampliada o una familia restringida de estados iniciales. La suficiencia debe especificar siempre qué información y qué preparaciones admite.

## 4. Producto interno y métrica del cociente

Suponga ahora que $V$ y $W$ tienen productos internos positivos. Sea $T^*:W\to V$ el adjunto respecto de esos productos. Como $T$ es sobreyectiva, $TT^*$ es invertible y

$$R=T^*(TT^*)^{-1},\qquad TR=I_W.$$

El vector $Ry$ es el único levantamiento de $y$ en $U=(\ker T)^\perp$, y también el de menor norma. Defina el producto interno colectivo inducido por

$$\langle y,z\rangle_q=\langle Ry,Rz\rangle_V.$$

Si el producto original de $V$ tiene matriz $G>0$ y las coordenadas auxiliares de $W$ son euclídeas,

$$R=G^{-1}T^{\mathsf T}(TG^{-1}T^{\mathsf T})^{-1},\qquad
G_q=(TG^{-1}T^{\mathsf T})^{-1}.$$

Suponga además que $K$ es autoadjunto y que se cumple el cierre. La invariancia de $\ker T$ implica la de $U$. Entonces

$$KR=R\bar K,\qquad
\langle y,\bar Kz\rangle_q=\langle Ry,KRz\rangle_V.$$

Se siguen dos propiedades:

- $\bar K$ es autoadjunto respecto del producto inducido.
- Si $K\geq0$, también $\bar K\geq0$ respecto de ese producto.

Estas afirmaciones no autorizan a suponer que la matriz de $\bar K$ es simétrica respecto de unas coordenadas euclídeas arbitrarias. La métrica forma parte de la construcción.

Además, $\bar K$ es conjugado a $K|_U$: el cociente selecciona modos del operador original; por sí solo no introduce frecuencias nuevas. La positividad tampoco basta para la estabilidad de la recurrencia discreta: la banda oscilatoria estricta es $0<\kappa<4$. Los extremos $0,4$ admiten crecimiento secular y un autovalor mayor que $4$ admite una solución exponencialmente creciente, como explica la [nota de incorporación](novelty_incorporation_and_dynamical_modes.es.md).

## 5. Una suma colectiva puede cerrar entre componentes acoplados

Considere, con producto euclídeo en $\mathbb R^2$,

$$K=\begin{pmatrix}2&b\\b&2\end{pmatrix},\qquad 0<|b|<2.$$

Las coordenadas originales están acopladas, pero para $T=(1,1)$ se tiene

$$TK=(2+b)T,\qquad \bar K=2+b.$$

Por ello, $y_n=x_{1,n}+x_{2,n}$ satisface exactamente

$$y_{n+1}=-b\,y_n-y_{n-1}.$$

El levantamiento mínimo es $Ry=(y/2,y/2)$ y la métrica colectiva es $G_q=1/2$. La diferencia oculta $r_n=x_{1,n}-x_{2,n}$ evoluciona por separado:

$$r_{n+1}=b\,r_n-r_{n-1}.$$

Ambos modos están en la banda estable. El acoplamiento de los componentes originales no impide una descripción colectiva autónoma: importa qué clases define la interfaz.

En cambio, para $T=(1,0)$,

$$TK=(2,b),$$

y no existe $\bar K$ con $TK=\bar KT$ cuando $b\ne0$. Las preparaciones $(x_{-1},x_0)=(0,0)$ y $(0,e_2)$ tienen iguales dos capas observadas, pero sus siguientes observaciones son $0$ y $-b$.

Esta segunda interfaz admite, sin embargo, una ley con más memoria:

$$y_{n+2}+(2-b^2)y_n+y_{n-2}=0.$$

Se obtiene eliminando la segunda coordenada de las dos ecuaciones acopladas. Ilustra por qué el fallo de cierre de dos capas no equivale a imposibilidad de toda descripción efectiva.

## 6. Acción visible e información interna

La autonomía colectiva no recupera toda la dinámica interna. En el ejemplo anterior, una oscilación $x_n=(a_n,-a_n)$ permanece invisible para la interfaz suma: $y_n=0$, aunque el modo oculto sea no trivial.

Con $K$ autoadjunto y cierre exacto, el lagrangiano discreto

$$L_d(x,x')=\tfrac12\|x'-x\|_V^2-\tfrac12\langle x,Kx\rangle_V$$

se separa ortogonalmente en contribuciones de $U$ y $\ker T$. La contribución visible es

$$\bar L_d(y,y')=\tfrac12\|y'-y\|_q^2-\tfrac12\langle y,\bar Ky\rangle_q.$$

La suma temporal de $\bar L_d$ no incluye la contribución de los modos ocultos. Asimismo, un modo oculto estable puede tener un invariante de área simpléctica positivo mientras el invariante visible sea cero. Deben mantenerse separadas la acción variacional discreta, el área simpléctica y la identificación física de unidades, según la [nota de acción y fase](relational_action_and_phase.es.md).

## 7. Papel en el programa y alcance

La [ontología de diferencia y cierre](../01_foundations/ontology_of_difference_and_closure.es.md) orienta la construcción de unidades relacionales. La [incorporación de novedad](novelty_incorporation_and_dynamical_modes.es.md) examina cómo nuevos sectores participan en $K$. Esta nota añade el criterio complementario: cuándo una interfaz colectiva conserva información suficiente para continuar la dinámica seleccionada.

La cadena verificable es: declarar $T$ y las preparaciones, comprobar $K(\ker T)\subseteq\ker T$, construir $\bar K$, declarar su métrica y evaluar las consultas preservadas. Ese resultado constituye una identidad dinámica contextual, no una garantía de suficiencia para cualquier observable o interacción externa. Tampoco establece, por sí solo, una interpretación química, termodinámica o gravitacional.

Procedencia: articulación de los desarrollos del autor sobre promoción de identidad colectiva (MF85) e incorporación de novedad (MF71), con la teoría lineal estándar de cocientes. Los [controles ejecutables](../tests/test_collective_dynamics.py) verifican ejemplos finitos y métricas no triviales; acompañan las pruebas, no las sustituyen.
