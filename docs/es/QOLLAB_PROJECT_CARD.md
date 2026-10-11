# Qubit Stories — Laboratorio multilingüe de aprendizaje cuántico

## Descripción breve (214/240)

Cuatro videos ilustrados y 64 capítulos en inglés, español, portugués de Brasil y de Portugal, vinculados a ocho experimentos Qiskit. Mira, predice, ejecuta y explica superposición, interferencia y entrelazamiento.

## Tema

Quantum Unlocked

## Qué hace

Una serie educativa ilustrada conecta historias con ocho experimentos ejecutables en Qiskit. Hay cuatro videos completos de aproximadamente 9min30s y 64 capítulos independientes narrados: 16 por variante lingüística. Las imágenes y las transiciones de los capítulos están alineadas. Las versiones en portugués de Brasil y de Portugal tienen guiones y voces propios. Los tres videos originales de YouTube siguen disponibles como referencias.

Mira el capítulo correspondiente, escribe una predicción, ejecuta el circuito y explica el resultado. Compara probabilidades ideales con conteos muestreados. Cambia la fase relativa a 0°, 90° o 180° y compara mediciones antes y después de una Hadamard final. Compara correlaciones de Bell en las bases Z y X y explora la recuperación de un error X controlado. Las predicciones son temporales y no recopilamos datos del alumnado. Los beneficios educativos todavía no se han medido en un estudio con participantes.

## Problema y aportación

Los conceptos cuánticos pueden ser difíciles de comprender solo con palabras. El proyecto combina una historia ilustrada coherente, cuatro variantes lingüísticas, enlaces directos a capítulos, predicciones y experimentos ejecutables que permiten comparaciones. Hace visible la fase mediante interferencia, compara correlaciones entre bases y relaciona una explicación de ingeniería con la recuperación de un error de bit controlado. No afirmamos una mejora educativa medida.

## Videos educativos

| | Videos completos | Capítulos |
|---|---|---|
| English | [The Forest of Qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/en/the-forest-of-qubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/en/README.md) |
| Português (Brasil) | [A floresta dos qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt/a-floresta-dos-qubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/pt/README.md) |
| Español | [El bosque de los cúbits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/es/el-bosque-de-los-cubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/es/README.md) |
| Português (Portugal) | [A floresta dos qubits — Portugal](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/pt-PT/README.md) |

## Cómo ejecutar

1. Crea un proyecto con **Upload your own files** y carga `qollab-runtime.zip`. Mantén los archivos de ejecución en la raíz; no cargues los videos MP4 en Qollab.
2. Pulsa **Run** y elige un simulador gratuito. Qollab proporciona `backend`; el proyecto no incluye credenciales de cuenta.
3. Elige el idioma, abre un capítulo correspondiente y escribe una predicción antes de revelar el resultado.
4. Ajusta la fase, el número de mediciones o la entrada lógica y ejecuta de nuevo. Los ocho circuitos se compilan y envían en un único trabajo por ejecución, respetando la restricción de IonQ en Qollab.

`index.html` y `main.js` seleccionan la interfaz JS/Qiskit; JavaScript llama a Python mediante el puente documentado `callPromising`. Esta interfaz requiere el entorno Qollab. Para la alternativa solo en Python, usa `main.py`, `quantum.py` y `requirements.txt`, sin `index.html` ni `main.js`; Qollab llama a `main()` automáticamente.

## Límites científicos

El ejemplo de repetición corrige un error X introducido, no cualquier ruido. Las ilustraciones son metáforas. Las probabilidades exactas se distinguen de los conteos muestreados. No afirmamos ventaja cuántica, tolerancia a fallos ni resultados de hardware.

## Accesibilidad

Los videos incluyen narración sintética, subtítulos incrustados y archivos ASS/SRT editables. Los guiones acompañan los materiales. El laboratorio dispone de controles por teclado, foco visible, campos identificados, tablas textuales de resultados y avisos de estado. Ver los videos es opcional; no hay destellos ni reproducción automática forzada. La interfaz tiene etiquetas en inglés y portugués; los videos y documentos abarcan las cuatro variantes. No afirmamos haber completado una auditoría WCAG.

## Código, licencia y originalidad

La licencia MIT cubre el software y la documentación. Los videos originales de YouTube pertenecen a sus titulares; los enlaces públicos no otorgan derechos de redistribución. Su autoría, fechas y herramientas todavía no se han confirmado. Los nuevos guiones, traducciones, diagramas y producción se prepararon con asistencia de Codex el 11 de octubre de 2026. Las notas de producción declaran la generación de imágenes y las voces sintéticas. El texto original en inglés de la licencia MIT sigue siendo el texto oficial; estas explicaciones no lo sustituyen.

[Git repository](https://github.com/SouBeatrizKaroline/qubit-stories)

## Demostración y publicación

La publicación de los materiales educativos en GitHub está completada. Quedan pendientes la importación en Qollab, las pruebas en simuladores gratuitos e IonQ, la publicación bajo MIT y el envío al hackathon. Una demostración pública separada de 2–3 minutos debe mostrar el laboratorio ejecutable; los videos educativos largos no la sustituyen.

---

[English](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/en/README.md) | [Português (Brasil)](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/pt-BR/README.md) | [Português (Portugal)](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/pt-PT/README.md) | [Español](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/es/README.md)

This effort is supported by Qollab & IonQ
