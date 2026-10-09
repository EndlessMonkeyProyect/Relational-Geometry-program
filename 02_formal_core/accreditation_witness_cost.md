# Acreditación de cierre y costo

[DEFINICIÓN] Se distinguen tres niveles:

1. **Cierre semántico:** existe una solución o referencia común bajo el contrato.
2. **Cierre acreditado:** hay testigos disponibles y aceptados por el verificador declarado de cómo las referencias entran al cierre.
3. **Cierre físicamente realizado:** un sistema medido realiza además las operaciones y el mapa físico propuestos.

Una identidad $I_\alpha=R^{-1}(\alpha)$ no necesita esperar a la acreditación para estar definida. Acreditar justifica su uso como referencia en una arquitectura concreta.

[DEFINICIÓN] Para una familia de referencias $S$, un candidato común $j$ y un sistema de verificación $\mathcal V$, sea $W_{\mathcal V}(S,j)$ el conjunto de certificados admisibles de las inclusiones y obligaciones del contrato. Si se acredita que $j$ es el join, su propiedad least debe figurar entre esas obligaciones; probar sólo que es cota superior no basta.

Fijados el cierre objetivo, la codificación y el modelo de costo, escribimos

$$\kappa(S)=\inf_{w\in W_{\mathcal V}(S,j)} C_{\mathcal V}(S,j,w),\qquad \inf\varnothing=+\infty.$$

El costo total declara construcción, acoplamiento/composición, almacenamiento, verificación y lectura de testigos. Una convención que mida sólo longitud o sólo verificación debe nombrarse como tal. Cambiar verificador o codificación puede cambiar $\kappa$.

[CONDICIONAL] Realizar el costo óptimo exige demostrar que el ínfimo se alcanza y proporcionar un método para encontrarlo. Existencia de certificado, verificación y búsqueda eficiente son obligaciones distintas. La disponibilidad de certificados y la independencia semántica se evalúan por separado.

[DEFINICIÓN] El residuo de acreditación registra obligaciones aún sin testigo aceptado; no se identifica con el residuo semántico verdadero. El costo de acoplamiento incluye la información conjunta que las interfaces aisladas no deciden.

[CONDICIONAL] En la rama computacional, $PSR^{acr}$ pregunta si existe una arquitectura derivable de costo acotado que resuelva la consulta $Q$; su versión constructiva exige encontrarla. La pertenencia de una versión de decisión a NP requiere certificados de longitud polinómica en la entrada y verificación polinómica, incluida la condición de parada. La codificación de la cota de costo importa.

[ABIERTO] Referencias → join → testigos → costo → control uniforme es una arquitectura de preguntas. Las cotas algorítmicas, de coercividad o multiescala son obligaciones distintas en cada [rama](../04_results/OPEN_PROBLEMS.md).

Procedencia: MF-63B, auditoría adversarial y continuidad de P vs NP, §§8–11, 23–24; [recierre exacto](compatible_reclosure.es.md).
