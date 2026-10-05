# Propagación causal y recursos de cierre

**Le Matt Ansatz Di Ego · Resultado de dependencia local y síntesis de recursos**

La localidad controla hasta dónde llega una diferencia por actualización. Separarla de la cantidad de compatibilidades y del trabajo para acreditarlas permite comparar los laboratorios mediante preguntas precisas.

## 1. Cono de dependencia

Sea $\mathcal G=(V,E)$ un grafo fijo no dirigido y $r\ge1$. Cada actualización en $i$ depende de estados en la bola $B_r(i)$ de la capa actual y de su propio estado anterior. Supóngase que dos historias coinciden fuera de $S$ en ambas capas iniciales $n=-1,0$.

Tras $n\ge0$ pasos,

$$\boxed{\operatorname{supp}(x_n-\widetilde x_n)\subseteq B_{rn}(S)}.$$

Prueba: el caso inicial es la hipótesis. Si $i\notin B_{r(n+1)}(S)$, todos los estados que consulta en la capa $n$ quedan fuera de $B_{rn}(S)$, y su memoria propia coincide por la hipótesis inductiva. La siguiente salida también coincide. La inducción controla ambas capas.

En unidades de enlaces por actualización la cota es $v_{\rm dep}\le r$. Se puede normalizar esa cota a uno midiendo distancia en unidades de $r$ enlaces. Una dinámica concreta alcanza la cota sólo si transmite efectivamente diferencias hasta el frente.

## 2. Acreditación y coordinación

Si la respuesta requerida en $v$ cambia entre esas dos historias, cualquier procedimiento sujeto al mismo contrato local requiere al menos

$$n_{\min}\ge\left\lceil d_{\mathcal G}(v,S)/r\right\rceil.$$

En un grafo conectado, la influencia desde $S$ hasta todos los nodos requiere al menos la excentricidad dividida por $r$, redondeada hacia arriba. Para una red infinita con $\sup_v d_{\mathcal G}(v,S)=\infty$, ninguna cantidad finita de pasos cubre toda la red.

Son cotas de dependencia desde información localizada. Los contratos con información precompartida o consultas globales deben registrar esos recursos por separado.

## 3. Cuatro recursos diferentes

| Recurso | Qué mide |
|---|---|
| Distancia de transporte | Enlaces que debe atravesar una dependencia |
| Rondas de acreditación | Actualizaciones hasta producir una conclusión certificada |
| Anchura de interfaz | Compatibilidades o datos que se conservan simultáneamente |
| Trabajo por actualización | Costo de construir, consultar y verificar cada paso |

En un grafo explícito conectado con $v$ vértices, el diámetro es como máximo $v-1$. Esto acota la distancia geométrica, no las rondas ni su costo. Un análisis de complejidad debe controlar los cuatro recursos y el tamaño en bits de las representaciones.

## 4. Aplicaciones con obligaciones propias

En [computación](../05_computation/README.md), la composición exacta da corrección semántica. Un procedimiento eficiente añade cotas uniformes de representación, número de pasos y construcción de cada certificado.

En [Yang–Mills](../06_yang_mills/README.md), las comparaciones deben controlar varianza mediante una desigualdad cuantitativa. La detección de toda función no constante es una etapa; la cota coerciva uniforme y la comparación con la dinámica son otras.

En [Navier–Stokes](../03_navier_stokes/README.md), se estudia una PDE con difusión y presión elíptica. El cono aquí demostrado pertenece a la regla de actualización declarada, mientras el laboratorio de fluidos mide balances materiales y su resolución numérica.

## 5. Puente dimensional

Si una realización asigna longitud $\ell_0$ al enlace y duración $\tau_0$ al paso, la cota física candidata es $r\ell_0/\tau_0$. Identificar esa magnitud con una velocidad medida exige el mapa físico correspondiente.

La contribución de esta separación es un lenguaje de recursos común con pruebas de dependencia verificables. Véanse la [ontología](../01_foundations/ontology_of_difference_and_closure.es.md) y las [condiciones de control global](novelty_and_global_control.es.md).

Procedencia: desarrollo de normalización causal y profundidad–anchura aportado por el autor.
