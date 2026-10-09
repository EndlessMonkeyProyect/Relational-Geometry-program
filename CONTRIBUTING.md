# Contribuir al programa

**For international contributors:** English and Spanish contributions are welcome. Start from a focused question in [REVIEW](REVIEW.md), provide reproducible evidence, and submit an Issue or pull request with the result and its scope.

Las contribuciones pueden ampliar una demostración, mejorar una explicación, reproducir un cálculo o desarrollar una nueva realización. La unidad de trabajo preferida es un resultado revisable: una pregunta, los supuestos necesarios y una respuesta que otra persona pueda comprobar.

## Preparar un aporte

1. Elija un punto **R1–R13**, o una obligación de la auditoría canónica, de [REVIEW](REVIEW.md) e identifique el archivo y la sección afectados. Puede abrir un Issue para presentar el trabajo o entregar directamente un cambio pequeño mediante pull request.
2. Explique qué aporta el resultado: qué permite calcular, distinguir, componer o medir. Declare las hipótesis junto al enunciado y conecte la conclusión con la evidencia disponible.
3. Incluya el desarrollo suficiente para revisarlo. Una demostración identifica su dominio y sus casos límite; un experimento registra entradas, parámetros, método y procedencia de datos; una implementación declara su contrato y el costo que evalúa.
4. Resuma el resultado obtenido y la siguiente pregunta que habilita. Cite las fuentes utilizadas y preserve la atribución de las contribuciones anteriores.

La comunicación pública parte del aporte positivo y precisa su alcance: identidad exacta, realización bajo hipótesis, observación numérica o propuesta de investigación. Las notas de exploración interna se conservan en `internal/`; las páginas públicas desarrollan los resultados disponibles y las preguntas que permiten extenderlos. Los archivos públicos se seleccionan de forma explícita en la herramienta de distribución.

## Reproducir y comprobar

Desde la raíz del repositorio, en un entorno Python de trabajo:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python tools/public_release.py
```

La suite comprueba las identidades y los controles implementados. El chequeo de distribución valida el manifiesto y los destinos locales de los enlaces Markdown. Una modificación de archivos públicos cambia sus hashes; la actualización del manifiesto forma parte de la preparación de una nueva distribución.

Para un aporte numérico, añada al pull request el comando específico usado, los parámetros, las versiones relevantes y una síntesis de los resultados. En Navier–Stokes, los presupuestos independientes y la sensibilidad a derivadas o resolución forman parte del entregable cuando sustentan la conclusión.

## Entregar un Issue o pull request

Use un título concreto, por ejemplo: `R4: cota de tamaño para una cápsula contador`. El texto debe permitir que un revisor encuentre el enunciado, reproduzca la evidencia y entienda qué cambia. Para código, incluya los controles pertinentes al comportamiento añadido. Para una corrección editorial, compruebe las fórmulas, las referencias y los enlaces afectados.

Los Issues del repositorio son el canal de revisión y coordinación. La integración de un aporte conserva su autoría y el alcance de lo revisado; el reconocimiento público se acuerda con la persona que contribuye.

## Preparar una distribución — mantenimiento

Una vez integrados los cambios públicos y completadas sus comprobaciones:

```bash
python tools/public_release.py --write-manifest --build
python tools/public_release.py
```

El primer comando actualiza `MANIFEST.json` y genera `dist/relational_geometry_program_public.zip` a partir de la selección pública. El segundo comprueba que el manifiesto y los enlaces corresponden a los archivos actuales. La generación del ZIP produce un artefacto local; su publicación se realiza como una acción posterior de mantenimiento.

## Mantenimiento canónico

Aplicar [STATUS_CANONICAL](STATUS_CANONICAL.md) y la [leyenda](00_orientation/EPISTEMIC_LEGEND.md). La presentación pública desarrolla los aportes junto con sus hipótesis, evidencia y cuestiones abiertas. El registro NO-GO, el archivo histórico y las auditorías de desarrollo se conservan en el área interna, excluidos tanto del paquete como de los nuevos commits publicados. Publicar requiere una solicitud explícita.
