# Composición de espines e información relacional

**Le Matt Ansatz Di Ego · Ejemplo trabajado en mecánica cuántica estándar**

Dos espines proporcionan una aplicación concreta de la pregunta central del
programa: ¿qué debe conservar una descripción para poder componerse con otra?
La respuesta depende del contrato. Para medir el espín total de un par en un
estado producto basta su ángulo relativo; para reutilizar cada espín frente a
cualquier compañero, la interfaz conserva su estado de Bloch.

El desarrollo conecta esa suficiencia con correlaciones del singlete,
registros de medición y un observable ternario. La física empleada es mecánica
cuántica estándar. El aporte del programa es organizarla mediante sus
[interfaces contextuales](../02_formal_core/contextual_identity_and_scale_promotion.es.md)
y su [resolución respecto de una referencia](../02_formal_core/resolution_and_modal_weights.es.md).

## 1. Estados, composición y pregunta

Un espín $1/2$ se representa por

$$
\rho_n=\tfrac12(I+n\cdot\sigma),\qquad n\in\mathbb R^3,\quad \|n\|\le1,
$$

donde $\sigma=(\sigma_x,\sigma_y,\sigma_z)$ son las matrices de Pauli. Para un
estado puro, $\|n\|=1$. La preparación independiente de dos espines es

$$J(\rho_n,\rho_m)=\rho_n\otimes\rho_m.$$

En $\mathcal H=\mathbb C^2\otimes\mathbb C^2$, los proyectores de espín total son

$$
\Pi_1=\frac{3I+\sum_a\sigma_a\otimes\sigma_a}{4},\qquad
\Pi_0=\frac{I-\sum_a\sigma_a\otimes\sigma_a}{4}.
$$

Son ortogonales, suman $I$ y tienen rangos tres y uno, respectivamente:
triplete $F=1$ y singlete $F=0$.

**Proposición.** Para un estado producto,

$$
\boxed{P(F=1)=\frac{3+n\cdot m}{4},\qquad
P(F=0)=\frac{1-n\cdot m}{4}.}
$$

**Prueba.** $\operatorname{Tr}(\rho_n\sigma_a)=n_a$ y las expectativas factorizan
en el producto. Sustituirlas en los proyectores da las dos probabilidades.
$\square$

## 2. Interfaz del par e interfaz reutilizable

### Una pregunta sobre el par ya preparado

Para la pregunta escalar $P(F=1)$ sobre estados producto,

$$\Phi(\rho_n,\rho_m)=n\cdot m$$

es una interfaz suficiente mínima: la respuesta es función de $\Phi$ y, a la
inversa, $\Phi=4P(F=1)-3$. La información de ambas cantidades es equivalente para
esa pregunta. La interfaz es invariante bajo una rotación simultánea de los dos
espines. En pares puros ordenados, el producto escalar también clasifica sus
órbitas bajo rotaciones simultáneas.

### Reutilización frente a todos los compañeros

Declare ahora como continuaciones todas las preparaciones de un compañero de
Bloch unitario $m$, seguidas de la medición de $F$. Entonces

$$
n\equiv n'
\iff n\cdot m=n'\cdot m\quad\text{para todo }\|m\|=1
\iff n=n'.
$$

**Prueba.** Basta tomar los tres vectores de una base ortonormal para recuperar
las tres componentes. $\square$

Por tanto, el vector de Bloch es una interfaz exacta reutilizable para este
contrato. El ángulo relativo pertenece al par, mientras que la descripción de
cada entrada debe permitir calcularlo con los compañeros admitidos. Esta
distinción concreta la relación entre consulta actual y
[continuación de una identidad](../02_formal_core/collective_dynamics_on_quotients.es.md).

## 3. Singlete, simetría y correlaciones

El vector

$$|s\rangle=(|{\uparrow\downarrow}\rangle-|{\downarrow\uparrow}\rangle)/\sqrt2$$

