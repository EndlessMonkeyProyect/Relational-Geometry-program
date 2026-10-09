# Recierre contextual, residuo y costo de una interfaz

**Le Matt Ansatz Di Ego · Contratos exactos y realizaciones finitas**

Una identidad reutilizable conserva lo que puede importar en las relaciones siguientes. Esta nota une tres preguntas del programa: qué interfaz basta, qué información debe añadirse cuando el contrato se enriquece y cuánto trabajo requiere construir y reutilizar esa interfaz.

El resultado es una arquitectura verificable: cociente contextual, composición compatible, residuo por fibras y operaciones explícitas de construcción, actualización y lectura. Las construcciones algebraicas son estándar; su aporte aquí es articular el [cierre suficiente](closure_information.es.md), la [identidad colectiva](contextual_identity_and_scale_promotion.es.md) y la [rama computacional](../05_computation/README.md) bajo un mismo contrato.

## 1. Continuaciones y mínimo semántico

Sea $X\ne\varnothing$ un conjunto, $(C,\circ,e)$ un monoide y una acción derecha total

$$x\cdot e=x,\qquad (x\cdot c)\cdot d=x\cdot(c\circ d).$$

Fije una pregunta $Q:X\to Y$. Defina

$$x\equiv_Q y\iff Q(x\cdot c)=Q(y\cdot c)\quad\text{para todo }c\in C,$$

$$I_Q=X/{\equiv_Q},\qquad q_Q(x)=[x]_Q.$$

**Proposición de suficiencia y continuación.** Esta equivalencia es estable bajo toda continuación. El cociente es la interfaz exacta menos informativa: si $\Phi:X\to Z$ satisface $\Phi(x)=\Phi(y)\Rightarrow x\equiv_Qy$, existe un único $g:\Phi(X)\to I_Q$ con $q_Q=g\circ\Phi$. Además,

$$[x]_Q\star c=[x\cdot c]_Q$$

define una acción sobre el cociente.

**Prueba.** Las propiedades de equivalencia se heredan de la igualdad. Si $x\equiv_Qy$, para cualquier $c,d\in C$ se cumple

$$Q((x\cdot d)\cdot c)=Q(x\cdot(d\circ c))=Q(y\cdot(d\circ c))=Q((y\cdot d)\cdot c).$$

Esto demuestra estabilidad y buena definición de $\star$; las leyes de acción se heredan de $X$. Para la minimalidad, ponga $g(\Phi(x))=[x]_Q$: la suficiencia elimina la dependencia del representante, y la restricción a $\Phi(X)$ garantiza unicidad. $\square$

La respuesta actual $Q(x)$ es recuperable desde $[x]_Q$ porque $e\in C$. Conservar sólo esa respuesta puede bastar para una consulta terminal; conservar la clase permite responder después de cualquier continuación declarada.

Si $N=|I_Q|<\infty$, toda interfaz suficiente tiene al menos $N$ valores. Una codificación binaria de longitud fija requiere al menos $\lceil\log_2N\rceil$ bits, y una enumeración de las clases alcanza esa longitud como construcción de conjuntos. Para códigos inyectivos de longitud variable sin requisito de prefijo, la cota exacta sobre la longitud máxima es $\lceil\log_2(N+1)\rceil-1$, contando la cadena vacía. Son cotas de identificación; los algoritmos para encontrar y utilizar las etiquetas se especifican en §5.

## 2. Componer identidades: la condición de congruencia

Declare una operación total $J:X\times X\to X$. Existe una única operación colectiva

$$\widehat J:I_Q\times I_Q\to I_Q,\qquad
\widehat J([x]_Q,[y]_Q)=[J(x,y)]_Q$$

si y sólo si

$$\boxed{x\equiv_Qx',\ y\equiv_Qy'\ \Longrightarrow\ J(x,y)\equiv_QJ(x',y').}$$

**Prueba.** La condición hace que la fórmula de $\widehat J$ no dependa de representantes. En sentido inverso, una operación bien definida da salidas iguales para clases de entrada iguales. La proyección sobre las clases es sobreyectiva y determina toda la operación. $\square$

