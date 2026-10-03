# Yang–Mills: composición no abeliana y comparaciones sobre estados

Esta rama construye un puente entre la información que aparece al componer relaciones y el estudio de sistemas gauge. Su bloque algebraico ofrece ejemplos exactos de novedad contextual, una selección condicional del álgebra compacta mínima y un observable explícito de incompatibilidad en $SU(2)$. La siguiente etapa estudia cuándo comparaciones locales pueden controlar variaciones globales de un estado.

El valor de esta arquitectura es que cada transición tiene un objeto matemático y una pregunta de revisión: composición, descriptor gauge-invariante, forma sobre estados, desigualdad cuantitativa y comportamiento de escala.

## 1. Una diferencia visible al componer

El grupo de cuaterniones:

$$
Q_8=\{\pm1,\pm i,\pm j,\pm k\}
$$

contiene dos elementos de orden cuatro cuya composición depende del orden: $ij=k$ y $ji=-k$. Da una realización finita de la idea de que el contexto de composición puede aportar información que las observaciones separadas no determinan.

En una realización por matrices de $SU(2)$, los pares $(i\sigma_x,i\sigma_x)$ y $(i\sigma_x,i\sigma_y)$ tienen las mismas trazas individuales, ambas cero. El primer par conmuta; el segundo tiene conmutador de grupo $-I$. Esta comparación es un testigo explícito de no-factorización respecto de las dos trazas individuales.

El tamaño ocho es mínimo entre grupos finitos con dos elementos de orden cuatro no conmutantes: la presencia de un elemento de orden cuatro exige que el orden del grupo sea múltiplo de cuatro, y el caso de orden cuatro es abeliano. $Q_8$ alcanza la cota.

## 2. Álgebra compacta mínima bajo hipótesis declaradas

El paso continuo considera grupos con una representación lineal real fiel, finita dimensional, que preserva un producto interno positivo, y admite su cierre topológico. En esa clase compacta se exige no conmutatividad infinitesimal y se busca el álgebra de Lie de dimensión mínima.

Para una forma positiva e invariante, si $[X,Y]\ne0$, se cumple:

$$
\langle[X,Y],X\rangle=\langle[X,Y],Y\rangle=0.
$$

Como $X,Y$ son linealmente independientes, $X,Y,[X,Y]$ generan un espacio de dimensión tres. La cota se realiza mediante:

$$
\mathfrak{so}(3)\simeq\mathfrak{su}(2).
$$

Así, el álgebra compacta no abeliana mínima dentro de esta clase es tridimensional. La afirmación selecciona un álgebra bajo hipótesis explícitas; la elección de un grupo global y su interpretación física se declaran en cada aplicación.

En la realización $\mathfrak{so}(3)\simeq(\mathbb R^3,\times)$, para $R\ne0$, el operador $T(A)=A\times R$ satisface sobre $R^\perp$:

$$
T^2=-\|R\|^2I.
$$

Por tanto $J=T/\|R\|$ cumple $J^2=-I$ y $J^4=I$ en ese plano. Esto proporciona una conexión exacta con el sector rotatorio del núcleo relacional.

## 3. Observable exacto de incompatibilidad

Para $U,V\in SU(2)$, definimos:

$$
\nu(U,V)=1-\frac12\operatorname{ReTr}(UVU^{-1}V^{-1}).
$$

La identidad:

$$
\|UV-VU\|_F^2
=4-2\operatorname{ReTr}(UVU^{-1}V^{-1})
$$

se obtiene expandiendo la norma de Frobenius y usando la unitariedad y la ciclicidad de la traza. En consecuencia:

$$
\boxed{\nu(U,V)=\frac14\|UV-VU\|_F^2},\qquad
0\le\nu\le2,\qquad
\nu=0\Longleftrightarrow UV=VU.
$$

El observable mide exactamente el defecto de conmutación del par elegido.

Si:

$$
U=\cos\alpha\,I+i\sin\alpha\,\hat a\cdot\vec\sigma,
\qquad
V=\cos\beta\,I+i\sin\beta\,\hat b\cdot\vec\sigma,
$$

la regla de producto de matrices de Pauli da:

$$
\nu=2\sin^2\alpha\sin^2\beta\,[1-(\hat a\cdot\hat b)^2].
$$

Esta fórmula permite comprobar directamente cómo intervienen los ángulos y la orientación relativa de los ejes.

### Información suficiente para reconstruirlo

Sean $x=\operatorname{Tr}U$, $y=\operatorname{Tr}V$ y $z=\operatorname{Tr}(UV)$. Cayley–Hamilton da $U^{-1}=xI-U$, $V^{-1}=yI-V$ y $\operatorname{Tr}((UV)^2)=z^2-2$. Al expandir:

$$
\begin{aligned}
\operatorname{Tr}(UVU^{-1}V^{-1})
&=xyz-x(yz-x)-y(xz-y)+(z^2-2)\\
&=x^2+y^2+z^2-xyz-2.
\end{aligned}
$$

Por tanto:

$$
\nu=2-\frac12(x^2+y^2+z^2-xyz).
$$

Las dos trazas individuales dejan abierta una diferencia que la tercera traza permite resolver. Este ejemplo conecta de manera concreta novedad contextual y suficiencia de una firma.

## 4. Descriptor gauge-invariante en una red

Fijemos una familia de pares de lazos $(p,q)$, caminos de transporte hacia un punto base común y pesos $w_{pq}\ge0$. Definimos:

$$
\mathcal N_a[U]=\sum_{(p,q)}w_{pq}\,\nu(U_p,U_q).
$$

