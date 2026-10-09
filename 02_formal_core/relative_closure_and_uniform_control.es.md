# Cierre relativo y control uniforme entre escalas

**Le Matt Ansatz Di Ego · Resultados exactos y condiciones de transferencia**

Una interfaz suficiente permite reutilizar lo relevante de una estructura. El
siguiente paso del programa es cuantificar con qué costo, intensidad o duración
se conserva esa suficiencia al componerla. Esta nota desarrolla tres respuestas
concretas: coercividad por bloques, contracción de un presupuesto y residencia
geométrica durante el crecimiento.

El punto de partida es la [identidad contextual](contextual_identity_and_scale_promotion.es.md)
y la [incorporación con control global](novelty_and_global_control.es.md).
La correspondencia entre ramas organiza obligaciones de prueba. No identifica
sus espacios, sus operadores ni sus límites físicos.

## 1. Comparaciones por bloques: una cota explícita

Sea $\lambda=\bigotimes_{e=1}^N\lambda_e$ un producto finito de probabilidades,
$N\ge1$, y sea $d\mu=\rho\,d\lambda$, con

$$
0<m\le\rho\le M<\infty,\qquad \int\rho\,d\lambda=1.
$$

Para funciones reales de $L^2(\mu)$ definimos

$$
\mathcal D_e^\mu[f]
=\mathbb E_\mu[\operatorname{Var}_\mu(f\mid U_{-e})],
\qquad
\mathcal D_{\rm block}^\mu[f]=\sum_{e=1}^N\mathcal D_e^\mu[f].
$$

Se usa la **suma**, no el promedio por número de coordenadas. Cada comparación
mantiene fijo el exterior $U_{-e}$ y permite variar la coordenada restante.

### Proposición 1. Coercividad y núcleo

$$
\boxed{\operatorname{Var}_\mu(f)
\le\frac{M}{m}\,\mathcal D_{\rm block}^\mu[f].}
$$

En particular, $\mathcal D_{\rm block}^\mu[f]=0$ si y sólo si $f$ es constante
$\mu$-casi seguramente.

**Prueba.** La caracterización variacional de la esperanza condicional da

$$
\mathcal D_e^\mu[f]
=\inf_{g=g(U_{-e})}\int |f-g|^2\,d\mu
\ge m\inf_{g=g(U_{-e})}\int |f-g|^2\,d\lambda
=m\mathcal D_e^\lambda[f].
$$

Los espacios de funciones cuadrado-integrables coinciden como conjuntos porque
las dos medidas tienen densidades comparables. Por otra parte,

$$
\operatorname{Var}_\mu(f)
=\inf_c\int |f-c|^2\,d\mu
\le M\operatorname{Var}_\lambda(f)
\le M\sum_e\mathcal D_e^\lambda[f]
\le\frac{M}{m}\sum_e\mathcal D_e^\mu[f].
$$

La desigualdad intermedia es la tensorización de la varianza en una medida
producto. Puede verse descomponiendo $f$ en componentes ortogonales $f_A$ de
dependencia pura en subconjuntos de coordenadas:
$\operatorname{Var}_\lambda f=\sum_{A\ne\varnothing}\|f_A\|^2$ y
$\mathcal D_{\rm block}^\lambda f=\sum_{A\ne\varnothing}|A|\|f_A\|^2$.
El enunciado sobre el núcleo sigue de la cota.

Esta prueba usa directamente la minimización sobre el exterior y obtiene
$M/m$, en lugar de la cota más gruesa $(M/m)^2$ del desarrollo fuente. Es una
comparación de formas bajo hipótesis explícitas, no una afirmación de prioridad
sobre la tensorización o la técnica de comparación.

### Producto: constante óptima y normalización

Si al menos una coordenada admite una función no constante en $L^2$, entonces

$$
C_*^\lambda
:=\sup_{\operatorname{Var}_\lambda f>0}
\frac{\operatorname{Var}_\lambda f}{\mathcal D_{\rm block}^\lambda f}
=1.
$$

La igualdad se alcanza con una función centrada de una sola coordenada. Si se
usa $\overline{\mathcal D}=\mathcal D_{\rm block}/N$, la constante óptima pasa a
ser $N$. Declarar esa normalización es indispensable al comparar tamaños.

