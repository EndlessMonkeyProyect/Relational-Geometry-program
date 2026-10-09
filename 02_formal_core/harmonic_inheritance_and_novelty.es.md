# Herencia multiplicativa, factores primitivos y novedad armónica

**Le Matt Ansatz Di Ego · Aritmética exacta en la familia declarada**

Una arquitectura multiplicativa permite distinguir repetir factores disponibles de ampliar su repertorio. Esta nota formaliza esa distinción y clasifica la familia $M_h=2^h-1$, $h\ge1$.

## 1. Repertorio y descomposición

Sean $\mathcal P_{<h}$ los primos que dividen algún $M_j$ con $1\le j<h$, y

$$\mathcal H_{<h}=\left\{\prod_{p\in\mathcal P_{<h}}p^{a_p}:a_p\in\mathbb N_0\right\}.$$

Por factorización única,

$$M_h=H_hN_h,\quad
H_h=\prod_{p\in\mathcal P_{<h}}p^{v_p(M_h)},\quad
N_h=\prod_{p\notin\mathcal P_{<h}}p^{v_p(M_h)}.$$

Se tiene $\gcd(H_h,N_h)=1$ y

$$\boxed{N_h=1\iff M_h\in\mathcal H_{<h}}.$$

En efecto, pertenecer al monoide equivale a usar sólo factores del repertorio previo. Las valuaciones $\mathbf v(z)=(v_p(z))_p$ satisfacen $\mathbf v(ab)=\mathbf v(a)+\mathbf v(b)$: un primo nuevo añade una coordenada, una potencia mayor modifica una coordenada existente.

## 2. Clasificación completa

Para $h>1$, un divisor primo $p$ de $2^h-1$ es nuevo exactamente cuando $\operatorname{ord}_p(2)=h$. El orden es el primer exponente positivo para el que $p\mid2^h-1$.

Además,

$$H_h=1\iff h\text{ es primo}.$$

Si $h$ es primo, el orden de cualquier divisor primo divide $h$ y no puede ser uno, por lo que es $h$. Si $h$ es compuesto, un divisor propio $1<d<h$ cumple $2^d-1\mid2^h-1$ y aporta un factor heredado.

Para decidir si hay un factor nuevo usamos el teorema clásico de Bang–Zsigmondy: la sucesión tiene un divisor primitivo después del sexto término. El enunciado y su atribución aparecen en [Min Sha, §1.1](https://arxiv.org/pdf/2005.01940). Los índices 2–6 se comprueban directamente.

| Índice | Clase | Condición |
|---|---|---|
| $h=1$ | Neutra | $H_h=N_h=1$ |
| $h$ primo | Novedad pura | $H_h=1,\ N_h>1$ |
| $h=6$ | Repetición pura | $H_h=63,\ N_h=1$ |
| $h$ compuesto, $h\ne6$ | Mixta | $H_h>1,\ N_h>1$ |

Así $M_4=15=3\cdot5$ es el primer caso mixto; $M_8=255$ tiene $H_8=15$, $N_8=17$. Novedad pura significa que todos los factores son nuevos: por ejemplo $M_{11}=23\cdot89$ pertenece a esa clase aunque sea compuesto.

La clasificación es un corolario de aritmética clásica expresado en el vocabulario del programa. Su aplicación propuesta es distinguir herencia y expansión de repertorio.

## 3. Un puente informacional explícito

En $X=\mathbb N_{>0}$, fije un repertorio finito $P$ y la firma $\Phi_P(z)=(v_p(z))_{p\in P}$. Para $r\notin P$, la pregunta $d_r(z)=v_r(z)$ no factoriza por $\Phi_P$: $z$ y $zr$ tienen igual firma y respuestas distintas.

Este ejemplo realiza el [criterio de novedad](closure_information.es.md) mediante valuaciones. Para usarlo en el dominio restringido $\{2^h-1\}$ hay que verificar allí los testigos y el contrato. Registrar sólo soporte primo o registrar también multiplicidades produce interfaces diferentes.

## 4. Del repertorio a un ritmo

La imagen de engranajes describe aquí generadores multiplicativos. Para períodos enteros, el retorno conjunto usa el mínimo común múltiplo y conserva exponentes. Para frecuencias, la conmensurabilidad usa razones racionales. Ambas nociones deben especificarse cuando se construye una realización dinámica.

Si $M$ representa una razón cuadrática $\omega_1^2/\omega_2^2$, la razón de frecuencias es $\sqrt M$. Una realización debe comprobar su propia sincronización y construir el mapa a [modos dinámicos](novelty_incorporation_and_dynamical_modes.es.md).

Un mapa definido $\omega(M)>0$, junto con $\ell(M)=v_*/\omega(M)$, parametriza una familia a lo sumo numerable de escalas. Para obtener un conjunto discreto de radios hacen falta condiciones adicionales de separación o aislamiento de su imagen. Para obtener estabilidad hace falta una dinámica y un criterio de persistencia.

## 5. Valor y revisión

El criterio mixto proporciona un candidato de herencia más novedad; la clasificación muestra exactamente cuántos tipos de índices admite. La siguiente tarea es construir una comparación acreditada a partir de esas firmas y estudiar si cambia la respuesta, el espectro o la interfaz.

Los controles finitos están en [las pruebas aritméticas](../tests/test_action_and_harmonic_structure.py). La clasificación general depende del teorema citado, no de extrapolar esos controles.

Procedencia: desarrollo de factores armónicos primitivos y su integración ontológica aportados por el autor. [Ontología del programa](../01_foundations/ontology_of_difference_and_closure.es.md).

[CONDICIONAL] Aquí $h$ es profundidad aritmética; no es $q$, $b$, $o_J$ ni $d_R$. Adoptar $r_V=2^{-q}$ ya produce $r_m/r_V=2^q-1$; la aparición de Mersenne no es evidencia independiente del supuesto. Esta herramienta no es un selector físico demostrado. El costo diofántico $\kappa_\varepsilon$ mencionado en la revisión canónica se conserva como línea exploratoria: en las fuentes textuales inspeccionadas no se localizó una definición operativa verificable, por lo que no se inventa una fórmula ni un resultado.
