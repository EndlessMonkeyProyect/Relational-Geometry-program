# SAT contextual: canonización y costo de representación

**Le Matt Ansatz Di Ego · Caracterización condicional y eliminación por tablas**

La interfaz de un bloque lógico conserva cómo puede relacionarse con su exterior. Esta nota caracteriza el costo de realizar esa idea en dos lenguajes concretos: fórmulas CNF y tablas densas de frontera. El resultado permite distinguir una equivalencia de complejidad, una representación canónica y una cota estructural de almacenamiento.

La base semántica está en [interfaces suficientes y recierre exacto](../02_formal_core/compatible_reclosure.es.md); el contrato operativo se desarrolla en [recierre contextual y costo](../02_formal_core/contextual_reclosure_and_resource_cost.es.md).

## 1. Contrato: frontera nombrada, fórmulas y continuaciones

Un bloque es una CNF finita $F(I,S)$, con variables interiores $I$ y una lista ordenada de variables de frontera $S$, disjuntas. Las variables y sus nombres tienen codificación binaria explícita. La interfaz semántica es

$$B_F:\{0,1\}^{S}\to\{0,1\},\qquad B_F(s)=\exists i\ F(i,s).$$

Las continuaciones son CNF $C(S)$ que sólo restringen la frontera. Su composición es la conjunción, con la fórmula verdadera como identidad. La pregunta final es satisfacibilidad. Como las continuaciones incluyen las que fijan cualquier asignación de frontera,

$$F\equiv_SG\iff B_F=B_G.$$

La igualdad compara bloques con la misma lista de frontera; los interiores pueden tener distintos nombres y tamaños. Una codificación canónica conserva el contrato $S$ y permite variables auxiliares interiores cuantificadas existencialmente. No se exige eliminar esas variables de la fórmula representante.

Sea $n$ la longitud codificada del bloque inicial, incluidas las declaraciones de frontera. Para una historia explícita $C_1,\ldots,C_k$, se cuenta también su longitud:

$$M=n+\sum_{j=1}^k\bigl(1+|C_j|\bigr).$$

Las cotas se expresan primero en $M$. Para obtenerlas en el tamaño inicial $n$, la política debe producir un número polinómico de continuaciones con longitud total polinómica, y su selección y construcción deben costar tiempo polinómico. Los algoritmos son uniformes: un mismo programa sirve para todos los tamaños, con su memoria auxiliar y preprocesamiento contabilizados.

## 2. Presentación y código de una clase

Una **presentación** conserva una fórmula representante:

$$\operatorname{Build}(F)=F,\qquad
\operatorname{Update}(G,C)=G\land C,\qquad
\operatorname{Read}(G)=\operatorname{SAT}(G).$$

Su corrección semántica es inmediata. Construir y concatenar fórmulas tiene costo lineal en los datos que se copian; la longitud crece aditivamente. Una historia de longitud total $M$ puede procesarse con un costo polinómico de gestión de las fórmulas. Distintas presentaciones pueden pertenecer a la misma clase contextual.

Una **realización canónica** elige un único código $E_S([F])$ por clase, inyectivo entre clases, y satisface

$$\operatorname{Build}(F)=E_S([F]),$$

$$\operatorname{Update}(E_S([F]),C)=E_S([F\land C]),\qquad
\operatorname{Read}(E_S([F]))=\operatorname{SAT}(F).$$