El operador auxiliar $L_{\rm block}=\sum_e(I-P_e)$, con
$P_e=\mathbb E_\mu[\,\cdot\mid U_{-e}]$, es positivo y autoadjunto en $L^2(\mu)$.
Su forma cuadrática es $\mathcal D_{\rm block}^\mu$. La cota controla su gap
de resampling en el complemento de las constantes.

## 2. Realización gauge y producto de constantes

En una red finita puede tomarse $\lambda$ como el producto de medidas de Haar
normalizadas de un grupo compacto. Una densidad continua estrictamente positiva
en ese espacio compacto cumple las hipótesis anteriores.

Para una medida de Gibbs $\rho=Z^{-1}e^{-S}$,

$$
C_*^\mu\le e^{\operatorname{osc}S}.
$$

Como ejemplo externo de realización, la acción de Wilson de $SU(2)$,

$$
S_W=\beta_{\rm lat}\sum_{p=1}^{N_p}
\left(1-\frac12\operatorname{ReTr}U_p\right),\qquad \beta_{\rm lat}\ge0,
$$

satisface $\operatorname{osc}S_W\le2\beta_{\rm lat}N_p$. Por tanto

$$
\boxed{C_*^\mu\le e^{2\beta_{\rm lat}N_p}.}
$$

Es una cota finita, no una estimación óptima. Que este límite superior crezca con
el volumen no demuestra que la constante óptima crezca de la misma forma.

Para estudiar el sector físico se declara
$\mathcal H_{\rm inv}\subset L^2(\mu)$, formado por funciones gauge-invariantes,
y se usa la misma forma restringida a ese dominio. Su mejor constante satisface
$C_{\rm inv}\le C_{\rm all}$. Un cociente
$\operatorname{Var}_\mu h/\mathcal D_{\rm block}^\mu h$ sólo aporta una cota
inferior para la constante del sector al que pertenece $h$; una función de un
enlace que no sea gauge-invariante no certifica el sector físico. Tampoco una
familia pequeña de observables controla el supremo sobre todas sus funciones.

La siguiente obligación se formula como

$$
\operatorname{Var}_\mu f\le C_{\rm rel}\mathcal D_{\rm rel}[f],
\qquad
\mathcal D_{\rm rel}[f]\le C_{\rm bridge}\mathcal E_{\rm phys}[f].
$$

En un dominio común resulta
$\operatorname{Var}_\mu f\le C_{\rm rel}C_{\rm bridge}\mathcal E_{\rm phys}[f]$.
Si cambia la medida hay que justificar además su transferencia, como especifica
la [rama Yang–Mills](../06_yang_mills/README.md). El objetivo cuantitativo es el
producto de constantes en unidades físicas, junto con la construcción y el
paso al límite. Un gap de un algoritmo de resampling y un mass gap de la teoría
física son objetos distintos.

## 3. Contracción que controla un presupuesto completo

Sean $M_1,M_2\ge0$ funciones medibles y $M=\max(M_1,M_2)$. Supongamos que

$$
M_2(t)\le A(t),\qquad M_1(t)\le\theta M(t)+R(t),
\qquad 0\le\theta<1,
$$

con $A,R\ge0$ integrables en $(0,T)$. Entonces

$$
\boxed{
M(t)\le\max\left(A(t),\frac{R(t)}{1-\theta}\right)
\le A(t)+\frac{R(t)}{1-\theta}.
}
$$

**Prueba.** Si el máximo se alcanza en el segundo canal, $M\le A$. Si se alcanza
en el primero, $(1-\theta)M\le R$. Integrar la cota da un presupuesto total finito.

Esta versión conserva el máximo en lugar de reemplazarlo inmediatamente por
una suma. Si $\theta=\theta(t)<1$ varía, la misma prueba es puntual, pero la
integrabilidad exige controlar $R/(1-\theta)$, no sólo $R$.

Para aplicarla a $M=\|\omega(t)\|_\infty$ es necesario que los canales cubran
**todo** el supremo. Si una coordenada geométrica sólo está definida donde
$q>0$ y $a>0$, los sectores restantes necesitan una definición o una cota
adicional. La conclusión es condicional a las desigualdades; obtenerlas para
Navier–Stokes es la tarea analítica siguiente. La continuación requiere además
las hipótesis del criterio de regularidad usado.

## 4. Residencia durante crecimiento logarítmico

