# Contrato finito de comparación, escala geométrica y pesos modales

**Le Matt Ansatz Di Ego · Resultados exactos bajo hipótesis declaradas**

Esta construcción une tres piezas concretas del programa: una interfaz que
conserva respuestas contextuales, una realización geométrica con escala explícita
y una regla calculable de pesos de eventos. Su aporte es mostrar qué determina
cada contrato, con pruebas y ejemplos finitos reproducibles.

## 1. Registro y respuestas contextuales

Sea $k\ge1$, $X_k=\{0,1\}^k$ y $Q(x)=x_1$. La suma $x\oplus a$ es binaria
coordenada a coordenada. Para una familia de contextos $\Sigma$ cerrada bajo
composición y que contiene la identidad, defina

$$
x\equiv_\Sigma y
\iff Q(c(x))=Q(c(y))\quad\text{para todo }c\in\Sigma.
$$

Es la [equivalencia contextual](contextual_identity_and_scale_promotion.es.md)
aplicada a un registro finito. Su cociente conserva exactamente las respuestas
del contrato elegido.

### Lectura con traslaciones

Si los contextos son todas las traslaciones $T_a(x)=x\oplus a$, entonces

$$
Q(T_a x)=x_1\oplus a_1,\qquad
x\equiv_\Sigma y\iff x_1=y_1.
$$

**Prueba.** La igualdad del primer bit da igualdad de todas las respuestas; el
contexto identidad permite recuperar ese bit. Por tanto, el cociente tiene dos
clases y una interfaz suficiente mínima es $\sigma(x)=x_1$. Sobre ella, cada
traslación induce $\bar T_a(b)=b\oplus a_1$. $\square$

### Lectura con permutaciones de coordenadas

Amplíe los contextos al grupo generado por traslaciones y permutaciones de
coordenadas. Para cada $i$ existe una permutación que coloca $x_i$ en la primera
posición. Por tanto,

$$
x\equiv_\Sigma y\iff x=y,\qquad |X_k/{\equiv_\Sigma}|=2^k.
$$

**Prueba.** Si todos los contextos responden igual, las $k$ lecturas obtenidas por
esas permutaciones dan $x_i=y_i$ para cada $i$. La recíproca es inmediata. $\square$

El resultado identifica con precisión cómo ampliar las operaciones refina la
interfaz: una lectura accesible pasa de un bit a los $k$ bits del registro.
$\log_2|X_k/{\equiv_\Sigma}|=k$ cuenta información distinguible en este contrato.
Es una dimensión informacional, no una dimensión espacial física.

## 2. Realización geométrica con escala explícita

En $\mathbb R^3$ con producto interno euclídeo, elija $R\ne0$,
$\rho=\|R\|$ y

$$
J_R A=A\times R,\qquad D=R^\perp.
$$

Las identidades del producto vectorial dan, en todo el espacio,

$$
J_R^2A=R\langle A,R\rangle-\rho^2 A.
$$

En consecuencia $D$ es invariante y, para $A\in D$,

$$
\langle J_RA,A\rangle=0,\qquad
\|J_RA\|=\rho\|A\|,\qquad J_R^2A=-\rho^2 A.
$$

**Prueba.** $A\times R$ es perpendicular a $A$ y a $R$. La identidad de la norma
es $\|A\times R\|^2=\|A\|^2\|R\|^2-\langle A,R\rangle^2$; en $D$ desaparece el
segundo término. La fórmula del doble producto prueba el cuadrado. $\square$

La normalización

$$
\mathcal I_R=\rho^{-1}J_R|_D
$$

satisface $\mathcal I_R^2=-I_D$ y $\mathcal I_R^4=I_D$. Así se realiza el
[operador de cuatro fases](order_four_operator.md) y una estructura compleja
sobre el plano: multiplicar por $i$ se representa mediante $\mathcal I_R$.
Si $R=(0,0,\rho)$, entonces $\mathcal I_R(x,y,0)=(y,-x,0)$.

La separación entre escala y fase es exacta: $J_R^4=\rho^4 I_D$, mientras que el
operador normalizado cierra en cuatro fases. Para $0<\rho\le1$, la realización
incluye además el sector geométrico contractivo de la construcción fuente.
La longitud de $R$ es una escala del espacio de representación; asignarle una
unidad o un observable físico exige un mapa adicional.

## 3. De una medida a pesos de eventos

