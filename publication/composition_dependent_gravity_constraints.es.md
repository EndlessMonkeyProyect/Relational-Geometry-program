# Gravedad dependiente de la composición: cotas condicionales

**Le Matt Ansatz Di Ego · Correspondencia observable para un modelo de carga**

La [rama gravitatoria](gravity.es.md) puede contrastar una carga efectiva
$m_i f_i$ mediante aceleraciones de cuerpos con composiciones distintas.
Esta nota especifica un contrato cuantitativo para ese contraste.

## Observable diferencial

Suponga que dos cuerpos de prueba A y B, en el mismo campo y régimen, tienen
aceleraciones proporcionales a factores positivos $f_A,f_B$. El valor absoluto
del parámetro diferencial es

$$|\eta_{AB}|=\frac{2|f_A-f_B|}{f_A+f_B}.$$

La comparación es invariante bajo una multiplicación común de ambos factores.
Por ello se fija una normalización común $f_0$ y se escribe, para un descriptor
de composición X y un único coeficiente activo,

$$f_i=f_0(1+\epsilon X_i),\qquad
|\eta_{AB}|=\frac{|\epsilon\Delta X|}{|1+\epsilon\bar X|},$$

con $\Delta X=X_A-X_B$ y $\bar X=(X_A+X_B)/2$. Para
$|\epsilon X_i|\ll1$, se obtiene $|\eta_{AB}|\simeq|\epsilon\Delta X|$.

## Contraste con MICROSCOPE

El resultado final de MICROSCOPE para sus aleaciones de titanio y platino es

$$\eta({\rm Ti,Pt})=[-1.5\pm2.3\ ({\rm estad.})\pm1.5\ ({\rm sist.})]\,10^{-15}.$$

[Fuente primaria: Touboul et al., 2022](https://arxiv.org/abs/2209.15487).

Como convención de comparación, combinar ambas incertidumbres en cuadratura y
usar $|\eta_{\rm central}|+2\sigma_{\rm tot}$ da aproximadamente
$7.0\,10^{-15}$. No se presenta esa convención como una nueva evaluación
estadística de los datos de la misión.

Para el modelo lineal de un parámetro, la región admisible aproximada es

$$|\epsilon|\lesssim\frac{7.0\,10^{-15}}{|\Delta X|},\qquad\Delta X\ne0.$$

Por ejemplo, estimando X como número de neutrones por masa atómica en unidades u,
con isótopos dominantes y fracciones de masa Pt/Rh de 90/10 y Ti/Al/V de 90/6/4,
se obtiene $\Delta X\simeq0.0553$, y por tanto
$|\epsilon|\lesssim1.3\,10^{-13}$. Es una estimación de orden de magnitud
condicionada a esa representación de composición, no una medición directa de
una carga gravitatoria individual del protón o neutrón.

## Hipótesis y aplicación al programa

El contraste supone aditividad de las cargas efectivas, respuesta en el mismo
campo, validez del régimen lineal y ausencia de mecanismos adicionales que
modifiquen esa respuesta. Las abundancias isotópicas y energías de ligadura
deben incorporarse si se necesita mayor precisión.

Con varios coeficientes, la misma comparación controla aproximadamente
$|\sum_j\epsilon_j\Delta X_j|$; determinar parámetros separados exige más
composiciones o hipótesis. La normalización $f_0$ se fija con el resto del modelo
y su calibración. La elección convencional $f_0=1$ no es una medición absoluta
de una función universal f mediante esta sola comparación.

El aporte es un criterio operativo para evaluar diccionarios de la rama:
declarar cómo los estados relacionales determinan X, calcular las aceleraciones
y contrastar la diferencia bajo las mismas condiciones experimentales.

Las [pruebas de correspondencias físicas](../tests/test_physical_correspondence_contracts.py)
controlan la fórmula exacta, su aproximación y la aritmética de la cota. No
constituyen una nueva medición ni una validación de una dinámica gravitatoria.