Así se separan tres objetos: decidir si dos entradas son equivalentes, calcular un invariante completo y producir una forma canónica representante. Son distinciones estudiadas en la literatura de equivalencias computacionales; véase [Fortnow y Grochow](https://arxiv.org/abs/0907.4775).

## 3. Caracterización de la economía uniforme

**Teorema.** Para el contrato CNF de §1, son equivalentes:

1. $P=NP$.
2. Existe una realización por presentación con lectura polinómica y costo total polinómico en $M$.
3. Existe una realización canónica con construcción, actualización y lectura polinómicas, códigos de longitud polinómica y costo total polinómico en $M$.

### Presentación y decisión

Si $P=NP$, SAT tiene un algoritmo polinómico, que realiza la lectura de §2. En sentido inverso, una construcción y lectura polinómicas permiten decidir SAT mediante $\operatorname{Read}(\operatorname{Build}(F))$, incluso sin continuaciones. El mismo argumento prueba que 3 implica 1.

### Construcción canónica bajo $P=NP$

Fije un alfabeto, una sintaxis CNF decodificable en tiempo polinómico, un orden lexicográfico y nombres internos normalizados. La lista exterior $S$ permanece fija y codificada; su renombrado no identifica fronteras diferentes. La normalización de nombres de una entrada puede hacerse con aumento polinómico de longitud.

Defina $E_S([F])$ como la CNF normalizada $G$ de menor longitud y, entre ellas, lexicográficamente menor, tal que $B_G=B_F$. Existe porque una versión normalizada de $F$ es candidata; por tanto su longitud está acotada polinómicamente por la entrada. Al depender sólo de $S$ y de $B_F$, es un código canónico e inyectivo sobre clases.

La prueba de costo utiliza la jerarquía polinómica $PH$. La equivalencia residual pertenece a $\Pi_2^p$: una de sus inclusiones puede escribirse

$$\forall s\,\forall i\,\exists j\ \bigl(\neg F(i,s)\lor G(j,s)\bigr),$$

y la otra intercambia $F,G$. Los tamaños de las asignaciones están acotados por las longitudes de ambas fórmulas. Preguntar si existe una candidata $G$ de longitud acotada y prefijo dado con esa equivalencia pertenece a $\Sigma_3^p$.

Bajo $P=NP$, $PH=P$. Por ello se puede encontrar la longitud mínima y luego cada símbolo del primer código mediante un número polinómico de consultas polinómicas. Esto proporciona $\operatorname{Build}$ uniforme. Para actualizar, se canoniza $G\land C$; para leer, se decide SAT.

Durante una historia, la fórmula inicial junto con todas las continuaciones recibidas sigue siendo una presentación candidata de longitud polinómica en $M$. Los códigos canónicos sucesivos están acotados por esa longitud. Con a lo sumo $M$ actualizaciones, el costo acumulado permanece polinómico en $M$. $\square$

**Alcance.** Es una caracterización del contrato especificado, no una construcción actualmente acreditada como polinómica ni una resolución de $P$ frente a $NP$. Restricciones adicionales sobre el lenguaje —por ejemplo exigir una tabla de verdad o una CNF sin variables interiores auxiliares— definen otro problema de representación y requieren su propio análisis.

## 4. Eliminación completa por tablas densas

Ahora se fija un lenguaje más concreto. Una tabla densa sobre un ámbito $A$ de variables booleanas reserva una entrada para cada asignación de $A$, incluidas las que tienen valor falso. Su tamaño lógico es $2^{|A|}$ entradas.

Considere el siguiente esquema sobre un conjunto no vacío de variables y un orden completo de eliminación $\sigma$:

1. Cada factor inicial conserva su ámbito sintáctico declarado.
2. Para eliminar $v$, se agrupan todos los factores cuyo ámbito contiene $v$.
3. Se forma su conjunción sobre la unión declarada $U_v$ de ámbitos, que incluye $v$.
4. Se produce un mensaje sobre $N_v=U_v\setminus\{v\}$ tomando OR sobre los dos valores de $v$.
5. Se conserva exactamente ese ámbito de mensaje y se continúa hasta eliminar todas las variables.

Si una variable no aparece en factores, se usa la función verdadera sobre esa variable. Los factores constantes también se conservan. El esquema **no reduce ámbitos por independencia funcional, no simplifica sus dependencias y no termina anticipadamente**. Estas condiciones permiten medir su costo estructural independientemente de los valores de las tablas.

El grafo primal $G$ conecta dos variables cuando aparecen juntas en un ámbito inicial. Al eliminar una variable, se conectan entre sí sus vecinos todavía presentes. Defina la anchura inducida del orden como

$$w^*(\sigma)=\max_v |N_v|.$$

**Proposición de tamaños.** En el esquema completo descrito,

$$\boxed{\max_v |\text{mensaje}_v|=2^{w^*(\sigma)}.}$$

Si cada conjunción temporal se materializa como tabla densa sobre $U_v$, además

$$\boxed{\max_v |\text{unión temporal}_v|=2^{w^*(\sigma)+1}.}$$

**Prueba.** Por inducción, el ámbito del mensaje es el vecindario activo de la variable eliminada en el grafo con relleno: agrupar factores reúne exactamente esos vecinos y conservar el mensaje añade la clique correspondiente. Una tabla densa guarda todas las asignaciones de ese ámbito. La unión previa incluye además $v$, de donde el segundo factor dos. $\square$

La caracterización clásica por eliminación da $\min_\sigma w^*(\sigma)=\operatorname{tw}(G)$, la anchura de árbol. En consecuencia, el menor máximo de tamaño de mensaje, entre órdenes completos de **este esquema**, es

$$2^{\operatorname{tw}(G)}.$$

La cantidad cuenta entradas de un mensaje, no la suma de toda la memoria de la ejecución. Una implementación puede calcular la proyección sin almacenar la unión temporal; en ese caso la segunda fórmula describe el ámbito enumerado, no una asignación de memoria obligatoria. El marco clásico de eliminación y sus costos estructurales se desarrolla en [Dechter, *Bucket Elimination*](https://arxiv.org/abs/1302.3572).

## 5. Parámetros y utilidad de la anchura

Sea $v=|V(G)|$ el número de variables y $n$ la longitud binaria de la entrada. Son parámetros distintos: los nombres y las cláusulas también ocupan bits. Una afirmación $\operatorname{tw}(G)=\Omega(v)$ implica mensajes de $2^{\Omega(v)}$ entradas en el esquema de §4; convertirla a una expresión en $n$ requiere una relación explícita entre ambos tamaños.

En sentido constructivo, si se proporciona o calcula en tiempo polinómico un orden con $w^*=O(\log n)$, hay un número polinómico de factores iniciales y sus tablas pueden construirse en tiempo polinómico, la eliminación completa por tablas tiene tiempo y almacenamiento polinómicos. La enumeración de cada unión utiliza a lo sumo $2^{w^*+1}$ asignaciones y un trabajo polinómico de consulta de factores por asignación.

Esto proporciona una familia concreta de realizaciones económicas. También permite comparar órdenes sobre una semántica final fija. Las fórmulas de §4 corresponden al lenguaje de tablas y al esquema declarado; una representación que aproveche estructura adicional se evalúa con sus propias operaciones y cotas.

## 6. Controles reproducibles y papel en el programa

Los [controles de representación SAT](../tests/test_sat_representation_cost.py) usan sólo la biblioteca estándar. Comprueban por enumeración finita:

- la lectura de presentaciones y la actualización contextual;
- una canonización longitud-lex dentro de un universo pequeño explícito;
- la corrección de eliminación completa por tablas;
- el tamaño de mensajes y uniones, comparado con el relleno del grafo;
- los óptimos de anchura para caminos, ciclos y grafos completos pequeños.

La canonización exhaustiva de prueba es un modelo finito de la definición: no implementa el algoritmo condicional de §3 ni demuestra una cota polinómica general. Las demostraciones de la nota y el contrato de costo determinan el alcance.

La contribución al programa es ubicar con precisión tres tareas de revisión: justificar suficiencia contextual, acreditar los costos de una representación y controlar una política completa de recierre. La equivalencia de §3 fija el alcance del objetivo universal; la anchura ofrece un parámetro calculable para familias concretas.

Procedencia: desarrollo del autor sobre economía del recierre y representación contextual SAT, integrado con la teoría clásica de equivalencias y eliminación. Esta nota no reivindica prioridad sobre esas herramientas ni afirma una solución de $P$ frente a $NP$.
