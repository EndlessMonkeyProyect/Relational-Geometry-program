# Programa de Geometría Relacional

**Cierre contextual, resolución y composición**

Le Matt Ansatz Di Ego · [English](README.md) · **v3.0.0-review · 9 de octubre de 2026**

¿Qué información debe conservar un sistema para seguir siendo reconocible y componerse con otros? El programa desarrolla esta pregunta mediante interfaces suficientes, geometría de la comparación y modelos reproducibles. La v3 conecta la resolución respecto de una referencia con pesos calculables, ejemplos cuánticos y el costo de realizar un cierre.

## Aportes centrales

- **Interfaces contextuales y recierre:** una clase conserva las respuestas de todas las continuaciones admitidas; la congruencia permite componer clases y las fibras cuantifican distinciones residuales.
- **Resolución y peso:** en un contrato finito explícito, $r_{\rm ref}=2^{-\mathcal R}$ conecta autocoincidencia, proyección, diferencias de una red y composición independiente.
- **Composición de espines:** probabilidades de espín total, correlaciones del singlete y quiralidad ternaria proporcionan ejemplos exactos en mecánica cuántica estándar.
- **Representación y costo:** la caracterización del cociente contextual SAT y la anchura de tablas separan semántica, canonización y recursos.
- **Dinámica y escala:** comparadores locales, acción, dinámica de cocientes y cotas de control uniforme conectan descripciones individuales y colectivas.
- **Laboratorios y observables:** fluidos, teoría gauge, química y crecimiento aportan controles reproducibles; las notas de protón y gravedad fijan correspondencias y condiciones de contraste.

[Qué incorpora la v3](publication/UPDATE_3_0.md) · [Resultados y evidencia](04_results/RESULTS_REGISTER.md)

## Ruta de lectura

1. [Lenguaje canónico y notación](01_foundations/canonical_relational_language.es.md).
2. [Recierre contextual y recursos](02_formal_core/contextual_reclosure_and_resource_cost.es.md).
3. [Resolución y pesos](02_formal_core/resolution_and_modal_weights.es.md).
4. [Espines e información relacional](publication/spin_composition_and_relational_information.es.md).
5. [SAT y costo de representación](05_computation/contextual_sat_and_representation_cost.es.md).
6. [Puentes físicos](publication/physical_bridges.es.md), [laboratorios](07_emergence_laboratory/README.md) y [estado por rama](STATUS_CANONICAL.md).

La ontología organiza la investigación; los teoremas declaran sus hipótesis y las aplicaciones físicas declaran sus observables. «Singularidad relacional» significa una diferencia cerrada reutilizable como unidad, no una singularidad de una PDE ni un agujero negro. Los resultados de esta edición no anuncian una solución propia de P vs NP, Yang–Mills o regularidad global de fluidos.

## Reproducir y revisar

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
python tools/canonical_audit.py
python tools/public_release.py
~~~

El [informe de reproducción](04_results/REPRODUCTION_REPORT.md) identifica las verificaciones ejecutadas y los datos de producción suministrados. La revisión está abierta en español o inglés: elegí una [pregunta concreta](REVIEW.md) y compartí una prueba, reproducción o extensión con alcance explícito.

Autoría y cita: [CITATION.cff](CITATION.cff). Condiciones de uso: [NOTICE.md](NOTICE.md). Archivo del programa: [versiones en Zenodo](https://doi.org/10.5281/zenodo.23123167). Para citar un resultado, identificá su versión y el DOI específico del depósito correspondiente.