Sobre una trayectoria material donde $\omega$ es dos veces diferenciable y
$q=|\omega|>0$, definimos

$$
\xi=\omega/q,\quad a=D_t\log q,\quad b=D_t\xi,\quad
\mathcal A=\frac{D_t^2\omega}{q}.
$$

Escribimos $\mathcal A_\parallel=\xi\cdot\mathcal A$ y
$\mathcal A_\perp=(I-\xi\xi^{\mathsf T})\mathcal A$. Diferenciar
$\omega=q\xi$ y $|\xi|^2=1$ da las identidades

$$
D_ta=\mathcal A_\parallel-a^2+|b|^2,\qquad
P_\xi^\perp D_tb=\mathcal A_\perp-2ab.
$$

Donde $a>0$ y $b\ne0$, usamos $\zeta=|b|/a$ y $dG=a\,dt$. El símbolo
$\zeta$ evita confundir esta razón geométrica con $\beta_{\rm lat}$:

$$
\boxed{
\frac{d\zeta}{dG}
=\Gamma
:=\frac{\widehat b\cdot\mathcal A_\perp}{a^2}
-\zeta\left(1+\zeta^2+\frac{\mathcal A_\parallel}{a^2}\right).
}
$$

La identidad es cinemática. Una ecuación de evolución concreta debe aportar y
controlar $\mathcal A$. Además,
$\rho_\perp=\zeta^2/(1+\zeta^2)$, de modo que el umbral
$0<\eta<1$ corresponde a $\zeta_\eta=\sqrt{\eta/(1-\eta)}$.

### Proposición 2. Residencia condicional

Supóngase que $\zeta(G)$ es absolutamente continua durante un episodio con
$0\le\zeta<\zeta_\eta$ y que $d\zeta/dG\ge\delta>0$ casi en todas partes.
Si entra con valor $\zeta_{\rm in}$, el episodio no puede persistir más allá de

$$
\Delta G\le\frac{\zeta_\eta-\zeta_{\rm in}}{\delta},
\qquad
\frac{q_{\rm out}}{q_{\rm in}}
\le\exp\!\left(\frac{\zeta_\eta-\zeta_{\rm in}}{\delta}\right).
$$

La prueba integra la desigualdad de derivadas. Si el régimen de crecimiento
termina antes, el episodio termina por esa causa y no se afirma una salida por
el umbral. En puntos con $b=0$, la fórmula con $\widehat b$ no está definida:
aplicar la proposición allí exige justificar por separado la derivada de
$\zeta$ y la cota casi en todas partes.

La duración se mide en **crecimiento logarítmico**, no en tiempo físico.
Controla una residencia de una trayectoria. Para sumar episodios y controlar
el supremo espacial todavía se deben acotar reentradas, migración y los demás
sectores. Esto identifica una transición analítica concreta entre observación
geométrica y control global.

## 5. Balance del máximo: conservar todos los puntos activos

Para una solución suave de Navier–Stokes incompresible **sin forzamiento**, con
viscosidad $\nu>0$, sea $S=(\nabla u+\nabla u^{\mathsf T})/2$ y
$\alpha=\xi\cdot S\xi$. Donde $q>0$,

$$
D_tq=\alpha q+\nu\Delta q-\nu q|\nabla\xi|^2.
$$

En el toro, mientras $Q(t)=\max_xq(x,t)>0$, definimos el conjunto activo completo
$\mathcal M(t)=\{x:q(x,t)=Q(t)\}$. La derivada superior derecha satisface, bajo
esta suavidad,

$$
\boxed{
D^+\log Q(t)=
\max_{x\in\mathcal M(t)}
\left(\alpha+\nu\frac{\Delta q}{q}-\nu|\nabla\xi|^2\right)(x,t).
}
$$

**Justificación.** La derivada derecha de un máximo suave sobre un compacto es
el máximo de las derivadas temporales en los puntos activos. En esos puntos
$\nabla q=0$, por lo que $D_tq=\partial_tq$. No se puede elegir un máximo
arbitrario cuando varios puntos empatan con distintas derivadas.

La curvatura del pico se expresa mediante
$R^{-2}=-\Delta q/q\ge0$, admitiendo $R=\infty$ si $\Delta q=0$.
Cuando $R<\infty$, el parámetro $\kappa=\alpha R^2/\nu$ organiza el balance:
una contribución positiva al crecimiento desde un punto activo requiere
$\kappa>1+R^2|\nabla\xi|^2$. Hay que controlar esa expresión en **todos** los
puntos activos para obtener una cota superior del máximo.

