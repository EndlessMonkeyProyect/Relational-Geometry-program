# Cierre redistributivo y canales de información recuperable

**Le Matt Ansatz Di Ego · Arquitectura formal y criterios de factorización**

Un cierre puede condensar información en una referencia colectiva y mantener otras diferencias accesibles en canales distintos. Esta nota describe esa distribución sin identificar información con energía ni imponer una medida probabilística.

## 1. Estado, canales y suficiencia

Sea $X$ un dominio de estados admisibles y

$$F=(\Gamma,\Lambda,\Pi):X\to S_\Gamma\times S_\Lambda\times S_\Pi.$$

Aquí $\Gamma$ representa la referencia colectiva, $\Lambda$ un canal exteriorizado y $\Pi$ un registro pendiente. Son nombres locales de canales; $\Gamma$ no es el factor dinámico de las notas de comparadores.

Para un observable $d:X\to D$, escriba $d\preceq f$ cuando existe $\bar d:f(X)\to D$ con $d=\bar d\circ f$. La condición equivale a que $d$ sea constante en cada fibra de $f$.

El cierre es suficiente respecto de una familia declarada $\mathcal D$ si

$$d\preceq F\qquad\text{para todo }d\in\mathcal D.$$

Este requisito sólo conserva las diferencias de $\mathcal D$. El modelo debe especificar qué regla construye los canales y cuándo representan una transición efectiva.

## 2. Patrones mínimos de recuperabilidad

Denote por $I=\{\Gamma,\Lambda,\Pi\}$ el conjunto de canales y por $F_A$ la observación conjunta de los canales de $A\subseteq I$. Para $A=\varnothing$, $F_A$ es constante.

Defina

$$\mathcal U_d=\{A\subseteq I:d\preceq F_A\}.$$

**Proposición.** $\mathcal U_d$ es creciente: si $A\in\mathcal U_d$ y $A\subseteq B$, entonces $B\in\mathcal U_d$. Cuando $d\preceq F$, queda determinada por sus elementos mínimos

$$\mathcal M_d=\{A\in\mathcal U_d:\text{ningún subconjunto propio de }A
\text{ pertenece a }\mathcal U_d\}.$$

**Prueba.** La observación $F_A$ se obtiene proyectando $F_B$, de modo que la factorización se compone. Como hay un número finito de canales, cada conjunto recuperador contiene uno mínimo. Por tanto, $\mathcal U_d$ es exactamente la familia de conjuntos que contienen algún elemento de $\mathcal M_d$. $\square$

Esta construcción incluye recuperación individual, recuperación conjunta y redundancia. No exige que cada diferencia tenga un único destino.

| Patrón mínimo | Significado operacional |
|---|---|
| $\{\{\Gamma\}\}$ | La referencia basta y los otros canales solos o juntos no bastan |
| $\{\{\Lambda\}\}$ | El canal exteriorizado basta y es necesario en todo conjunto recuperador |
| $\{\{\Pi\}\}$ | El registro pendiente basta y es necesario en todo conjunto recuperador |
| $\{\{\Gamma,\Lambda\}\}$ | Se requiere observar conjuntamente referencia y exterior |
| $\{\{\Gamma,\Pi\}\}$ o $\{\{\Lambda,\Pi\}\}$ | Recuperación conjunta que también involucra el registro pendiente |
| $\{\{\Gamma,\Lambda,\Pi\}\}$ | Los tres canales son necesarios |
| $\{\{\Gamma\},\{\Lambda\}\}$ | Dos vías individuales redundantes de recuperación |

La tabla ilustra patrones; la definición cubre todos. Una diferencia constante tiene $\mathcal M_d=\{\varnothing\}$. Una diferencia que no factoriza por $F$ no se conserva en esta arquitectura.

## 3. Ejemplos que distinguen los canales

Para $X=\{0,1\}^2$, tome $\Gamma(a,b)=a$, $\Lambda(a,b)=0$, $\Pi(a,b)=b$. La paridad $d=a\oplus b$ requiere conjuntamente $\Gamma$ y $\Pi$. Se conserva por $F$, aunque no pueda asignarse sólo a referencia, exterior, correlación referencia–exterior o registro pendiente.

Para representar redundancia, tome $\Gamma(a,b)=\Lambda(a,b)=a$. La diferencia $d=a$ se recupera desde cualquiera de esos canales. Contarla dos veces como dos cantidades independientes requeriría una justificación adicional.

Un cierre colectivo ilustrativo es

$$\Gamma(a,b)=a\oplus b,\qquad\Lambda(a,b)=a,\qquad\Pi(a,b)=0.$$

La referencia $\Gamma$ es la [identidad de paridad](contextual_identity_and_scale_promotion.es.md). Desde ella no se recuperan las partes; desde $(\Gamma,\Lambda)$ sí:

$$a=\Lambda,\qquad b=\Gamma\oplus\Lambda.$$

Hay compresión desde la referencia sin pérdida del estado en el conjunto de canales. Esta distinción hace comprobable la propuesta de cierre redistributivo.

## 4. Promoción y sucesivas resoluciones

Para que $\Gamma(x)$ opere como estado del nivel siguiente, debe ser suficiente para las consultas y composiciones de ese nivel. El [criterio de congruencia](contextual_identity_and_scale_promotion.es.md) controla la composición; el [descenso dinámico](collective_dynamics_on_quotients.es.md) controla una realización lineal particular.

Llamar pendiente a $\Pi$ declara un papel en la arquitectura. Para describir cómo una diferencia pasa de pendiente a resuelta se necesita una evolución, sus entradas y sus contratos; esa transición no se deduce del nombre del canal.

Si el contrato posterior requiere también un dato exterior o pendiente, la interfaz utilizable debe ampliarse. Ocultar un canal no lo vuelve prescindible.

## 5. Saturación relativa al acceso exterior

Considere refinamientos $X_{j+1}\xrightarrow{p_{j+1,j}}X_j$ e interfaces exteriores $\sigma_j:X_j\to S_{\rm ext}$. La condición

$$\sigma_{j+1}=\sigma_j\circ p_{j+1,j}\qquad(j\ge j_*)$$

expresa que esos refinamientos no añaden respuestas en la interfaz exterior escogida. Su contenido depende de que las consultas, operaciones, resolución y horizonte de observación estén fijados independientemente. Elegir interfaces que descartan todos los refinamientos satisface la igualdad de manera trivial.

Esta es una noción de saturación de acceso, no un criterio suficiente para identificar un objeto astrofísico. El nivel jerárquico, la profundidad binaria, la longitud física y el acceso causal son variables distintas.

## 6. Papel experimental

El [laboratorio exploratorio](../07_emergence_laboratory/README.md) distingue dos usos:

- En química se comprueba si una coordenada factoriza por descriptores convencionales y qué utilidad tiene en un predictor concreto.
- En crecimiento se comparan descriptores colectivos bajo perturbaciones transitorias, sin presuponer que formen una interfaz suficiente para toda evolución.

Ni una mejora predictiva ni una forma final parecida acreditan por sí solas una promoción de identidad. Proporcionan objetos medibles para estudiar qué conserva cada descripción.

Procedencia: integración del módulo del autor sobre cierre redistributivo y promoción de escala, con clasificación por conjuntos mínimos de canales. [Controles finitos](../tests/test_contextual_identity_and_channels.py). Las correspondencias físicas se mantienen en la [agenda de puentes](../publication/physical_bridges.es.md).
