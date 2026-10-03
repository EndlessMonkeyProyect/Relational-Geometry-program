# Control gaussiano de comparaciones por bloques

Este control permite reproducir una pregunta de escala en un modelo lineal: cuánto de la variación global de un observable puede registrarse mediante cambios locales por bloques. Compara el operador de campo libre con variantes masivas sobre el mismo toro discreto de cuatro dimensiones.

## Modelo y objeto calculado

Sea $d$ el operador discreto de enlaces a plaquetas y

$$Q=d^\top d+m^2I.$$

Para $m^2=0$, la covarianza $Q^+$ se interpreta en el cociente por el núcleo, o mediante el límite regularizado para los observables que anulan ese núcleo. Así se especifica el sentido de la expresión gaussiana en presencia de modos gauge.

Se fija un observable lineal del campo de fuerza $f(A)=\langle\phi,dA\rangle=\langle c,A\rangle$, con $c=d^\top\phi$, donde $\phi$ es $\cos(2\pi x_0/L)$ en las plaquetas $(0,1)$ y cero en las restantes. El código evalúa

$$\operatorname{Var}(f)=c^\top Q^+c,\qquad
\mathcal D_\ell[f]=\sum_B c_B^\top(Q_{BB})^+c_B,\qquad
R=\frac{\operatorname{Var}(f)}{\mathcal D_\ell[f]}.$$

Los bloques contienen enlaces con ambos extremos dentro de cubos de lado $\ell$, cuyos orígenes se separan $\ell/2$. El programa verifica la invariancia por traslación de una matriz local representativa y la compatibilidad del observable con el núcleo local cuando éste está presente.

La constante óptima de una desigualdad de varianza para todos los observables es al menos el cociente de cualquier observable admisible. Por eso $R$ ofrece un diagnóstico concreto para esta función de prueba. Una cota uniforme para la constante óptima requiere, además, un argumento válido para toda la clase de funciones.

## Reproducción rápida

```bash
python -m pip install -r requirements.txt
python 06_yang_mills/scripts/gaussian_control.py --quick
python 06_yang_mills/scripts/gaussian_control.py --quick --json
```

Resultados verificados el 3 de octubre de 2026, con $\ell=2$:

| $L$ | $m^2$ | Varianza | $R=\operatorname{Var}/\mathcal D_\ell$ |
|---:|---:|---:|---:|
| 4 | 0 | 128.000000 | 0.218750000 |
| 4 | 0.5 | 102.400000 | 0.201923077 |
| 4 | 0.1 | 121.904762 | 0.214773614 |
| 6 | 0 | 648.000000 | 0.403846154 |
| 6 | 0.5 | 432.000000 | 0.312500000 |
| 6 | 0.1 | 589.090909 | 0.378960055 |

La ejecución utilizó Python 3.12, NumPy 2.5.3 y SciPy 1.18.1. Las identidades son de matrices finitas; sus valores se calculan en punto flotante, con tolerancia CG relativa $10^{-12}$ y umbral espectral local relativo $10^{-9}$. La tabla verifica estos seis casos. Las conclusiones asintóticas exigen estudiar la dependencia con $L$ y justificar las estimaciones correspondientes.

## Exploración ampliada

```bash
python 06_yang_mills/scripts/gaussian_control.py --full
```

El barrido ampliado conserva los tamaños del código fuente: $\ell=2$ con $L=4,6,8,10,12,16,20$ y $\ell=4$ con $L=8,12,16,20$. Usa más memoria y tiempo; esta edición verificó el protocolo rápido.

La comparación gaussiana es un laboratorio para seleccionar y evaluar formas relacionales. La transferencia al problema gauge no abeliano, a la dinámica física y al límite continuo tiene sus propias condiciones, descritas en la [rama Yang–Mills](README.md).

Procedencia: adaptación de *control_gaussiano_U1_bloques.py*, suministrado con los materiales del programa. La adaptación agrega validación de parámetros, ejecución rápida y salida JSON, conservando el cálculo matricial.
