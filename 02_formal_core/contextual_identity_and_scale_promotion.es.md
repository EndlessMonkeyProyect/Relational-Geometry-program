# Identidad colectiva, suficiencia contextual y promoción de escala

**Le Matt Ansatz Di Ego · Construcción formal con ejemplos finitos**

Una estructura puede funcionar como una nueva unidad cuando su interfaz permite responder y componer sin reconstruir todos sus estados interiores. Esta nota concreta ese paso: define qué conserva la identidad colectiva, qué detalles deja de exigir y qué operaciones puede seguir realizando.

El punto de partida es el [cierre suficiente](closure_information.es.md). La contribución de esta integración es articularlo con recuperabilidad de constituyentes, promoción de escala e [incorporación dinámica](novelty_incorporation_and_dynamical_modes.es.md).

## 1. Estado compuesto y contrato exterior

Sea $X_C\subseteq\prod_{i=1}^m\Sigma_i$ un conjunto no vacío de estados admisibles. Las proyecciones $\pi_i:X_C\to\Sigma_i$ separan conjuntamente los estados. La elección de constituyentes forma parte del modelo.

Declare una familia de consultas $Q_{\rm ext}$ y operaciones exteriores. Los contextos de un hueco $\mathfrak C_{\rm ext}$ incluyen el contexto identidad, la composición de contextos y la fijación de los demás argumentos de cada operación mediante estados admisibles. Las operaciones consideradas en el teorema siguiente son totales y cierran en $X_C$.

Defina

$$x\equiv_{\rm ext}y
\iff q(c[x])=q(c[y])
\quad\text{para todo }q\in Q_{\rm ext},\ c\in\mathfrak C_{\rm ext}.$$

[DEFINICIÓN] El resolutor es la familia de respuestas contextuales; sus fibras son las clases contextuales. «Identidad colectiva» en esta nota designa esa equivalencia matemática relativa al contrato. La ontología actual usa «singularidad relacional» para una diferencia cerrada reutilizable; su realización exige acreditar las operaciones pertinentes. Ampliar preguntas u operaciones puede exigir una interfaz más fina.

## 2. Interfaz canónica y suficiencia mínima

Sea

$$\Sigma_C=X_C/{\equiv_{\rm ext}},\qquad \sigma_C(x)=[x]_{\rm ext}.$$

**Proposición.** Toda consulta contextual factoriza por $\sigma_C$. Si $s:X_C\to S$ es otra interfaz suficiente, es decir,

$$s(x)=s(y)\Rightarrow x\equiv_{\rm ext}y,$$

existe un único mapa $f:s(X_C)\to\Sigma_C$ con $\sigma_C=f\circ s$.

**Prueba.** Las consultas son constantes en cada clase por definición. Para la segunda afirmación, defina $f(s(x))=[x]_{\rm ext}$; la suficiencia hace independiente la elección de representante y la imagen de $s$ garantiza unicidad. $\square$

Así, el cociente es la descripción exacta más gruesa que conserva las respuestas declaradas. Su existencia no proporciona automáticamente una representación pequeña ni un algoritmo eficiente para calcularlo.

## 3. Composición sobre identidades

Para una operación $\star:X_C\times X_C\to X_C$, existe una operación colectiva bien definida con

$$\sigma_C(x\star y)=F_\star(\sigma_C(x),\sigma_C(y))$$

si y sólo si la equivalencia es una congruencia:

$$x\equiv_{\rm ext}x',\ y\equiv_{\rm ext}y'
\Rightarrow x\star y\equiv_{\rm ext}x'\star y'.$$

**Prueba.** Si existe $F_\star$, entradas de igual clase dan salidas de igual clase. Recíprocamente, defina $F_\star([x],[y])=[x\star y]$; la congruencia elimina la dependencia de representantes. $\square$