Sea $X$ un conjunto finito no vacío, $N=|X|$ y $\pi$ una distribución de
probabilidad. En $\mathcal H=\mathbb C^X$, con base ortonormal
$\{|x\rangle:x\in X\}$, defina

$$
|\psi_\pi\rangle=\sum_{x\in X}\sqrt{\pi_x}\,|x\rangle,\qquad
P_A=\sum_{x\in A}|x\rangle\langle x|
$$

para un evento $A\subseteq X$. Entonces

$$
\|\psi_\pi\|^2=1,\qquad
p_A=\langle\psi_\pi,P_A\psi_\pi\rangle
=\|P_A\psi_\pi\|^2=\sum_{x\in A}\pi_x.
$$

Este mapa representa una medida clásica mediante amplitudes reales no negativas.
Los proyectores considerados son **proyectores de eventos diagonales en la base
de registros**. Esa estructura, y no sólo su rango, forma parte de la fórmula.

### Teorema de uniformidad condicionada

Si un grupo $G$ actúa transitivamente en $X$ y $\pi_{gx}=\pi_x$ para todo
$g\in G$ y $x\in X$, entonces

$$
\pi_x=\frac1N,\qquad p_A=\frac{|A|}{N}.
$$

**Prueba.** Dados $x,y$, la transitividad da un $g$ con $gx=y$. La invariancia
iguala $\pi_x$ y $\pi_y$. Todas las masas son iguales y suman uno, de modo que
cada una es $1/N$. Sumar sobre $A$ da el peso. $\square$

Para el registro binario, las traslaciones ya actúan transitivamente. Bajo una
medida invariante, un evento con $r$ registros tiene peso $r/2^k$; un singleton
tiene peso $2^{-k}$. Esta es una selección exacta **una vez fijados** el registro,
su simetría, la medida invariante y el evento.

Más generalmente, si hay varias órbitas $O_j$, una medida invariante con masa
$c_j$ en $O_j$ satisface
$\pi_x=c_j/|O_j|$ para $x\in O_j$ y
$p_A=\sum_j c_j|A\cap O_j|/|O_j|$.
La transitividad corresponde a una sola órbita de masa uno.

## 4. Dinámica explícita que produce la medida uniforme

Escriba $U_{xy}=1/N$ y, para $0<\alpha\le1$, defina

$$
T_\alpha=(1-\alpha)I+\alpha U.
$$

La convención es de distribuciones fila: $\mu_{t+1}=\mu_tT_\alpha$. La matriz
es estocástica y doblemente estocástica. Si $u=(1/N,\ldots,1/N)$, para toda
distribución inicial $\mu$ y todo entero $t\ge0$,

$$
\mu T_\alpha^t=u+(1-\alpha)^t(\mu-u).
$$

**Prueba.** $uT_\alpha=u$. Todo vector fila $v$ de suma cero satisface $vU=0$,
luego $vT_\alpha=(1-\alpha)v$. Aplique esto a $\mu=u+(\mu-u)$. Para
$\alpha=1,t=0$ la expresión se interpreta como $\mu T_\alpha^0=\mu$; para
$t\ge1$ la distribución es $u$. $\square$

La fórmula implica unicidad de la distribución estacionaria y convergencia.
En distancia de variación total,

$$
\|\mu T_\alpha^t-u\|_{\rm TV}
=(1-\alpha)^t\|\mu-u\|_{\rm TV}.
$$

Esta dinámica realiza una redistribución finita con tasa de mezcla calculable.
$T_\alpha$ conmuta con toda permutación de los registros. Es un operador
propuesto de mezcla completa, no una dinámica local deducida del producto
vectorial. $t$ cuenta aplicaciones de la regla; convertirlo en duración física
requiere calibrar un reloj.

## 5. Compatibilidad algebraica entre dos representaciones de masa

La misma disciplina de contratos permite comparar fórmulas sin identificar por
anticipado sus observables. Sean $c,\hbar>0$ constantes de referencia. En la
representación F se postulan

$$
I_F=M_FR_F^2,\qquad L_F=I_F\Omega_F,\qquad R_F,\Omega_F>0,
$$

de donde $M_F=L_F/(\Omega_FR_F^2)$. Aquí $L_F\ge0$ tiene dimensiones de momento
angular e $I_F$ de momento de inercia. La igualdad $I_F=M_FR_F^2$ define el modelo
de radio efectivo que se está usando.

