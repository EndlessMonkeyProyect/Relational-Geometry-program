# Resolución respecto de una referencia y pesos modales

**Le Matt Ansatz Di Ego · Resultados finitos bajo un contrato métrico explícito**

La resolución, la proyección respecto de una referencia uniforme y el espacio
de diferencias de una red pueden describirse dentro de una misma construcción.
La identidad central es

$$r_{\rm ref}=2^{-\mathcal R}.$$

El aporte al programa es hacer calculable esa conexión y precisar cómo se
compone. El espacio de alternativas, la métrica y la representación del estado
son parte del contrato.

## 1. Distribución, referencia y resolución

Sean $N\ge1$ alternativas, una distribución $p\in\mathbb R^N$ con
$p_i\ge0$, $\sum_i p_i=1$, y el producto interno euclídeo. Distinga la distribución
uniforme $\bar p=(1/N,\ldots,1/N)$ de su dirección normalizada
$u=(1,\ldots,1)/\sqrt N$.

Defina la autocoincidencia y la resolución:

$$
C_2(p)=\sum_i p_i^2,\qquad
\mathcal R(p)=\log_2\!\big(NC_2(p)\big)=\log_2N-H_2(p),
\qquad H_2(p)=-\log_2C_2(p).
$$

Aquí «resolución en bits» designa este déficit de entropía de Rényi de orden 2.
La unidad se refiere a la distribución uniforme: $\mathcal R(\bar p)=0$.
Una distribución de Dirac $p=e_x$, concentrada en una alternativa, tiene
$\mathcal R(e_x)=\log_2N$. Por Cauchy–Schwarz y normalización,

$$\frac1N\le C_2(p)\le1,\qquad 0\le\mathcal R(p)\le\log_2N.$$

Si un grupo permuta transitivamente las alternativas, su espacio de vectores
invariantes es $\operatorname{span}(u)$. La normalización de probabilidad fija
$\bar p$, y la norma unitaria con signo positivo fija $u$. La
[construcción finita de comparación](finite_comparison_contract_and_modal_weights.es.md)
explicita ese resultado.

## 2. Reflexión y descomposición ortogonal

Escriba

$$
P_{\rm ref}=uu^{\mathsf T},\qquad
P_{\rm dif}=I-P_{\rm ref},\qquad H_u=2P_{\rm ref}-I.
$$

**Proposición.** $H_u$ es una involución ortogonal. Su autoespacio de valor $+1$
es $\operatorname{span}(u)$ y el de valor $-1$ es $u^\perp$.

**Prueba.** $P_{\rm ref}^2=P_{\rm ref}=P_{\rm ref}^{\mathsf T}$ implica
$H_u^2=I$ y $H_u^{\mathsf T}H_u=I$. La acción en los dos sumandos es inmediata.
$\square$

Para el vector de probabilidades,

$$
V=P_{\rm ref}p=\bar p,\qquad m=P_{\rm dif}p=p-\bar p.
$$

La reflexión pertenece al **espacio de comparación**. Representarla como una
evolución de probabilidades o un canal físico requiere además un dominio
admisible y una ley que preserve estados. En coordenadas $x_i=Np_i$, su acción
ambiental es $x_i\mapsto2-x_i$.

## 3. La identidad peso–resolución

Defina el peso respecto de la referencia y el peso de diferencia:

$$
r_{\rm ref}=\frac{\|V\|^2}{\|p\|^2},\qquad
r_{\rm dif}=\frac{\|m\|^2}{\|p\|^2}.
$$

En la notación modal del programa, este $r_{\rm ref}$ puede escribirse
$r_V^{(\mathrm{res})}$: el superíndice identifica esta realización.

**Teorema.** Si $\theta$ es el ángulo entre $p$ y $u$, entonces

$$
\|V\|^2=\frac1N,\qquad \|m\|^2=C_2(p)-\frac1N,
$$

$$
\boxed{r_{\rm ref}=\cos^2\theta=\frac1{NC_2(p)}=2^{-\mathcal R}},
\qquad
r_{\rm dif}=1-2^{-\mathcal R},\qquad
\tan^2\theta=2^{\mathcal R}-1.
$$

