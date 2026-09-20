# Programa de Geometría Relacional
## Diferencia, cierre, identidad, comparación de ritmos y laboratorio Navier–Stokes

**Autor:** Le Matt Ansatz Di Ego  
**Publicación:** 1.0 — septiembre de 2026

Este repositorio presenta una propuesta autocontenida. Su orden lógico es:

\[
\text{unidad singular}
\to\text{reflexión}
\to\text{diferencia}
\to\text{relación}
\to\text{comparación}
\to\text{residuo}
\to\text{recursión}
\to\text{cierre}
\to\text{identidad}.
\]

La pregunta central es si categorías que normalmente se toman como primitivas —cardinalidad, dimensión, geometría, tiempo, fuerza, partícula y escala física— pueden introducirse sólo cuando se vuelven necesarias para conservar información distinguible.

El texto conceptual principal es [`publication/relational_geometry_core.es.md`](publication/relational_geometry_core.es.md). La rama de Navier–Stokes es un laboratorio técnico y no una afirmación de solución del problema de regularidad; su manuscrito está en [`03_navier_stokes/manuscript.md`](03_navier_stokes/manuscript.md).

El repositorio mantiene separados: definición, resultado exacto, derivación interna, correspondencia, hipótesis, observación computacional, pendiente y NO-GO. Esa separación es parte del método, no una nota editorial.

### Lo que sí sostiene esta publicación

- La diferencia se coloca lógicamente antes que el conteo.
- El residuo es información pendiente respecto de una arquitectura de comparación; no se identifica con materia o energía.
- El cierre se modela como reconstrucción interna/autorreferencia, no como simple retorno ni residuo cero.
- Bajo una realización condicional con \(J^2=-I\), existe un ciclo discreto local de orden cuatro.
- \(\pi\) entra limpiamente al representar ese ciclo mediante una familia continua periódica.
- La comparación entre ritmos puede preceder a la elección de un reloj absoluto.
- Navier–Stokes ofrece una ecuación exacta en la que una diferencia transversal debe ser reacreditada dinámicamente para conservar peso frente al crecimiento de la referencia.

### Lo que no sostiene

No se afirma una derivación completa de la física, una identidad entre cierre abstracto y partículas, una derivación universal del cuatro, una derivación de \(\pi\) desde la nada, ni una solución del problema de Navier–Stokes.

Empiece por [`00_orientation/START_HERE.md`](00_orientation/START_HERE.md).
