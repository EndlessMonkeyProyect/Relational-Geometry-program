# De la representación relacional a los observables físicos

El programa busca conectar su arquitectura formal con fenómenos medibles. Esta línea tiene un objetivo definido: construir mapas que preserven las operaciones relevantes y produzcan consecuencias contrastables. Cada puente declara qué estructura utiliza y cómo podría revisarse.

## Tasas, medida y escala

El [resultado de fase y medida](../02_formal_core/phase_measure.es.md) determina dieciséis firmas y un peso elemental $1/16$. Una realización candidata asigna a esas firmas vectores de tasa $\nu_1,\ldots,\nu_{16}$ ortogonales y de igual norma en un espacio interno. Si la norma representa frecuencia y $\omega_U=\|\sum_i\nu_i\|$, entonces

$$\omega_U^2=16\|\nu_1\|^2,\qquad \frac{\omega_V^2}{\omega_U^2}=\frac1{16},\qquad \frac{\omega_V}{\omega_U}=\frac14.$$

Si además el mapa a longitud es $R_i=c/\omega_i$, se obtiene $R_V/R_U=4$. Esta cadena es una consecuencia exacta de la realización adoptada. La revisión física debe establecer por qué las tasas son ortogonales, qué mide su norma y qué selecciona el soporte completo en un sistema concreto. Dieciséis tasas ortogonales requieren un espacio interno de dimensión al menos dieciséis.

La [dinámica cuadrática del comparador](../02_formal_core/second_order_dynamics.md) ofrece otra realización explícita: $\ddot f+\Gamma Gf=0$, con $G=C^\dagger C$ y $\Gamma>0$. Para modos de autovalor positivo, $\varpi_i^2=\Gamma\lambda_i$ y la escala espectral $R_i=\lambda_i^{-1/2}$ cumple $R_i|\varpi_i|=\sqrt\Gamma$. La asociación con una longitud medida requiere un mapa independiente.

## Acción, escala relativa e incorporación

La [acción relacional](../02_formal_core/relational_action_and_phase.es.md) añade un invariante canónico $\mathcal J$ para cada modo estable. Una realización física puede introducir $J_{\rm phys}=S_0\mathcal J$. La identificación de $S_0$, el contenido elemental y un observable de acción son obligaciones del mapa físico.

Las [razones logarítmicas de escala](../02_formal_core/local_comparators_and_relational_laplacian.es.md) permiten trabajar con $\log(\ell_j/\ell_i)$ sin elegir una longitud absoluta. Su compatibilidad en ciclos y su respuesta cuadrática son exactas en la arquitectura declarada. La [incorporación de novedad](../02_formal_core/novelty_incorporation_and_dynamical_modes.es.md) identifica qué condiciones producen un ritmo nuevo antes de asociarle longitud.

## Objetivo protónico

Al elegir $R_U=\hbar/(m_pc)$ en la realización anterior, la longitud objetivo es

$$R_\star=4\frac{\hbar}{m_pc}\approx0.841236\ \mathrm{fm}.$$

La expresión y el valor aproximado se conservan como objetivo de contraste de los materiales aportados. La pregunta física es derivar una respuesta electromagnética que permita relacionar esa longitud con el radio de carga rms obtenido del factor de forma. También debe establecerse qué propiedad del sistema selecciona las dieciséis firmas y la realización de tasa. La evaluación de antecedentes y de predicciones adicionales forma parte de la revisión solicitada; esta edición no asigna prioridad histórica a la expresión.

## Otros dominios

| Dominio | Objeto de trabajo | Revisión que puede producir un avance |
|---|---|---|
| Química | Descriptores racionales de ocupaciones y pesos de bloques electrónicos | Medir aporte predictivo fuera de muestra frente a número atómico, grupo, período y conteo electrónico |
| Gravedad | Interpretación relacional de cambios entre sistemas | Construir una dinámica covariante y su mapa a observables |
| Navier–Stokes | Tasas materiales de crecimiento y giro | Obtener una escala espacial independiente y comprobar su relación con las tasas bajo escalamiento parabólico |
| Yang–Mills | Defecto de conmutación de holonomías y formas relacionales | Relacionar coercividad, dinámica física y control de escala |
| Tiempo y dimensión | Comparación de cambios y capacidad representacional | Especificar el reloj operacional y el mapa a geometría espacial |

Estas líneas amplían la agenda del programa. Su siguiente contribución debe ser una ley, observable o protocolo definido que permita distinguir realizaciones físicas. Véanse [revisión R7](../REVIEW.md), [Navier–Stokes](../03_navier_stokes/README.md) y [Yang–Mills](../06_yang_mills/README.md).

Procedencia: *Núcleo integrado*, partes VII–XI; *Hilo canónico de cierre, localidad y escala relacional*; puentes físicos de la edición fuente 2.0.0. La cifra protónica se reproduce como valor documental aproximado, sin actualizar una comparación experimental.