genera el subespacio unidimensional de vectores invariantes bajo la
representación diagonal $U\otimes U$, $U\in SU(2)$. La representación se
descompone en singlete y triplete. Para operadores densidad, los estados
invariantes bajo conjugación diagonal tienen la forma

$$
\rho_a=a\Pi_0+(1-a)\Pi_1/3,\qquad 0\le a\le1.
$$

Esto distingue la referencia de un subespacio de vectores de una distribución
de poblaciones entre sectores.

La densidad del singlete satisface

$$
\rho_s=|s\rangle\langle s|
=\frac14\left(I\otimes I-\sum_a\sigma_a\otimes\sigma_a\right),
\qquad
\operatorname{Tr}_1\rho_s=\operatorname{Tr}_2\rho_s=I/2.
$$

La expansión muestra dónde está la estructura: en las correlaciones conjuntas,
con $\langle\sigma_a\otimes\sigma_b\rangle=-\delta_{ab}$; los términos de
polarización individual son cero.

Con la resolución de Hilbert–Schmidt

$$\mathcal R_{\rm q}(\rho)=\log_2(d\,\operatorname{Tr}\rho^2),$$

el singlete tiene resolución conjunta de dos bits y resolución marginal cero.
Para cualquier estado puro de dos qubits,
$\mathcal R_{\rm q}(\rho)=2$ y
$\mathcal R_{\rm q}(\rho_A)=1-S_2(\rho_A)$, donde
$S_2(\rho_A)=-\log_2\operatorname{Tr}\rho_A^2$.
Los bits designan esta magnitud definida, no un número de bits clásicos
extraíbles de una sola medición.

La preparación de estados entrelazados y su evolución se especifican mediante
operaciones adicionales al producto de preparaciones independientes.

## 4. Proporción estadística y referencia modal

Un ensamble de orientaciones puras uniformes e independientes tiene densidad
media $(I/2)\otimes(I/2)=I_4/4$. Por las trazas de los proyectores,

$$
\overline{P(F=0)}:\overline{P(F=1)}=1:3.
$$

La independencia y el ensamble fijan aquí la proporción. En el sistema físico,
las poblaciones de los niveles también dependen de su preparación y de los
procesos de transición.

La partición singlete–triplete actúa en el espacio físico de vectores de dimensión
cuatro. La realización modal de
[resolución y peso](../02_formal_core/resolution_and_modal_weights.es.md)
actúa en el espacio real de operadores hermíticos de dimensión dieciséis: su
referencia normalizada es $I_4/2$ y su complemento tiene dimensión quince.
Allí se calcula $r_{\rm ref}^{(\rm q)}=1/(4\operatorname{Tr}\rho^2)$.
Para comparar esa cantidad con una probabilidad de sector debe declararse un
mapa entre ambos contratos, con sus espacios y proyectores correspondientes.

## 5. Probabilidades, resultados medidos y fibras de registros

La pregunta $q_F(\rho)=\operatorname{Tr}(\rho\Pi_F)$ devuelve una probabilidad.
La medición proyectiva ideal, en cambio, entrega un registro discreto
$f\in\{0,1\}$ y, condicionado a un resultado con probabilidad positiva, el estado

$$
\rho\longmapsto\frac{\Pi_f\rho\Pi_f}{\operatorname{Tr}(\rho\Pi_f)}.
$$

Son tres objetos tipados: estado preparado, distribución de resultados y registro
observado.

Sobre los registros ya obtenidos, la proyección

$$
(1s,f)\longmapsto(1s)
$$

tiene dos elementos en su fibra cuando ambos resultados son admisibles. Para
reconstruir ese registro fino desde la etiqueta gruesa hace falta una etiqueta
binaria. Esta aplicación del
[refinamiento contextual](../02_formal_core/redistributive_closure_and_information_channels.es.md)
se refiere al registro de $F$, no a una codificación de la distribución continua
ni a una descripción completa del estado cuántico.

## 6. Transición hiperfina como ejemplo dinámico físico

