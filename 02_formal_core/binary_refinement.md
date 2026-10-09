# Refinamiento binario y los distintos «cuatro»

[DEFINICIÓN] Una primera diferencia binaria $d_1:U\to\{0,1\}$ exige ambos valores en su imagen. Cada nuevo discriminante $d_{k+1}$ añade una coordenada independiente sólo si realiza ambos valores en **cada** fibra de la firma previa:

$$\operatorname{Im}(d_1,\ldots,d_{k+1})
=\operatorname{Im}(d_1,\ldots,d_k)\times\{0,1\}.$$

[DERIVADO] Por inducción, $b$ discriminantes que satisfacen este requisito producen $2^b$ firmas. Es una implicación; no construye los discriminantes que faltan.

[CONDICIONAL] Una involución que preserve la firma previa y cambie el nuevo bit garantiza accesibilidad de ambos valores por fibra no vacía. Ésta es una condición suficiente para la segunda diferencia independiente; su existencia debe acreditarse en el dominio pertinente.

[ABIERTO] El corpus acredita una primera diferencia binaria y una segunda independiente condicional. **$b=4$ no está derivado:** no se han acreditado cuatro discriminantes del núcleo generativo con imagen $\{0,1\}^4$. Recodificar un producto de 16 estados ya supuesto mediante cuatro bits no llena esa obligación.

| Objeto | Símbolo | Lo que no implica |
|---|---|---|
| Diferencias binarias independientes | $b$ | No se fija por el orden de un operador |
| Fracción cuadrática $r_V=2^{-q}$ | $q$ | No cuenta discriminantes sin un puente adicional |
| Razón de amplitudes $2^{-n_{\rm amp}}$ | $n_{\rm amp}$ | No es el exponente cuadrático: $q=2n_{\rm amp}$ |
| Profundidad de $2^h-1$ | $h$ | No selecciona automáticamente una escala física |
| Orden de $J$ | $o_J$ | $o_J=4$ no implica $b=4$ |
| Dimensión real de representación | $d_R$ | El plano rotatorio tiene $d_R=2$ aunque $o_J=4$ |

[DERIVADO] Si se adopta $r_V=2^{-q}$ y $r_m=1-r_V$, entonces $r_m=(2^q-1)/2^q$ y $r_m/r_V=2^q-1$. El número de Mersenne aparece por construcción; no verifica de forma independiente el supuesto binario.

[CONDICIONAL] $n_{\rm amp}=2$ y $q=4$ representan la misma razón $\omega_V/\omega_U=1/4$. La medida de [16 firmas](phase_measure.es.md) y la [aritmética](harmonic_inheritance_and_novelty.es.md) permanecen como realizaciones matemáticas. Sus identificaciones físicas se examinan en los [puentes](../publication/physical_bridges.es.md).
