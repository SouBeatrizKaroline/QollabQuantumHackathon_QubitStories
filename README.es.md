# Qubit Stories — Laboratorio multilingüe de aprendizaje cuántico

[English](docs/en/README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [Português (Portugal)](docs/pt-PT/README.md) | [Español](docs/es/README.md)

Una serie educativa ilustrada conecta historias con ocho experimentos ejecutables en Qiskit. Hay cuatro videos completos de aproximadamente 9min30s y 64 capítulos independientes narrados: 16 por variante lingüística. Las imágenes y las transiciones de los capítulos están alineadas. Las versiones en portugués de Brasil y de Portugal tienen guiones y voces propios. Los tres videos originales de YouTube siguen disponibles como referencias.

| | Videos completos | Capítulos |
|---|---|---|
| English | [The Forest of Qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/en/the-forest-of-qubits.mp4) | [16](media/chapters/en/README.md) |
| Português (Brasil) | [A floresta dos qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt/a-floresta-dos-qubits.mp4) | [16](media/chapters/pt/README.md) |
| Español | [El bosque de los cúbits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/es/el-bosque-de-los-cubits.mp4) | [16](media/chapters/es/README.md) |
| Português (Portugal) | [A floresta dos qubits — Portugal](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4) | [16](media/chapters/pt-PT/README.md) |

Mira el capítulo correspondiente, escribe una predicción, ejecuta el circuito y explica el resultado. Compara probabilidades ideales con conteos muestreados. Cambia la fase relativa a 0°, 90° o 180° y compara mediciones antes y después de una Hadamard final. Compara correlaciones de Bell en las bases Z y X y explora la recuperación de un error X controlado. Las predicciones son temporales y no recopilamos datos del alumnado. Los beneficios educativos todavía no se han medido en un estudio con participantes.

## Ejecutar en Qollab

1. Crea un proyecto con **Upload your own files** y carga `qollab-runtime.zip`. Mantén los archivos de ejecución en la raíz; no cargues los videos MP4 en Qollab.
2. Pulsa **Run** y elige un simulador gratuito. Qollab proporciona `backend`; el proyecto no incluye credenciales de cuenta.
3. Elige el idioma, abre un capítulo correspondiente y escribe una predicción antes de revelar el resultado.
4. Ajusta la fase, el número de mediciones o la entrada lógica y ejecuta de nuevo. Los ocho circuitos se compilan y envían en un único trabajo por ejecución, respetando la restricción de IonQ en Qollab.

`index.html` y `main.js` seleccionan la interfaz JS/Qiskit; JavaScript llama a Python mediante el puente documentado `callPromising`. Esta interfaz requiere el entorno Qollab. Para la alternativa solo en Python, usa `main.py`, `quantum.py` y `requirements.txt`, sin `index.html` ni `main.js`; Qollab llama a `main()` automáticamente.

[Descargar el paquete Qollab](qollab-runtime.zip)

## Ejecutar localmente y verificar

Se requiere Python 3.10+ y Qiskit 2.x. La ejecución local utiliza el `BasicSimulator` gratuito de Qiskit. Las tres pruebas verifican fase/interferencia, recuperación coherente de un error X en cada posición y envío de un único trabajo con los totales de conteos. La ejecución en Qollab y en IonQ aún no se ha verificado.

```sh
python -m pip install -r requirements.txt
python main.py
python -m unittest discover -s tests -v
```

## Alcance científico

- Los personajes y el bosque son metáforas visuales; un cúbit es un estado cuántico, no una esfera luminosa.
- Las amplitudes y la fase relativa distinguen la superposición del desconocimiento clásico. Cada medición da un resultado; las distribuciones requieren nuevas preparaciones.
- Las correlaciones en una sola base no prueban entrelazamiento. La preparación de Bell y la comparación X/Z destacan la coherencia; no es una prueba de Bell libre de lagunas. El entrelazamiento no permite mensajes más rápidos que la luz.
- El código de repetición de tres cúbits recupera un error X introducido. No corrige ruido arbitrario, errores de fase ni dos errores de bit, y no demuestra tolerancia a fallos. El cúbit lógico recuperado es q0, el bit de la derecha en las cadenas de Qiskit; los demás guardan información del síndrome.
- Las probabilidades ideales exactas difieren de los conteos del simulador. No afirmamos ejecución en hardware real, ventaja cuántica ni una mejora medida del aprendizaje.
- Los circuitos no modelan enfriamiento de superconductores, láseres de iones atrapados, simulación molecular ni sensores mencionados en las historias.

## Accesibilidad

Los videos incluyen narración sintética, subtítulos incrustados y archivos ASS/SRT editables. Los guiones acompañan los materiales. El laboratorio dispone de controles por teclado, foco visible, campos identificados, tablas textuales de resultados y avisos de estado. Ver los videos es opcional; no hay destellos ni reproducción automática forzada. La interfaz tiene etiquetas en inglés y portugués; los videos y documentos abarcan las cuatro variantes. No afirmamos haber completado una auditoría WCAG.

## Fuentes, autoría y licencia

La licencia MIT cubre el software y la documentación. Los videos originales de YouTube pertenecen a sus titulares; los enlaces públicos no otorgan derechos de redistribución. Su autoría, fechas y herramientas todavía no se han confirmado. Los nuevos guiones, traducciones, diagramas y producción se prepararon con asistencia de Codex el 11 de octubre de 2026. Las notas de producción declaran la generación de imágenes y las voces sintéticas. El texto original en inglés de la licencia MIT sigue siendo el texto oficial; estas explicaciones no lo sustituyen.

- [The World of Qubits — English](https://youtu.be/EAcDVqTb0lk)
- [O Mundo dos Qubits — pt-BR](https://youtu.be/nkQpc2YPSCA)
- [The Fellowship Of The Qubit — English](https://youtu.be/uPTSfysNvgw)

## Estado de la entrega

La publicación de los materiales educativos en GitHub está completada. Quedan pendientes la importación en Qollab, las pruebas en simuladores gratuitos e IonQ, la publicación bajo MIT y el envío al hackathon. Una demostración pública separada de 2–3 minutos debe mostrar el laboratorio ejecutable; los videos educativos largos no la sustituyen.

## Documentación

- [README](docs/es/README.md)
- [Project Card](docs/es/QOLLAB_PROJECT_CARD.md)
- [Guía de configuración](docs/es/QOLLAB_SETUP.md)
- [Lista de preparación](docs/es/SUBMISSION_CHECKLIST.md)
- [Procedencia y autoría](docs/es/PROVENANCE.md)
- [Notas de producción](docs/es/PRODUCTION_NOTES.md)
- [Entregables](docs/es/DELIVERABLES.md)

- [Qollab — hackathon](https://qollab.xyz/programs/hackathon/terms#submissions)
- [Qollab — Python/Qiskit](https://qollab.xyz/learn/docs/python-qiskit-projects)
- [Qollab — runtime](https://qollab.xyz/learn/docs/runtime-environment)
- [Qollab — project page](https://qollab.xyz/learn/docs/write-your-project-page)
- [IBM Quantum — repetition codes](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes)


---

[English](docs/en/README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [Português (Portugal)](docs/pt-PT/README.md) | [Español](docs/es/README.md)

This effort is supported by Qollab & IonQ
