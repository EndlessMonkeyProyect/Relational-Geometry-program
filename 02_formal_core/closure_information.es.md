# Información, cápsulas y cierre suficiente

## Contrato y firma

Sea $\Omega$ un conjunto de realizaciones, $\mathcal Q$ una familia de preguntas y $\mathcal G$ una familia de contextos admisibles. Se agrupan dos realizaciones cuando dan la misma respuesta a todas las preguntas en todos los contextos:

$$x\sim y\quad\Longleftrightarrow\quad q(gx)=q(gy)\quad\text{para todo }q\in\mathcal Q,\ g\in\mathcal G.$$

Una **cápsula** es una clase de esta equivalencia. La firma $\Phi:\Omega\to K=\Omega/{\sim}$ conserva exactamente las distinciones del contrato. Toda pregunta del contrato factoriza por $\Phi$, porque es constante en sus fibras. Este es el sentido operacional de descripción suficiente.

La construcción aporta una definición de cierre relativa a preguntas explícitas. Para el mismo contrato, volver a tomar el cociente por las mismas respuestas deja una estructura canónicamente equivalente: $\mathrm{Cl}(\mathrm{Cl}(\Omega))\cong\mathrm{Cl}(\Omega)$.

## Criterio exacto de nueva información

Sea $d:\Omega\to D$ una comparación adicional. La firma refinada es $(\Phi,d)$ y su imagen es

$$K^+=(\Phi,d)(\Omega)\subseteq K\times D.$$

**Proposición.** $d$ aporta una distinción nueva si y sólo si no existe $f:K\to D$ tal que $d=f\circ\Phi$.

**Demostración.** Si existe $f$, dos estados con la misma firma tienen el mismo valor de $d$. Recíprocamente, si $d$ es constante en cada fibra no vacía de $\Phi$, se define $f(a)$ como ese valor común. La definición es independiente del representante y produce la factorización. Por tanto, la falta de factorización equivale a la existencia de $x,y$ con $\Phi(x)=\Phi(y)$ y $d(x)\ne d(y)$.

Para particiones finitas, el refinamiento se escribe $\Pi^+=\Pi\vee\Pi(d)$. Su ganancia de capacidad de identificación es

$$\Delta b=\log_2\frac{|\Pi^+|}{|\Pi|}.$$

Se trata de capacidad combinatoria. Una interpretación probabilística utiliza además una distribución explícita sobre las clases.

## Fronteras que permiten composición

Para una relación de restricciones $R\subseteq A^{I\cup B}$, con interior $I$ y frontera $B$, la interfaz $\pi_B R$ conserva qué asignaciones de frontera admiten al menos un interior compatible. Si el entorno sólo accede a $B$, esta interfaz basta para decidir la compatibilidad con cualquier restricción externa sobre $B$.

La igualdad de interfaces caracteriza la indistinguibilidad cuando la familia de preguntas externas separa las asignaciones de frontera; por ejemplo, cuando permite preguntar por cada asignación concreta. La [prueba de composición](compatible_reclosure.es.md) desarrolla esta propiedad y su recierre.

## Alcance y revisión

El resultado es un criterio semántico exacto. Una implementación especifica cómo representa las firmas y qué certificados o cálculos permiten decidir la factorización. Ese costo constituye una pregunta propia de la [rama computacional](../05_computation/README.md).

Procedencia: *Núcleo integrado del Programa de Geometría Relacional*, §§7–10; *Hilo canónico de cierre, localidad y escala relacional*, secciones de firmas y fronteras; edición pública fuente 2.0.0. [Revisión R1](../REVIEW.md).