La familia completa de contextos descrita en §1 garantiza esta propiedad: primero sustituya el argumento izquierdo usando el contexto $c[-\star y]$ y después el derecho usando $c[x'\star-]$. Para operaciones parciales también debe conservarse la condición de admisibilidad, no sólo la salida.

Este es el significado preciso de continuar componiendo sin reabrir el interior. El [recierre de restricciones](compatible_reclosure.es.md) proporciona otra realización del mismo requisito.

## 4. Qué individualidades pueden recuperarse

Escriba $d\preceq s$ cuando $d$ factoriza por $s$. Defina

$$\mathcal R_{\rm parts}(\sigma_C)
=\{i:\pi_i\preceq\sigma_C\}.$$

**Proposición.**

$$\boxed{\sigma_C\text{ inyectiva}
\iff \pi_i\preceq\sigma_C\quad\text{para todo }i}.$$

Si $\sigma_C$ es inyectiva, su inversa sobre la imagen recupera todas las coordenadas. Si todas las coordenadas se recuperan, dos estados con la misma interfaz coinciden en cada constituyente y por tanto son iguales. $\square$

La no inyectividad implica que al menos una coordenada constituyente completa no puede recuperarse desde esa interfaz. No significa que desaparezca toda información parcial sobre cada parte. El conjunto $\mathcal R_{\rm parts}$ depende de la descomposición física o lógica declarada; no es invariante bajo cualquier recodificación que mezcle constituyentes.

## 5. Promoción colectiva compresiva

En esta nota, una promoción colectiva compresiva requiere:

1. Un dominio admisible y un contrato exterior explícitos.
2. Una interfaz suficiente, no inyectiva y no constante.
3. Descenso de las operaciones posteriores, incluyendo su admisibilidad.
4. Una realización de sus clases como estados utilizables del nivel siguiente.

La no constancia excluye una interfaz que no conserva ninguna distinción; la no inyectividad distingue esta promoción compresiva de una recodificación completa. Son criterios operacionales, no una afirmación automática de emergencia física.

El nivel de cierre no es una longitud ni una duración. Una realización física debe construir esos mapas por separado.

### Novedad y condensación son pasos diferentes

Una comparación nueva refina una firma $\Phi$ a $(\Phi,d)$. El cierre posterior puede condensar detalles del estado enriquecido en una interfaz suficiente para otro contrato. La novedad se evalúa respecto de la firma anterior; la compresión, respecto del estado compuesto.

Estos dos pasos pueden coexistir, pero ninguno implica el otro. Si el contrato exige recuperar cierta herencia o una magnitud como la acción modal, hay que comprobar que también factoriza por la interfaz elegida. La [arquitectura de canales](redistributive_closure_and_information_channels.es.md) permite registrar información disponible fuera de la referencia colectiva.

## 6. Modelo de dos bits: composición y cambio de contrato

Tome $X_C=\{0,1\}^2$, con operación XOR coordenada a coordenada, y consulta exterior de paridad:

$$\sigma(a,b)=a\mathbin{\oplus}b.$$

Los contextos admiten componer con cualquier estado fijo. El cociente tiene las clases

$$\{00,11\},\qquad \{01,10\}.$$

La interfaz es suficiente para todos esos contextos porque

$$\sigma(x\mathbin{\oplus}y)=\sigma(x)\mathbin{\oplus}\sigma(y).$$

Ninguno de los dos bits completos puede recuperarse de la paridad, aunque persiste una distinción colectiva no trivial. La identidad se reutiliza mediante XOR de paridades.

Ahora añada la consulta por el primer bit. La interfaz refinada $(a\oplus b,a)$ recupera también $b=(a\oplus b)\oplus a$ y se vuelve inyectiva. La interfaz anterior dejó de ser suficiente para el contrato ampliado. Se ha cambiado el acceso pertinente, no demostrado una destrucción física de información.

## 7. Interior dinámico y continuidad de la identidad

Una evolución puede recorrer estados de una misma fibra $\sigma_C^{-1}(s)$ sin cambiar la identidad observada. Para predecir la evolución entre fibras hace falta una ley colectiva bien definida, no sólo una instantánea suficiente.

En el sector lineal, la [dinámica en cocientes](collective_dynamics_on_quotients.es.md) demuestra el criterio exacto $TK=\bar KT$, conservando las dos capas iniciales de la recurrencia. Una suma colectiva puede cerrar aun cuando sus componentes originales estén acoplados.

Si la interfaz admite una realización diferenciable, $D\sigma_C(x)v=0$ expresa invisibilidad a primer orden en ese punto. No garantiza permanencia de una trayectoria en la fibra; por ejemplo, la derivada de $x^2$ se anula en cero, pero desplazamientos no nulos cambian su valor.

## 8. Qué permite revisar

El modelo da pruebas concretas de suficiencia, composición y recuperabilidad, y un caso controlado de cómo falla una interfaz al ampliar las consultas. El próximo paso de cada aplicación es seleccionar su contrato independientemente del resultado buscado y comprobar persistencia, costo y observables preservados.

Procedencia: integración del desarrollo del autor sobre promoción de cierre a identidad colectiva (MF85), enlazada al núcleo previo de información y recierre. Las construcciones de cociente y congruencia son estándar; aquí se especifica su función dentro del programa. [Controles finitos](../tests/test_contextual_identity_and_channels.py). [Ontología](../01_foundations/ontology_of_difference_and_closure.es.md).
