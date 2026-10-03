# Una arquitectura relacional de información y geometría

El Programa de Geometría Relacional estudia cómo una diferencia llega a convertirse en información utilizable, cómo esa información sostiene una identidad y cómo varias identidades pueden componerse conservando lo relevante. Busca que términos como dimensión, cierre, escala y tiempo tengan una función explícita dentro de esa construcción.

La idea organizadora es sencilla: una descripción es suficiente respecto de las preguntas que permite responder. Cuando aparece una comparación que esa descripción no puede resolver, la representación debe refinarse. El programa estudia qué se conserva, qué se añade y cuál es la extensión mínima necesaria.

## Lo que ya permite hacer

El núcleo define las **cápsulas** como clases de estados indistinguibles bajo un contrato de preguntas y contextos. Esto convierte el cierre en un objeto operacional. Dos interiores pueden ser diferentes y compartir la misma interfaz si responden igual a todas las preguntas del contrato. Una nueva comparación es informativa cuando separa al menos una de esas clases.

En una realización lineal con producto interno, una comparación orientada antisimétrica que conserva la norma determina una estructura concreta: $J^2=-I$, un plano mínimo generado por una novedad y su imagen, y una órbita de cuatro fases. El interés es la conexión explícita entre condiciones de comparación y estructura geométrica. La selección de esas condiciones por un sistema físico es una pregunta adicional identificable.

El desarrollo de segundo orden construye dos coordenadas de fase independientes. Sus dieciséis firmas forman $\mathbb Z_4\times\mathbb Z_4$. Una medida normalizada, local e invariante bajo los dos avances de fase asigna $1/16$ a cada firma: una firma y su complemento tienen razón $1:15$. El resultado establece una estructura de representación, su capacidad de identificación y una medida determinada por simetría. Su traducción a tasas y longitudes se desarrolla como un puente físico con supuestos propios.

La composición de cápsulas añade una herramienta complementaria. Cuando dos relaciones comparten una frontera, se pueden unir sus condiciones y eliminar las variables interiores conservando exactamente las posibilidades de la frontera exterior. El teorema da una semántica precisa a la idea de que un cierre puede actuar como unidad de una construcción posterior. En computación, permite formular por separado la corrección de la composición y el costo de representarla.

## Por qué merece revisión

El programa reúne conceptos amplios alrededor de obligaciones verificables. Una afirmación sobre información se traduce en una partición o factorización; una afirmación sobre geometría se traduce en operadores e invariantes; una afirmación sobre composición se traduce en relaciones y eliminación de variables. Ese paso de lenguaje conceptual a objetos explícitos permite discutir la propuesta en puntos concretos.

Los laboratorios aportan vías de contraste. En Navier–Stokes, la descomposición material distingue crecimiento de magnitud y giro de la vorticidad, y su ley en coordenadas de crecimiento identifica los términos dinámicos que sostienen el cambio transversal. En Yang–Mills, un observable del conmutador de holonomías da una cantidad gauge-invariante que puede examinarse algebraica y numéricamente. En computación, las cápsulas permiten estudiar representación, certificados y composición de restricciones.

La amplitud del programa está en estas conexiones y en una agenda de trabajo compartida. El respaldo de cada resultado se encuentra en su propia demostración o cálculo. Una revisión útil puede determinar tanto la validez de un paso como su relación con métodos existentes, su utilidad y las condiciones para ampliarlo.

## La revisión que buscamos

Hay entradas para especialistas en álgebra y geometría, teoría de la información, complejidad computacional, dinámica de fluidos y teoría gauge. También es valiosa una revisión conceptual que evalúe si las definiciones hacen trabajo explicativo y si los mapas entre niveles están suficientemente especificados.

Las preguntas prioritarias son: qué comparaciones selecciona una dinámica; cómo una estructura relacional adquiere una medida física independiente; qué costo tienen las representaciones composicionales; y qué observables distinguen las propuestas físicas de otras explicaciones. La [guía de revisión](../REVIEW.md) identifica objetos, preguntas y entregables para cada especialidad.

Para entrar en detalle: [núcleo integrado](relational_geometry_core.es.md), [resultados](../04_results/RESULTS_REGISTER.md) y [objetivos físicos](physical_bridges.es.md).