En DNS, el argmax de una malla y una diferencia temporal de máximos discretos
son diagnósticos aproximados. Su desacuerdo con el balance local puede incluir
error espacial, error temporal y cambios de punto activo. Para atribuirlo a
migración material hacen falta seguimientos y controles de resolución
adicionales.

## 6. Economía de representación: un control exacto en 2-CNF

El papel de [computación](../05_computation/README.md) se formula en recursos:
tamaño de interfaz, número de pasos, costo de construcción y recuperación de
certificados. Eliminar existencialmente una variable de una 2-CNF mediante
resolución conserva anchura a lo sumo dos.

Con $n$ variables, el número de cláusulas distintas, no tautológicas, de anchura
a lo sumo dos, incluyendo la vacía, es

$$
1+2n+4\binom n2=2n^2+1.
$$

La razón es que hay una cláusula vacía, $2n$ unitarias y cuatro elecciones de
signos por par de variables distintas. Un resolvente de dos cláusulas binarias
contiene como máximo los dos literales que no son el pivote. Al conservar
conjuntos sin duplicados, esta clase tiene un control polinómico de tamaño.
El conteo no exige que el número de cláusulas descienda en cada paso.

En una representación afín sobre $\mathbb F_2$, la eliminación puede conservar
una base de a lo sumo $n$ ecuaciones independientes, más una marca de
incompatibilidad. Son dos mecanismos precisos de economía, con lenguajes
diferentes. Ajustes de crecimiento observados en instancias pequeñas no se
transfieren a cotas inferiores para todos los lenguajes o todas las políticas.

## 7. Evidencia y reproducción de esta integración

Los desarrollos fuente aportan experimentos de eliminación lógica, modelos sigma
2D, redes gauge finitas y DNS de Taylor–Green. Su papel es proponer observables
y contrastes específicos; no sustituyen las desigualdades uniformes.

| Material revisado | Verificación realizada aquí | Alcance |
| --- | --- | --- |
| Eliminación lógica finita | Una instancia pequeña contrastada por eliminación y enumeración exhaustiva | Control de implementación de esa instancia |
| Cocientes gauge aportados | Recálculo aritmético de 19 cocientes a partir de sus resúmenes JSON | Coherencia de los valores suministrados; no repetición de Monte Carlo |
| Taylor–Green aportado | Balance aritmético de 251 muestras a $96^3$ y 134 a $128^3$; energía y disipación iniciales | Coherencia de resúmenes; no nueva DNS ni certificación de resolución |
| Proposiciones de esta nota | Pruebas finitas independientes, exactas o con tolerancia declarada | Controles de fórmulas y dominios; las pruebas generales son las anteriores |

Los cocientes empíricos de Monte Carlo estiman razones de esperanzas. No son
cotas estadísticas certificadas de una constante óptima. Las series DNS no
aportan trayectorias materiales que certifiquen el lema de residencia. No se
han repetido las corridas de producción ni se promueven sus resúmenes a
evidencia de un límite asintótico.

Los controles públicos de esta nota no dependen de archivos internos ni escriben
resultados:

~~~shell
python -B -m unittest discover -s tests -p test_relative_closure_control.py -v
~~~

Procedencia: integración revisada de los desarrollos del autor sobre cierre
relativo, uniformidad y reingreso (MF94–MF96R). Los originales y sus registros de
revisión se conservan por separado. La nota pública presenta las derivaciones,
sus hipótesis y las preguntas siguientes, sin trasladar el archivo histórico.

## 8. Qué revisión habilita

El avance es cuantitativo: hay una constante explícita de coercividad, un blanco
de contracción integrable, una cota de residencia por episodio y un balance que
respeta la geometría completa del máximo. Cada uno indica qué estimar después.

En Yang–Mills se busca controlar el producto de constantes en el sector físico
y pasar al límite. En Navier–Stokes se busca una desigualdad euleriana que cubra
episodios y reentradas. En computación se busca una representación junto con
una política cuyo costo total esté acotado uniformemente. Son objetivos
relacionados por la arquitectura del programa, con obligaciones independientes.
