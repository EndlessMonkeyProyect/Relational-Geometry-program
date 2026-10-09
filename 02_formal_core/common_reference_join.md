# Referencia común: preorden, cociente y join

[DEFINICIÓN] Sea $x\preceq y$ «$y$ extiende la referencia $x$», con reflexividad y transitividad. Identifique $x\simeq y$ si $x\preceq y$ e $y\preceq x$. En el cociente, la relación inducida es un orden parcial. En esta nota $x,y$ denotan clases del cociente.

$$U(x,y)=\uparrow x\cap\uparrow y
=\{z:x\preceq z\text{ e }y\preceq z\}.$$

| Caso | Estatuto |
|---|---|
| $U(x,y)=\varnothing$ | [DEFINICIÓN] No hay extensión común admisible |
| $U(x,y)\ne\varnothing$ sin elemento least | [DEFINICIÓN] Hay rutas comunes; el cierre común permanece indefinido |
| Existe $j\in U(x,y)$ con $j\preceq z$ para todo $z\in U(x,y)$ | [DEFINICIÓN] $j=x\vee y$ es el least upper bound / join; cierre común resuelto |

[DERIVADO] El join es único: dos elementos least se preceden mutuamente y son iguales por antisimetría. Un elemento **minimal** sólo carece de otro estrictamente menor en $U(x,y)$; no tiene por qué preceder a todos.

Un control finito es el poset con $x,y\prec a,b$ y $a,b$ incomparables. Ambos son cotas superiores minimales; ninguno es least. Tampoco la existencia de rutas comunes garantiza una cota minimal en posets infinitos.

[CONDICIONAL] En particiones se elige aquí el orden «menos información $\preceq$ más información»; el join es el refinamiento común. En enteros positivos bajo divisibilidad es el LCM. Estas realizaciones no convierten LCM en una ley gravitacional. El `Join` relacional de restricciones conserva su definición operativa de conjunción compatible; no debe confundirse con un join abstracto sin declarar el orden.

[ABIERTO] Existencia de un join semántico no entrega un testigo computable, una cota de costo ni una realización física. Véase [acreditación](accreditation_witness_cost.md).

Procedencia: corpus local MF-0–MF-23, §§22–27, y corrección canónica del autor de octubre de 2026; inventario en [procedencia](../references/SOURCE_PROVENANCE.md).