Para el sector de espín del hidrógeno $1s$ aislado y sin campo externo, el
Hamiltoniano efectivo isotrópico

$$
H_{\rm hf}=\frac{A_{\rm hf}}4\sum_a\sigma_a\otimes\sigma_a,\qquad A_{\rm hf}>0,
$$

asigna $E_1=A_{\rm hf}/4$ y $E_0=-3A_{\rm hf}/4$. La separación es
$A_{\rm hf}$. La interacción con el campo electromagnético habilita el canal
radiativo dipolar magnético $F=1\to0$.

La frecuencia medida adoptada en la compilación de Kramida es
$\nu_{\rm hf}=1420.405751768\ \mathrm{MHz}$, con incertidumbre conservadora de
$1\ \mathrm{mHz}$. Da $\lambda=c/\nu_{\rm hf}\simeq21.106\ \mathrm{cm}$ y
$h\nu_{\rm hf}\simeq5.874\ \mu\mathrm{eV}$.
[Fuente: Kramida, NIST, §3](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=842564).

El fotón es un portador físico de energía y momento angular en ese proceso
radiativo. Vincular sus registros con una fibra contextual requiere especificar
la dinámica átomo–campo, la preparación y las preguntas registradas. La operación
tensorial y el conteo de una fibra son la parte informacional del contrato;
el acoplamiento radiativo es la parte dinámica. El número espectroscópico se usa
como dato externo, no como predicción del programa.

Otros procesos físicos también redistribuyen las poblaciones hiperfinas. La
investigación de intercambio de espín en colisiones protón–hidrógeno ofrece
una realización concreta de esa dependencia dinámica.
[Fuente: Furlanetto y Furlanetto](https://arxiv.org/abs/astro-ph/0702487).

## 7. Tres espines y orientación ternaria

Para tres estados producto con vectores de Bloch $n_1,n_2,n_3$, declare como
consultas de parejas los escalares rotacionalmente invariantes
$\langle\sigma_i\cdot\sigma_j\rangle=n_i\cdot n_j$. Entonces

$$
P(S=3/2)=\frac{3+\sum_{i<j}n_i\cdot n_j}{6}.
$$

Una consulta conjunta adicional es la quiralidad escalar

$$
\chi=\sum_{abc}\epsilon_{abc}\,
\sigma_a\otimes\sigma_b\otimes\sigma_c,\qquad
\langle\chi\rangle=n_1\cdot(n_2\times n_3).
$$

$\chi$ es hermítica: los factores actúan en sitios distintos, con coeficientes
reales. La factorización de expectativas prueba la segunda identidad.
Bajo inversión de todos los vectores de Bloch, los productos escalares de
parejas se conservan y la quiralidad invierte su signo. El contrato de consultas
de parejas aquí elegido permite así añadir una orientación ternaria.

Fije el ciclo $C|a,b,c\rangle=|c,a,b\rangle$. Con esta convención,

$$C-C^{-1}=-\frac{i}{2}\chi.$$

La expansión de los intercambios
$P_{ij}=(I+\sigma_i\cdot\sigma_j)/2$ prueba la identidad. La quiralidad queda
vinculada a la parte antisimétrica de la operación cíclica. Las consultas
escalares de parejas declaradas son una selección de observables; las matrices
densidad reducidas completas constituyen un contrato más rico.

## Papel en el programa y verificación

Este ejemplo proporciona interfaces exactas, una representación explícita de
información en correlaciones y una extensión ternaria medible dentro de la
mecánica cuántica. La interpretación ontológica puede organizar esos resultados
manteniendo separados estados, consultas, registros y dinámica.

Las [pruebas de composición de espines](../tests/test_spin_composition.py)
comprueban proyectores, probabilidades, reconstrucción de Bloch, correlaciones,
instrumento de medición, espectro hiperfino y quiralidad por matrices finitas.
Las pruebas son controles del modelo declarado, no una nueva medición física.

~~~shell
python -X utf8 -B -m unittest discover -s tests -p test_spin_composition.py -v
~~~