**Prueba.** $\langle p,u\rangle=1/\sqrt N$ por normalización. La proyección tiene
norma cuadrada $1/N$; dividir por $\|p\|^2=C_2(p)$ y aplicar Pitágoras da las
identidades. $\square$

La igualdad vincula una resolución definida, una métrica elegida y un peso
geométrico. Su eventual identificación con energía, frecuencia o masa requiere
una correspondencia adicional.

### Realización equiprobable sobre un soporte

Para una distribución uniforme sobre $M$ de las $N$ alternativas,

$$
C_2=1/M,\qquad \mathcal R=\log_2(N/M),\qquad r_{\rm ref}=M/N.
$$

Dentro de esta subfamilia, $r_{\rm ref}=2^{-n}$ equivale a $N/M=2^n$. Es una
realización explícita mediante $n$ distinciones binarias equiprobables resueltas.
Para distribuciones generales, la equivalencia exacta es
$r_{\rm ref}=2^{-n}\iff\mathcal R=n$; el mecanismo que produjo la distribución
forma parte de su preparación.

## 4. El espacio de diferencia como imagen de una red

Sea $\Gamma$ un grafo conexo con $N$ vértices. Oriente sus aristas y defina
$D_\Gamma\in\mathbb R^{N\times |E|}$ con una columna $e_j-e_i$ por arista
$i\to j$. Es la traspuesta de la incidencia de filas-arista usada en
[comparadores locales](local_comparators_and_relational_laplacian.es.md).

**Teorema.**

$$
\operatorname{im}D_\Gamma=u^\perp,\qquad
\operatorname{rank}D_\Gamma=N-1.
$$

**Prueba.** Cada columna suma cero. Por conectividad, una suma orientada a lo largo
de un camino produce $e_b-e_a$ para cualquier par de vértices. Esas diferencias
generan todo el subespacio de suma cero, de dimensión $N-1$. $\square$

Así,

$$\mathbb R^N=\operatorname{span}(u)\oplus\operatorname{im}D_\Gamma.$$

Para una distribución de Dirac $e_x$ se obtiene además

$$
\tan^2\theta=N-1
=\frac{\dim u^\perp}{\dim\operatorname{span}(u)}
=\operatorname{rank}D_\Gamma.
$$

Esta igualdad entre ángulo y rango se refiere al estado completamente resuelto.
La descomposición del espacio, en cambio, está fijada por el grafo conexo y la
referencia, y sirve para representar todos los estados.

## 5. Registros binarios y comparaciones de Walsh

Para $X=\{0,1\}^n$, $N=2^n$, las funciones

$$w_s(x)=N^{-1/2}(-1)^{s\cdot x},\qquad s\in\{0,1\}^n,$$

con producto escalar binario en el exponente, forman una base ortonormal.
$w_0=u$ y los $N-1$ vectores restantes son una base de $u^\perp$.

**Prueba.** El producto de dos signos es el carácter indexado por $s\oplus t$.
Su suma sobre todos los registros es $N$ si $s=t$ y cero en otro caso, emparejando
registros que difieren en una coordenada activa. $\square$

Para $p=e_x$, todos los coeficientes tienen módulo $1/\sqrt N$, de modo que cada
paridad lleva peso cuadrado $1/N$. En cuatro bits hay quince paridades no
constantes. La cardinalidad del registro y un
[ciclo geométrico de cuatro fases](order_four_operator.md) son estructuras
declaradas por separado; relacionar sus operaciones exige un mapa explícito.

## 6. Composición independiente y correlaciones

Para distribuciones independientes $p$ sobre $N_1$ alternativas y $q$ sobre
$N_2$ alternativas,

$$
C_2(p\otimes q)=C_2(p)C_2(q),\qquad
\mathcal R(p\otimes q)=\mathcal R(p)+\mathcal R(q),
$$

$$r_{\rm ref}(p\otimes q)=r_{\rm ref}(p)r_{\rm ref}(q).$$

Las igualdades se siguen de factorizar la suma doble de cuadrados. La
descomposición tensorial da también