Una transformación gauge conjuga simultáneamente las holonomías transportadas al mismo punto. El conmutador también se conjuga y su traza se conserva. Por ello $\mathcal N_a$ es gauge-invariante y no negativo.

El descriptor se anula cuando todos los pares considerados conmutan, incluidos los sectores abelianos y las configuraciones contenidas en un mismo subgrupo de Cartan. También cumple $\nu(\epsilon U,\eta V)=\nu(U,V)$ para $\epsilon,\eta\in\{\pm1\}$. Estas propiedades especifican qué diferencias registra y orientan la elección de comparadores adicionales.

Para campos clásicos suaves, con plaquetas:

$$
U_{\mu\nu}(x)=\exp(ia^2gF_{\mu\nu}(x)+O(a^3)),
$$

el término principal es:

$$
\nu(U_{\mu\nu},U_{\rho\sigma})
=\frac{a^8g^4}{4}\operatorname{Tr}
\bigl([F_{\mu\nu},F_{\rho\sigma}]^\dagger
[F_{\mu\nu},F_{\rho\sigma}]\bigr)+\cdots.
$$

Esta expansión identifica el contenido clásico local del descriptor. La definición y renormalización del operador compuesto cuántico constituyen una etapa posterior.

## 5. De comparaciones locales a control global

El objeto siguiente es una forma sobre funciones o estados. Un candidato es la suma de varianzas condicionales por bloques:

$$
\mathcal D_{\mathrm{block}}^{(\rho)}[f]
=\sum_b\mathbb E_\rho
\left[\operatorname{Var}_\rho(f\mid U_{b^c})\right].
$$

Cada término mide cuánto varía $f$ al permitir cambios dentro de un bloque y mantener fijo su contexto exterior. La medida $\rho$, los bloques, el espacio de funciones y las condiciones de borde forman parte de la definición.

El programa plantea cinco etapas de revisión:

| Etapa | Resultado buscado | Por qué importa |
|---|---|---|
| Irreducibilidad | $\mathcal D_{\mathrm{rel}}[f]=0$ implica $f$ constante casi seguramente en el sector pertinente | Establece que las comparaciones alcanzan todas las diferencias admitidas |
| Coercividad | $\operatorname{Var}_\rho(f)\le C_{\mathrm{rel}}\mathcal D_{\mathrm{rel}}[f]$ | Convierte esa capacidad de distinguir en una cota cuantitativa |
| Comparación dinámica | Relacionar la forma relacional con la forma de Dirichlet de Yang–Mills | Conecta el control relacional con una afirmación espectral |
| Control de escala | Acotar las constantes al variar volumen, espaciado y acoplamiento | Determina qué control sobrevive a los límites físicos |
| Construcción continua | Construir el límite físico y transferir la desigualdad | Fija el alcance de la conclusión en una teoría continua |

En una red con variables $SU(2)$, el espacio de configuración sigue siendo continuo aunque el grafo tenga pocos enlaces. La prueba de núcleo constante y la cota de Poincaré son, por ello, obligaciones distintas.

Si la comparación física usa directamente la medida del vacío $\mu_0$, la forma ya incorpora información dinámica. Si se empieza con una medida relacional distinta $\rho$, el puente debe justificar también la transferencia de medidas. Por ejemplo, bajo cotas explícitas:

$$
\operatorname{Var}_{\mu_0}(f)\le C_{\mathrm{tr}}\operatorname{Var}_{\rho}(f),
\qquad
\mathcal D_{\mathrm{rel}}^{(\rho)}[f]\le C_{\mathrm{YM}}\mathcal E_{\mathrm{YM}}[f],
$$

se obtiene:

$$
\operatorname{Var}_{\mu_0}(f)
\le C_{\mathrm{tr}}C_{\mathrm{rel}}C_{\mathrm{YM}}\mathcal E_{\mathrm{YM}}[f].
$$

Para una misma medida puede tomarse $C_{\mathrm{tr}}=1$. Todas las constantes deben llevar sus dependencias en volumen, espaciado y acoplamiento. La coercividad apropiada, su comparación física y la construcción continua son los objetivos abiertos de esta rama.

## 6. Revisión solicitada

El [control gaussiano por bloques](GAUSSIAN_CONTROL.md) incluye código ejecutable, protocolo rápido y una tabla de seis casos verificados. Permite examinar la forma relacional en modelos finitos lineales, con un observable de prueba especificado.

Las identidades algebraicas anteriores pueden revisarse por cálculo directo. El programa dinámico requiere experiencia en teoría gauge, análisis de formas de Dirichlet, desigualdades funcionales y límites de escala.

Proponemos tareas concretas:

- reproducir las identidades de $\nu$ y los testigos de no-factorización;
- fijar un grafo pequeño, la familia de bloques, la medida y el sector gauge-invariante;
- caracterizar el núcleo del operador de comparación;
- obtener una cota de Poincaré con dependencias explícitas;
- estudiar controles gaussianos abelianos y variantes masivas para comprobar el comportamiento de escala;
- formular el puente con Yang–Mills y la transferencia de medidas sobre dominios precisos.

La convocatoria y el formato de observaciones están en [Revisión del programa](../REVIEW.md).

Procedencia: *Programa Relacional — Rama Yang–Mills*, §§3–13 y 18–29; *Cierre, localidad y escala relacional mínima*, §§37–40. Las identidades se exponen aquí con sus hipótesis; los resultados de análisis y de límite continuo se presentan como programa de trabajo.
