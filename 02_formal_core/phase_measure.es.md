# Dos coordenadas de fase, dieciséis firmas y medida invariante

## Representación de segundo orden

Considere dos firmas de fase, cada una en $\mathbb Z_4$, y el soporte

$$K=\mathbb Z_4\times\mathbb Z_4.$$

Los avances separados $g_A(a,b)=(a+1,b)$ y $g_B(a,b)=(a,b+1)$ conmutan y tienen orden cuatro. Para cada $(a_0,b_0)$ y cada $(a,b)\in K$ existe un único par $(i,j)\in\{0,1,2,3\}^2$ tal que $(a,b)=g_A^ig_B^j(a_0,b_0)$. La órbita contiene exactamente dieciséis firmas.

El resultado establece una representación coherente con dos fases independientes. En un dominio realizable $E$, una firma heredada $\Phi:E\to K_A$ y una nueva fase $d:E\to\mathbb Z_4$ completan el producto exactamente cuando

$$d(\Phi^{-1}(a))=\mathbb Z_4\quad\text{para todo }a\in K_A.$$

Esta condición de accesibilidad identifica la hipótesis que debe comprobar una realización. Una operación que conserve $\Phi$ y avance $d$ en una unidad es suficiente para satisfacerla. La capacidad de identificación del producto completo es $\log_2 16=4$ bits.

## Medida determinada por localidad y simetría

Sea $A=\mathbb C^K$, con multiplicación puntual. Sea $B$ una forma hermítica positiva definida, antilineal en su primera entrada. Impóngase compatibilidad con las preguntas multiplicativas:

$$B(fg,h)=B(f,\overline g\,h).$$

La conjugación hace que esta condición sea compatible con la convención hermítica compleja. Para los indicadores reales $e_x$ y $e_y$ de firmas distintas,

$$B(e_x,e_y)=B(e_x,e_xe_y)=0.$$

Por tanto, con $w_x=B(e_x,e_x)>0$,

$$B(f,h)=\sum_{x\in K}w_x\overline{f(x)}h(x).$$

Si $B$ es invariante bajo las traslaciones de ambas fases, la acción transitiva sobre $K$ obliga a que todos los $w_x$ sean iguales. Al normalizar $B(1,1)=1$ se obtiene

$$w_x=\frac1{16},\qquad \mu(\{x\})=\frac1{16},\qquad \mu(K\setminus\{x\})=\frac{15}{16}.$$

La razón $1:15$ es así un resultado de medida de firmas bajo las hipótesis indicadas. La [realización física de tasas](../publication/physical_bridges.es.md) especifica los pasos adicionales para interpretarla como una fracción cuadrática física.

## Realización de las fases en un dominio finito

Un control exhaustivo explora cuatro capas de fase con dos microestados por capa. Cada capa admite 16 matrices booleanas de transición $2\times2$, para un total de $16^4=65\,536$ grafos.

| Propiedad comprobada | Número de grafos |
|---|---:|
| Cada microestado tiene al menos una salida hacia la fase siguiente | 6 561 |
| Cada capa admite una transición biyectiva | 2 401 |
| Pueden elegirse biyecciones cuya composición tras cuatro capas es la identidad | 1 753 |

El control muestra cómo verificar tres requisitos de realización en un universo finito completamente enumerado. Sus conteos describen ese dominio de prueba. Se reproducen en [tests/test_relational_core.py](../tests/test_relational_core.py).

## Valor y revisión

La contribución reúne estructura de fase, accesibilidad, capacidad de identificación y medida en una cadena explícita. La revisión puede comprobar la demostración, comparar su formulación con construcciones existentes y estudiar dominios donde las acciones independientes tengan significado operacional.

Procedencia: edición pública fuente 2.0.0, secciones de cierre de segundo orden, medida e implementación de fases; *Núcleo integrado*, §§18–23. Esta edición explicita la conjugación en la compatibilidad hermítica. [Revisión R3](../REVIEW.md).

## Límite generativo y físico

[CONDICIONAL] El producto completo se supone o se acredita mediante acciones independientes en un dominio. Codificar sus 16 estados en cuatro bits no deriva cuatro discriminantes del núcleo ontológico. **$b=4$ permanece abierto.** [PUENTE FÍSICO] Seleccionar $q=4$ exige un mapa independiente del orden $o_J=4$ y del peso formal $1/16$. Véase [notación y requisito binario](binary_refinement.md).
