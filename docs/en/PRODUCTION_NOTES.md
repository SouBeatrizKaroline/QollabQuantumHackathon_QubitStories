# Production notes

An illustrated learning series connects storytelling to eight runnable Qiskit experiments. There are four full videos of approximately 9min30s and 64 independent narrated chapters: 16 per language variant. The visuals and chapter transitions are aligned. Brazilian and European Portuguese have distinct scripts and voices; these are separate language variants. The original three YouTube sources remain linked as references.

## Content and form

The supplied reference shows a girl and a luminous mascot in a night forest. A new illustration was generated for this project. The edit combines that illustration, camera movement, explanatory cards, diagrams and captions. Narration is synthetic and there is no lip synchronisation. All versions keep the same chapter sequence and approximately 9min30s duration; the Portuguese adaptation uses European vocabulary, phrasing and a Portugal voice.

## Tools and format

Scripts, translations, diagrams and editing: Codex assistance. Artwork: integrated image generation. Speech: edge-tts with the voices below. Composition: Pillow and FFmpeg. Output: 1280 × 720, 24 fps, H.264 video and AAC audio. Word timestamps from the speech service drive the captions; separate ASS/SRT files permit editing. Narration speed is adjusted per chapter to align transitions. New videos are hosted on GitHub, not uploaded to YouTube. Chapter 15 in the three earlier versions names the original source stories; the newer European Portuguese adaptation describes the four language variants.

| Locale | Voice |
|---|---|
| en-US | en-US-AriaNeural |
| es-MX | es-MX-DaliaNeural |
| pt-BR | pt-BR-FranciscaNeural |
| pt-PT | pt-PT-RaquelNeural |

## Original artwork prompt

```text
Use case: illustration-story. Asset type: cinematic illustrated educational video background. Create a polished wide 16:9 landscape illustration, highest practical resolution. A whimsical bioluminescent forest at night, glowing violet mushrooms, teal trees, fireflies, an old stone path that leads to a tiny observatory under stars. On the far RIGHT third stand a curious young girl with medium brown skin, curly dark hair in two puffs, yellow T-shirt, denim overalls, pink shoes and a small green backpack; beside her floats a friendly round pale cyan luminous mascot with expressive eyes and tiny arms. Original stylized 3D children's animation aesthetic, coherent anatomy, soft cinematic lighting, expressive but calm, charming, detailed. Left half should have dark calm uncluttered space and atmosphere for explanatory diagrams placed later in editing. No typography, no logos, no symbols, no visible writing, no mathematical graphics. Do not depict magic as literal science. One continuous environment, no collage or panels. Keep girl and mascot entirely inside frame with space above and below.
```

## Verification and limits

Local checks cover chapter counts, duration, decodable audio and Qiskit behaviour. Layout previews are visually inspected. The series distinguishes superposition from classical ignorance, phase from probabilities and correlation from communication. Error recovery is limited to the stated single-X model. No claim of flawless translation, complete accessibility certification, real hardware execution or fault tolerance is made.

GitHub publication of the learning materials is complete. Qollab import, free-simulator and IonQ checks, MIT publication and final hackathon submission remain pending. A separate public 2–3 minute demonstration must show the runnable lab; the long educational videos do not replace it.

- [Qollab — hackathon](https://qollab.xyz/programs/hackathon/terms#submissions)
- [Qollab — Python/Qiskit](https://qollab.xyz/learn/docs/python-qiskit-projects)
- [Qollab — runtime](https://qollab.xyz/learn/docs/runtime-environment)
- [Qollab — project page](https://qollab.xyz/learn/docs/write-your-project-page)
- [IBM Quantum — repetition codes](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes)


---

[English](../../docs/en/README.md) | [Português (Brasil)](../../docs/pt-BR/README.md) | [Português (Portugal)](../../docs/pt-PT/README.md) | [Español](../../docs/es/README.md)

This effort is supported by Qollab & IonQ