En la representación modal se fijan $\omega_U>0$, $\omega_V,\omega_m\ge0$ con

$$
\omega_U^2=\omega_V^2+\omega_m^2,\qquad
p=\omega_V^2/\omega_U^2,\qquad M_A=\hbar\omega_m/c^2.
$$

La última igualdad es un postulado de correspondencia. Bajo estos contratos,

$$
\boxed{M_F=M_A\iff
\frac{L_F}{\hbar}=\frac{\omega_m\Omega_FR_F^2}{c^2}.}
$$

**Prueba.** Iguale las dos expresiones de masa y multiplique por
$\Omega_FR_F^2/\hbar$. Todos los denominadores son positivos, por lo que el
procedimiento es reversible. $\square$

Para $0<p<1$, escriba $R_i=c/\omega_i$. Las siguientes elecciones dan condiciones
de compatibilidad diferentes y explícitas:

| Radio elegido | Frecuencia elegida | Condición $L_F/\hbar$ | Si se adopta $p=1/16$ |
|---|---|---|---|
| $R_F=R_V$ | $\Omega_F=\omega_V$ | $\sqrt{(1-p)/p}$ | $\sqrt{15}$ |
| $R_F=R_U$ | $\Omega_F=\omega_V$ | $\sqrt{p(1-p)}$ | $\sqrt{15}/16$ |
| $R_F=R_m$ | $\Omega_F=\omega_V$ | $\sqrt{p/(1-p)}$ | $1/\sqrt{15}$ |
| $R_F=R_U$ | $\Omega_F=\omega_U$ | $\sqrt{1-p}$ | $\sqrt{15}/4$ |

La última columna es la sustitución condicional $p=2^{-q}$ con $q=4$.
No selecciona ese exponente para un sistema físico ni lo identifica con una
dimensión espacial.

El resultado acredita compatibilidad algebraica bajo la elección declarada; la
elección de radio, frecuencia y momento proyectado sigue siendo información del
modelo. No se identifica aquí $L_F$ con el espín medido ni ninguno de estos radios
con un radio de carga.

## 6. Alcance de la integración y mapa físico por completar

Quedan construidos tres objetos independientes y conectables: las clases de
respuestas, el plano geométrico normalizado y la distribución modal de eventos.
La identificación entre ellos debe darse como un mapa, no por compartir un
símbolo o un número. En particular:

- $k$ cuenta bits del registro. Su asignación a un sistema físico debe justificarse.
- $A$ declara el evento cuyo peso se calcula. Su identificación con un canal
  observable debe fijarse independientemente de la medida que se quiere ajustar.
- $T_\alpha$ especifica la dinámica de mezcla. Su derivación desde operaciones
  físicas y el valor de $\alpha$ requieren una realización.
- La incrustación $\pi\mapsto\psi_\pi$ fija amplitudes positivas. Fases,
  interferencia y evolución cuántica constituyen estructura adicional.
- Identificar $p_A$ con una fracción de frecuencias al cuadrado es otro puente.
  El descriptor químico $r_V$ y un peso modal no son iguales por definición.

El siguiente contraste físico debe fijar $(k,A,T)$ y el diccionario de observables
antes de comparar datos, y obtener predicciones adicionales con incertidumbres.
Esta nota aporta los teoremas condicionales y las compatibilidades exactas para
formular ese contraste; no presenta una validación de partículas.

## 7. Verificación reproducible

Las pruebas de [test_finite_comparison_contract.py](../tests/test_finite_comparison_contract.py)
enumeran los cocientes para $k=1,\ldots,4$, comprueban la escala de $J_R$ con
aritmética racional, verifican pesos de eventos y medidas invariantes por órbita,
y contrastan exactamente la dinámica de mezcla en ejemplos finitos. También
comprueban la compatibilidad de masas para un triple de frecuencias racionales.
Son controles de implementación y ejemplos; las demostraciones generales están
en esta nota.

~~~shell
python -B -m unittest discover -s tests -p test_finite_comparison_contract.py -v
~~~

Procedencia: desarrollo aportado de contrato finito de comparación y selección
modal por cierre (MF101–102), y anexo de compatibilidad masa–momento–radio, 8 de
octubre de 2026. La integración conserva sus resultados afirmativos bajo
hipótesis explícitas y los enlaza con el núcleo contextual y geométrico.