$$
(N_1N_2-1)=(N_1-1)+(N_2-1)+(N_1-1)(N_2-1).
$$

Los tres términos corresponden a diferencia en la primera parte, diferencia en la
segunda y diferencias conjuntas. Para $N_1=N_2=4$, la cuenta es $15=3+3+9$.

Para una distribución conjunta general $p_{ab}$, con marginal $p_a$,

$$
\sum_{a,b}p_{ab}^2\le\sum_a p_a^2
\quad\Longrightarrow\quad
\mathcal R(p_{ab})\le\mathcal R(p_a)+\log_2N_2.
$$

La desigualdad usa $p_{ab}\ge0$ y
$\sum_b p_{ab}^2\le(\sum_b p_{ab})^2$. Dos bits uniformes perfectamente
correlacionados, con peso $1/2$ en $00$ y $11$, tienen resolución conjunta de un
bit y resolución marginal cero. Es un ejemplo de distinción sostenida por la
relación dentro del contrato declarado.

## 7. Realización en operadores densidad

Para una matriz densidad $\rho$ sobre $\mathbb C^N$, use el espacio real de
operadores hermíticos y el producto de Hilbert–Schmidt
$\langle A,B\rangle=\operatorname{Tr}(AB)$. La referencia normalizada es
$U_N=I_N/\sqrt N$ y la densidad de máxima mezcla es $I_N/N$.

La proyección sobre la referencia es $I_N/N$ y el complemento es
$\rho-I_N/N$, un operador de traza cero. Por el mismo cálculo,

$$
\mathcal R_{\rm q}(\rho)=\log_2\!\big(N\operatorname{Tr}\rho^2\big),
\qquad
r_{\rm ref}^{(\rm q)}=\frac1{N\operatorname{Tr}\rho^2}
=2^{-\mathcal R_{\rm q}}.
$$

Para un estado puro, $\mathcal R_{\rm q}=\log_2N$; para la máxima mezcla, vale cero.
La dimensión del complemento hermítico es $N^2-1$.

Para $n$ qubits, $N=2^n$, expanda $\rho=N^{-1}\sum_P a_P P$ en cadenas de Pauli
con $\operatorname{Tr}(PQ)=N\delta_{PQ}$ y $a_I=1$. Entonces

$$
\sum_{P\ne I}\langle P\rangle_\rho^2
=N\operatorname{Tr}\rho^2-1
=2^{\mathcal R_{\rm q}}-1.
$$

Esto cuantifica exactamente el componente de diferencia mediante expectativas
de observables de Pauli.

## 8. Tipos de peso y alcance

| Construcción | Estado representado | Cantidad calculada |
|---|---|---|
| Referencia uniforme de esta nota | Vector de probabilidades $p$ | $r_{\rm ref}=1/(NC_2(p))$ |
| [Eventos del contrato finito](finite_comparison_contract_and_modal_weights.es.md) | Amplitudes $\psi_x=\sqrt{p_x}$ | $p_A=\langle\psi,P_A\psi\rangle=\sum_{x\in A}p_x$ |
| Referencia cuántica | Operador densidad $\rho$ | $r_{\rm ref}^{(\rm q)}=1/(N\operatorname{Tr}\rho^2)$ |
| [Composición de espines](../publication/spin_composition_and_relational_information.es.md) | Densidad de dos espines | $P(F)=\operatorname{Tr}(\rho\Pi_F)$ |

Son realizaciones compatibles como herramientas del programa, cada una con su
propio estado, espacio y proyector. El alcance probado es finito y matemático.
Elegir un sistema físico, su espacio de estados y la lectura de estos pesos
constituye el siguiente contrato de aplicación.

## Verificación

Las [pruebas de resolución y peso](../tests/test_resolution_modal_weights.py)
comprueban proyecciones, reflexión ambiental, soportes uniformes, incidencia,
Walsh, composición independiente, correlación clásica y la expansión cuántica.

~~~shell
python -X utf8 -B -m unittest discover -s tests -p test_resolution_modal_weights.py -v
~~~