La acción de continuaciones de §1 garantiza el caso unario. Para una composición binaria adicional, la condición anterior debe verificarse; también puede garantizarse incluyendo sus contextos de un hueco en el contrato, como en la [nota de identidad colectiva](contextual_identity_and_scale_promotion.es.md#3-composición-sobre-identidades).

Para operaciones parciales, el dominio de pares admisibles debe ser una unión de productos de clases y las salidas admisibles deben cumplir la congruencia. Así la interfaz conserva tanto la posibilidad de componer como el resultado contextual.

## 3. Enriquecimiento, fibras y etiquetas residuales

Mantenga la misma acción de $C$ y enriquezca la pregunta a $Q_+:X\to Y_+$, con una recuperación explícita $Q=h\circ Q_+$. Entonces $x\equiv_{Q_+}y$ implica $x\equiv_Qy$, aplicando $h$ a cada respuesta contextual. Por tanto existe una proyección canónica sobreyectiva

$$\pi:I_{Q_+}\to I_Q,\qquad [x]_{Q_+}\mapsto[x]_Q.$$

Defina el **residuo contextual de una clase** por su fibra

$$\operatorname{Res}(s)=\pi^{-1}(s).$$

Es un conjunto de identidades refinadas compatibles con la misma identidad gruesa. No es una cantidad que se reste del estado, ni un canal físico automáticamente producido por una transición. Elegir un elemento de la fibra especifica qué identidad refinada estaba presente.

Una fibra tiene un único elemento exactamente cuando dentro de esa clase gruesa no hay distinción contextual adicional. Si todas son unitarias, $\pi$ es biyectiva y el enriquecimiento no cambia la partición.

**Teorema de etiquetas mínimas.** Suponga ambos cocientes finitos. Para representar cada identidad fina $t\in I_{Q_+}$ mediante un par $(\pi(t),r(t))\in I_Q\times R$ de manera inyectiva, el mínimo número de etiquetas residuales es

$$\boxed{|R|_{\min}=\max_{s\in I_Q}|\pi^{-1}(s)|=:M.}$$

**Prueba.** Dentro de una fibra, la primera componente es idéntica, por lo que sus elementos necesitan etiquetas distintas. Esto exige al menos $M$. Recíprocamente, enumere por separado cada fibra con etiquetas de $\{0,\ldots,M-1\}$. Dos identidades con igual primera componente se separan por su etiqueta; las de distintas fibras ya se separan por la primera componente. $\square$

Si la identidad gruesa ya está disponible, una etiqueta residual binaria de longitud fija necesita y puede alcanzar $\lceil\log_2M\rceil$ bits. El etiquetado no es canónico ni viene acompañado de un algoritmo eficiente por esta prueba. Cuando las fibras tienen tamaños diferentes, la imagen de $(\pi,r)$ puede ser un subconjunto propio de $I_Q\times R$: refinamiento no equivale a independencia de las dos coordenadas.

La [arquitectura de canales](redistributive_closure_and_information_channels.es.md) puede realizar esas etiquetas en una aplicación, una vez definidos sus mapas y operaciones.

## 4. Ejemplo completo: suma modular, paridad y acarreo

Tome $X=C=\mathbb Z_8$, con $x\cdot c=x+c\pmod8$, identidad $0$ y composición por suma modular. Aquí todas las continuaciones forman efectivamente un monoide.

Para $Q(x)=x\bmod2$, las dos clases son las paridades. Para $Q_+(x)=x\bmod4$, las cuatro clases son los residuos módulo $4$. Se tiene $Q=h\circ Q_+$ con $h(t)=t\bmod2$, y cada fibra de $\pi$ tiene tamaño dos.

La composición $J(x,y)=x+y\pmod8$ desciende a ambas interfaces. Escriba una identidad fina como

$$t=s+2r\pmod4,\qquad s,r\in\{0,1\}.$$

La etiqueta $s$ conserva la paridad y $r$ es el bit residual mínimo. Su actualización exacta es

$$s'=s_1\oplus s_2,\qquad
r'=r_1\oplus r_2\oplus(s_1s_2).$$

El producto $s_1s_2$ es el acarreo de la suma de los bits bajos. Así, el refinamiento no sólo admite etiquetas: en este caso tiene una ley de recierre explícita sobre ellas. Las dos interfaces responden a contratos distintos sin necesitar los ocho estados originales.

## 5. Construcción, actualización, lectura y política

Para una familia de contratos indexada por tamaño de entrada $n$, una realización efectiva canónica declara una codificación inyectiva $E_n:I_{Q,n}\to\{0,1\}^*$ y algoritmos uniformes que cumplen

$$\operatorname{Build}_n(x)=E_n([x]),$$

$$\operatorname{Update}_n(E_n([x]),c)=E_n([x\cdot c]),$$

$$\operatorname{Read}_n(E_n([x]))=Q_n(x).$$

La igualdad de actualización equivale a que construir después de continuar produzca el mismo código que actualizar el cierre ya construido. Para composiciones binarias se declara además la implementación de $\widehat J$.

Un contrato de costo incluye:

- codificación y tamaño de estados de entrada y continuaciones;
- tiempo de construcción, actualización y lectura;
- memoria de los códigos, estructuras auxiliares y preprocesamiento;
- algoritmo que selecciona y construye cada continuación;
- número total de pasos y condición de terminación.

Los programas son uniformes respecto de $n$; una tabla o consejo específico de cada tamaño no se considera gratuito. Las cotas de longitud mínima de §§1 y 3 describen distinciones semánticas, mientras que estas partidas miden la economía de una realización concreta.

Por ejemplo, con $C=\{e\}$ y pregunta booleana, hay a lo sumo dos clases. Usando la etiqueta $E([x])=Q(x)$, construirla es precisamente calcular la respuesta. Para una codificación general, la identidad operacional es $Q=\operatorname{Read}\circ\operatorname{Build}$, de modo que el costo relevante incluye ambos algoritmos.

**Proposición de costo acumulado.** Suponga que un procedimiento uniforme correcto inicializa su estado en tiempo $p_B(n)$, realiza a lo sumo $p_k(n)$ recierres, selecciona y codifica cada continuación en tiempo $p_P(n)$, actualiza en tiempo $p_U(n)$ y lee la respuesta final en tiempo $p_R(n)$. Suponga también cotas polinómicas sobre las representaciones alcanzadas, la memoria auxiliar y el preprocesamiento. Si todas estas cotas son polinomios de $n$, su tiempo total está acotado por

$$p_B(n)+p_k(n)\bigl(p_P(n)+p_U(n)\bigr)+p_R(n).$$

La prueba es sumar el trabajo declarado. Si la salida decide el problema de entrada, se obtiene un algoritmo polinómico para esa familia. La corrección de la salida, la selección efectiva de pasos y las cotas uniformes forman parte de las hipótesis; el tamaño del cociente no las sustituye.

## 6. Realización booleana: cerrar un interior sobre su frontera

Sean $I,S$ conjuntos finitos y disjuntos de variables interiores y de frontera, con $|S|=b$. Para una relación booleana $F$ sobre esas variables, defina

$$B_F:\{0,1\}^{S}\to\{0,1\},\qquad
B_F(s)=1\iff\exists i\in\{0,1\}^{I}\ F(i,s)=1.$$

Las continuaciones son todas las restricciones booleanas $C$ sobre $S$, actuando por $F\cdot C=F\land C$; se componen por conjunción y tienen identidad verdadera. La pregunta $Q$ decide si la relación tiene alguna realización.

**Teorema de interfaz residual.** Para bloques $F$ y $G$ sobre la misma frontera, con sus respectivos interiores,

$$\boxed{F\equiv_QG\iff B_F=B_G.}$$

**Prueba.** Para cualquier continuación, $F\land C$ tiene una realización exactamente cuando existe $s$ con $B_F(s)\land C(s)=1$. La igualdad de residuos da igualdad de todas las respuestas. Si difieren en $s_0$, la continuación que fija $S=s_0$ produce respuestas distintas. $\square$

La disponibilidad de esos contextos que fijan asignaciones es esencial para el recíproco. El efecto contextual del interior queda descrito exactamente por una función de frontera.

Una realización directa guarda la tabla de $B_F$:

$$\operatorname{Build}(F)=B_F,\quad
\operatorname{Update}(B,C)=B\land C,\quad
\operatorname{Read}(B)=\bigvee_sB(s).$$

Con $2^b$ entradas, actualizar a partir de otra tabla y leer cuestan $O(2^b)$ operaciones booleanas. Construir la tabla desde un interior de $m$ bits por enumeración puede requerir $2^{m+b}$ evaluaciones de $F$; cualquier mejor cota debe justificarse mediante su estructura y representación.

Para el universo que realiza todas las funciones booleanas de $b$ bits existen $2^{2^b}$ clases, y la longitud fija mínima es $2^b$ bits. Si se restringen los bloques permitidos, cambia el conjunto de funciones realizables. Este conteo no es una cota de tiempo en función del tamaño de una fórmula ni una separación de clases de complejidad.

## 7. Anchura como recurso operativo

La [composición de interfaces](compatible_reclosure.es.md) permite unir bloques de interiores disjuntos y proyectar variables que dejan de ser necesarias. En tablas, una operación sobre una unión de ámbitos de a lo sumo $w$ variables cuesta $\operatorname{poly}(w)2^w$ operaciones elementales por enumeración; la proyección se obtiene agrupando y tomando OR sobre las variables eliminadas.

Si una política calculable en tiempo polinómico realiza un número polinómico de operaciones, construye sus tablas iniciales en tiempo polinómico y mantiene $w=O(\log n)$ **también en los ámbitos temporales que se unen o proyectan**, la ejecución por tablas queda acotada polinómicamente. Controlar sólo la frontera final no basta para estimar el trabajo intermedio.

Otras representaciones pueden aprovechar estructura adicional. Para compararlas se registran, por separado, longitud, construcción, operaciones admitidas y lectura. Éste es el papel del recierre como recurso dentro de la investigación computacional.

## 8. Controles y siguiente paso del programa

Los [controles finitos](../tests/test_contextual_reclosure.py) comprueban la acción modular completa, el descenso de la suma, las fibras y el acarreo residual, la cota de etiquetas en ejemplos de fibras desiguales, y construcción/actualización/lectura booleanas por enumeración exhaustiva pequeña. Las pruebas generales están en el texto; los controles detectan errores de implementación y fijan ejemplos reproducibles.

El siguiente paso en cada aplicación es proponer su acción, sus consultas y su representación, verificar el descenso de operaciones y medir el costo de la política completa. En una realización física se necesita además una dinámica y observables que interpreten las clases y sus fibras; esta formalización no identifica el residuo con energía, radiación o una nueva dimensión física.

Procedencia: desarrollos del autor sobre interfaz contextual mínima, economía del recierre y congruencia/residuo contextual (MF97–MF99), integrados con sus ejemplos booleanos y modulares. La exposición conserva los resultados formales y sus condiciones; la revisión interna y el histórico de trabajo se mantienen separados de esta nota pública.
