# Interfaces suficientes y recierre exacto

Una interfaz suficiente conserva exactamente las condiciones de frontera que permiten realizar el interior de un sistema. El resultado central de esta nota es que dos interfaces pueden combinarse y volver a cerrarse sin recuperar los interiores ya eliminados. Esto da al programa una regla matemática de composición reutilizable.

La exposición trabaja con relaciones booleanas y cuantificación existencial sobre conjuntos finitos de variables. Los resultados son algebraicos; el costo de representar y calcular cada relación depende del lenguaje elegido.

## 1. La información que conserva una interfaz

Sean $I$ las variables interiores y $B$ las de frontera, con $I\cap B=\varnothing$. Para una relación $R(I,B)$, definimos:

$$
\Gamma_R(B)=\exists I\,R(I,B).
$$

Una asignación $b$ pertenece a $\Gamma_R$ exactamente cuando admite alguna realización interior. Por tanto, para cualquier contexto exterior $C(B,W)$, donde $W$ es disjunto de $I\cup B$:

$$
\exists I\,[R(I,B)\land C(B,W)]
=\Gamma_R(B)\land C(B,W).
$$

La igualdad es puntual en las variables visibles $B,W$: fijadas estas variables, $C$ no depende de $I$ y puede salir del cuantificador.

**Consecuencia.** Si $\Gamma_R=\Gamma_{R'}$, los dos interiores producen la misma relación visible al conectarse a cualquier contexto de este tipo. Cambiar el interior preservando la interfaz conserva su comportamiento contextual.

También vale el recíproco si la familia de contextos permite fijar cualquier asignación de frontera. En efecto, si las interfaces difieren en $b$, el contexto que exige $B=b$ hace satisfacible una composición y no la otra. Así, para esta familia separadora de contextos:

$$
R\simeq_B R'\quad\Longleftrightarrow\quad\Gamma_R=\Gamma_{R'}.
$$

Esta condición sobre los contextos forma parte del enunciado. Para familias restringidas, la noción de suficiencia se ajusta a las preguntas que efectivamente pueden formular.

## 2. Compatibilidad exacta entre dos bloques

Sean $X,S,Y$ conjuntos de variables mutuamente disjuntos y:

$$
F_A(X,S),\qquad F_B(S,Y).
$$

Su frontera compartida es $S$. Definimos:

$$
B_A(S)=\exists X\,F_A(X,S),\qquad
B_B(S)=\exists Y\,F_B(S,Y).
$$

La cápsula de compatibilidad es la relación:

$$
K_{AB}(S)=B_A(S)\land B_B(S).
$$

**Teorema de compatibilidad.**

$$
K_{AB}(S)=\exists X,Y\,[F_A(X,S)\land F_B(S,Y)].
$$

**Prueba.** Para una asignación fija $s$, pertenecer a $B_A$ proporciona un testigo $x$ y pertenecer a $B_B$ proporciona un testigo $y$. Como los interiores son disjuntos, ambos testigos pueden reunirse en la asignación $(x,s,y)$. Recíprocamente, cualquier realización conjunta proporciona los dos testigos. $\square$

En particular:

$$
F_A\land F_B\text{ es satisfacible}
\quad\Longleftrightarrow\quad
\exists S\,K_{AB}(S).
$$

La compatibilidad global queda expresada como un objeto del mismo tipo que las interfaces de entrada. Esa estabilidad de tipo permite iterar la construcción.

## 3. Recierre sobre una frontera menor

Dividamos $S=I\sqcup Z$: $I$ pasa a ser interior y $Z$ permanece visible.

**Teorema de recierre exacto.**

$$
\exists I\,K_{AB}(I,Z)
=\exists X,Y,I\,[F_A(X,I,Z)\land F_B(I,Z,Y)].
$$

**Prueba.** Sustituimos el teorema de compatibilidad en el miembro izquierdo:

$$
\exists I\,\exists X,Y\,[F_A\land F_B].
$$

La cuantificación existencial sobre variables distintas conmuta, lo que da el miembro derecho. $\square$

La operación completa puede escribirse como:

$$
\text{interfaces}\ \xrightarrow{\mathrm{Join}}\
\text{compatibilidad}\ \xrightarrow{\mathrm{Project}}\
\text{nueva interfaz}.
$$

