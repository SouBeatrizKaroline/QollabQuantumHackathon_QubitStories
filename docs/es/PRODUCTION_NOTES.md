# Notas de producción

Una serie educativa ilustrada conecta historias con ocho experimentos ejecutables en Qiskit. Hay cuatro videos completos de aproximadamente 9min30s y 64 capítulos independientes narrados: 16 por variante lingüística. Las imágenes y las transiciones de los capítulos están alineadas. Las versiones en portugués de Brasil y de Portugal tienen guiones y voces propios. Los tres videos originales de YouTube siguen disponibles como referencias.

## Contenido y formato

La referencia muestra a una niña y una mascota luminosa en un bosque nocturno. Se generó una nueva ilustración para este proyecto. La edición combina esa imagen, movimiento de cámara, tarjetas explicativas, diagramas y subtítulos. La narración es sintética y no hay sincronización labial. Las versiones mantienen la secuencia de capítulos y aproximadamente 9min30s; la adaptación de Portugal usa vocabulario, construcciones y voz europeos.

## Herramientas y formato

Guiones, traducciones, diagramas y edición: asistencia de Codex. Ilustración: generación integrada de imágenes. Voz: edge-tts con las voces de la tabla. Composición: Pillow y FFmpeg. Salida: 1280 × 720, 24 fotogramas por segundo, video H.264 y audio AAC. Los tiempos de palabras del servicio de voz guían los subtítulos; los archivos ASS/SRT permiten edición. La velocidad de narración se ajusta por capítulo para alinear transiciones. Los nuevos videos están en GitHub y no se han subido a YouTube. El capítulo 15 de las tres versiones anteriores cita las historias originales; la adaptación portuguesa más reciente presenta las cuatro variantes lingüísticas.

| Locale | Voice |
|---|---|
| en-US | en-US-AriaNeural |
| es-MX | es-MX-DaliaNeural |
| pt-BR | pt-BR-FranciscaNeural |
| pt-PT | pt-PT-RaquelNeural |

## Prompt original de la ilustración

```text
Use case: illustration-story. Asset type: cinematic illustrated educational video background. Create a polished wide 16:9 landscape illustration, highest practical resolution. A whimsical bioluminescent forest at night, glowing violet mushrooms, teal trees, fireflies, an old stone path that leads to a tiny observatory under stars. On the far RIGHT third stand a curious young girl with medium brown skin, curly dark hair in two puffs, yellow T-shirt, denim overalls, pink shoes and a small green backpack; beside her floats a friendly round pale cyan luminous mascot with expressive eyes and tiny arms. Original stylized 3D children's animation aesthetic, coherent anatomy, soft cinematic lighting, expressive but calm, charming, detailed. Left half should have dark calm uncluttered space and atmosphere for explanatory diagrams placed later in editing. No typography, no logos, no symbols, no visible writing, no mathematical graphics. Do not depict magic as literal science. One continuous environment, no collage or panels. Keep girl and mascot entirely inside frame with space above and below.
```

## Verificación y límites

Las verificaciones locales abarcan número de capítulos, duración, audio decodificable y comportamiento de Qiskit. Se inspeccionan vistas previas del diseño. La serie distingue superposición de desconocimiento clásico, fase de probabilidades y correlación de comunicación. La recuperación de errores se limita al modelo declarado de un error X. No afirmamos traducción perfecta, certificación completa de accesibilidad, ejecución en hardware real ni tolerancia a fallos.

La publicación de los materiales educativos en GitHub está completada. Quedan pendientes la importación en Qollab, las pruebas en simuladores gratuitos e IonQ, la publicación bajo MIT y el envío al hackathon. Una demostración pública separada de 2–3 minutos debe mostrar el laboratorio ejecutable; los videos educativos largos no la sustituyen.

- [Qollab — hackathon](https://qollab.xyz/programs/hackathon/terms#submissions)
- [Qollab — Python/Qiskit](https://qollab.xyz/learn/docs/python-qiskit-projects)
- [Qollab — runtime](https://qollab.xyz/learn/docs/runtime-environment)
- [Qollab — project page](https://qollab.xyz/learn/docs/write-your-project-page)
- [IBM Quantum — repetition codes](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes)


---

[English](../../docs/en/README.md) | [Português (Brasil)](../../docs/pt-BR/README.md) | [Português (Portugal)](../../docs/pt-PT/README.md) | [Español](../../docs/es/README.md)

This effort is supported by Qollab & IonQ
