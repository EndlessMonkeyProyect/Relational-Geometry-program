# Radio protónico: hipótesis de correspondencia y contraste

**Le Matt Ansatz Di Ego · Fórmula condicional y antecedentes explícitos**

Esta nota convierte una relación de escalas del programa en una hipótesis física
precisa. Separa el cálculo de la selección del modelo y de la identificación del
observable. Complementa los [puentes de tasas y longitudes](physical_bridges.es.md).

## Contrato de la correspondencia

Sean $\omega_U,\omega_V>0$ y adopte las siguientes hipótesis:

1. **Partición:** $r_V^{\rm freq}=\omega_V^2/\omega_U^2=1/16$.
2. **Escala total-Compton:** $\omega_U=m_pc^2/\hbar$.
3. **Longitud:** $R_V=c/\omega_V$.
4. **Observable candidato:** identificar $R_V$ con el radio rms de carga del protón.

Las tres primeras implican exactamente

$$R_V=\frac{4\hbar}{m_pc}=4\bar\lambda_p\simeq0.841236\ {\rm fm}.$$

**Prueba.** La primera da $\omega_V=\omega_U/4$; sustituir las otras dos da la
expresión. La cuarta hipótesis convierte esa longitud en una predicción para
un observable electromagnético, y por eso exige una justificación física propia.

La [resolución respecto de una referencia](../02_formal_core/resolution_and_modal_weights.es.md)
aporta realizaciones matemáticas de pesos. Relacionar uno de esos pesos con
$r_V^{\rm freq}$ requiere un mapa de estados y observables. La elección de 16
alternativas, su preparación y su significado para el protón deben fijarse
independientemente del radio que se pretende explicar.

## Antecedente y dato de comparación

La relación numérica ya aparece en **Trinhammer y Bohr (2019)**, quienes proponen
$\pi r_p=2\lambda_C$, equivalente a $r_p=4\hbar/(m_pc)$, dentro de su modelo.
El desarrollo relacional reconoce ese antecedente. Su tarea propia es construir
y comprobar el diccionario que conecta cierre, frecuencia y respuesta de carga.
[Artículo y resumen primarios](https://orbit.dtu.dk/en/publications/on-proton-charge-radius-definition/).

CODATA 2022 recomienda $r_p=0.84075(64)$ fm. La diferencia entre la fórmula y ese
valor central es aproximadamente $0.76$ veces la incertidumbre indicada para el
dato. Es una comparación con datos conocidos, no una confirmación prospectiva
ni una determinación de los supuestos del modelo.
[CODATA 2022, tabla XVI, NIST](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958143).

## Próximo contraste

Un protocolo prospectivo debe declarar antes de nuevos datos:

- el espacio interno, el criterio de selección y la correspondencia de frecuencias;
- el observable electromagnético, distinguiendo radio de carga, magnético y otras longitudes;
- las constantes y sus incertidumbres, la incertidumbre del modelo y la regla de comparación;
- una versión con fecha verificable y predicciones adicionales sin reajustar el diccionario.

Esta edición publica la hipótesis y sus condiciones; no declara un prerregistro
externo. El cálculo se controla en
[pruebas de correspondencias físicas](../tests/test_physical_correspondence_contracts.py).