Una representación exacta de la nueva interfaz puede reutilizarse en la siguiente composición. Este es el contenido preciso de «un cierre se convierte en una nueva referencia».

## 4. Asociación y conservación de fronteras

Considérese una familia finita de factores $F_1,\ldots,F_m$, el conjunto total de variables $V$ y una frontera final fija $Z\subseteq V$. La relación exterior es:

$$
\Gamma_Z=\exists(V\setminus Z)\,\bigwedge_{j=1}^{m}F_j.
$$

Cualquier orden de composición y proyección exactas produce $\Gamma_Z$ siempre que una variable se elimine sólo cuando todos los factores pendientes que la usan hayan quedado incorporados al bloque que se proyecta. Las variables de $Z$ se conservan hasta el final.

**Justificación.** Cada proyección autorizada aplica la identidad:

$$
(\exists x\,G)\land H=\exists x\,(G\land H)
\qquad\text{si }x\notin\operatorname{vars}(H).
$$

Repetir esta identidad, junto con la asociatividad de la conjunción y la conmutatividad de los cuantificadores existenciales, lleva siempre a $\Gamma_Z$.

El resultado permite comparar órdenes de composición sobre una misma semántica final. El tamaño de las interfaces intermedias y el tiempo de las operaciones siguen siendo magnitudes que debe estudiar cada implementación.

## 5. Una realización económica: contador truncado

Para bits $x_1,\ldots,x_n$ y un umbral entero $0\le k\le n$, consideremos la pregunta $\sum_jx_j\le k$. Tras leer $i$ bits, conservamos:

$$
q_i=\min\left(k+1,\sum_{j=1}^{i}x_j\right).
$$

La transición es:

$$
q_{i+1}=\min(k+1,q_i+x_{i+1}).
$$

**Suficiencia.** Si $q_i\le k$, el estado guarda la suma exacta del prefijo. Si $q_i=k+1$, toda continuación conserva el exceso sobre el umbral. En ambos casos, dos prefijos con el mismo estado dan la misma respuesta para cualquier continuación común. La aceptación final es $q_n\le k$.

Hay a lo sumo $k+2$ estados por capa y $(n+1)(k+2)$ nodos en la representación por capas. La cota es $O(n(k+1))$, incluida la frontera $k=0$; para $k=\Theta(n)$ es $O(n^2)$. Evaluar una asignación recorre $n$ transiciones con contadores de $O(\log(k+2))$ bits.

Para bloques disjuntos de variables, los estados se componen mediante:

$$
q_A\oplus_k q_B=\min(k+1,q_A+q_B).
$$

La operación es asociativa porque, para $a,b,c\ge0$:

$$
\min(k+1,\min(k+1,a+b)+c)=\min(k+1,a+b+c).
$$

Por tanto, la suma truncada permite acumular, compartir y recombinar bloques manteniendo una interfaz pequeña y suficiente para la pregunta de umbral. La disjunción de bloques evita contar una misma variable dos veces.

## 6. Qué revisar y desarrollar

Esta nota ofrece demostraciones directas de suficiencia contextual, compatibilidad, recierre y contador. Su aportación al programa es proporcionar un contrato común para comparar realizaciones exactas y estudiar su costo.

Los siguientes puntos de revisión son concretos:

- comprobar que cada aplicación declara su familia de contextos y su frontera visible;
- verificar que un orden de eliminación conserva todas las variables todavía compartidas;
- identificar lenguajes de interfaces con operaciones exactas y cotas explícitas de tamaño y tiempo;
- contrastar cada implementación con enumeración exhaustiva en instancias pequeñas.

La invitación general está en [Revisión del programa](../REVIEW.md). La [rama computacional](../05_computation/README.md) desarrolla el programa de acreditación y sus objetivos de complejidad.

Procedencia: *MF-63B — Recierre acreditado de compatibilidad*, §§1–5; *Cierre, localidad y escala relacional mínima*, §§9–11; *Programa Relacional — Rama P vs NP*, §§16–20. Esta exposición explicita las condiciones de frontera, contextos y composición necesarias para sus enunciados.
