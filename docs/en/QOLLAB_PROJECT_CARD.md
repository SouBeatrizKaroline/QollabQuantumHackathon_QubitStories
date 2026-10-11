# Qubit Stories — Multilingual Quantum Learning Lab

## Short description (220/240)

Four illustrated videos and 64 chapters in English, Spanish, Brazilian Portuguese and European Portuguese, linked to eight Qiskit experiments. Watch, predict, run and explain superposition, interference and entanglement.

## Theme

Quantum Unlocked

## What it does

An illustrated learning series connects storytelling to eight runnable Qiskit experiments. There are four full videos of approximately 9min30s and 64 independent narrated chapters: 16 per language variant. The visuals and chapter transitions are aligned. Brazilian and European Portuguese have distinct scripts and voices; these are separate language variants. The original three YouTube sources remain linked as references.

Watch the relevant chapter, write a prediction, run the circuit and explain the results. Compare ideal probabilities with sampled counts. Change the relative phase to 0°, 90° or 180° and compare measurements before and after a final Hadamard. Compare Bell correlations in Z and X and investigate recovery from one controlled X error. Predictions are temporary and no learner data is collected. Educational benefits have not been measured in a user study.

## Problem and contribution

Quantum concepts can be hard to understand from words alone. This project combines a consistent illustrated narrative, four language variants, direct chapter links, predictions and contrasting executable experiments. It makes phase visible through interference, compares correlations across bases and connects an engineering explanation to controlled bit-flip recovery. No measured educational improvement is claimed.

## Learning videos

| | Full videos | Chapters |
|---|---|---|
| English | [The Forest of Qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/en/the-forest-of-qubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/en/README.md) |
| Português (Brasil) | [A floresta dos qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt/a-floresta-dos-qubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/pt/README.md) |
| Español | [El bosque de los cúbits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/es/el-bosque-de-los-cubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/es/README.md) |
| Português (Portugal) | [A floresta dos qubits — Portugal](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/pt-PT/README.md) |

## How to run

1. Create a project using **Upload your own files** and upload `qollab-runtime.zip`. Keep the runtime files at the project root; do not upload the MP4 videos to Qollab.
2. Press **Run** and choose a free simulator. Qollab supplies `backend`; no account credentials are included in the project.
3. Choose a language, open a matching chapter and write a prediction before revealing the result.
4. Adjust phase, shots or logical input and run again. All eight circuits are transpiled and submitted in one backend job per run, following Qollab's IonQ constraint.

`index.html` and `main.js` select the JS/Qiskit interface; JavaScript calls Python via the documented `callPromising` bridge. This interface needs the Qollab runtime. For the Python-only alternative, use `main.py`, `quantum.py` and `requirements.txt` without `index.html` or `main.js`; Qollab calls `main()` automatically.

## Scientific limits

The repetition example corrects one injected X error, not arbitrary noise. The illustrations are metaphors. Exact probabilities are distinguished from sampled counts. No quantum advantage, fault tolerance or hardware result is claimed.

## Accessibility

Videos include synthetic narration, burned-in subtitles and editable ASS/SRT captions. Text scripts accompany the media. The lab provides keyboard controls, visible focus, labelled inputs, text result tables and live status. Playback is optional; no flashing or forced autoplay is used. Interface labels are in English and Portuguese, while videos and documentation cover all four language variants. A completed WCAG audit is not claimed.

## Source, license and originality

MIT covers the software and documentation. The original YouTube stories remain the property of their rights holders; public links do not grant redistribution rights. Their authorship, dates and tools remain unconfirmed. New scripts, translations, diagrams and production were prepared with Codex assistance on October 11, 2026. Generated artwork and synthetic narration are disclosed in the production notes. Keep the original English MIT license as the authoritative license text; these explanations do not replace it.

[Git repository](https://github.com/SouBeatrizKaroline/qubit-stories)

## Demo and publication status

GitHub publication of the learning materials is complete. Qollab import, free-simulator and IonQ checks, MIT publication and final hackathon submission remain pending. A separate public 2–3 minute demonstration must show the runnable lab; the long educational videos do not replace it.

---

[English](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/en/README.md) | [Português (Brasil)](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/pt-BR/README.md) | [Português (Portugal)](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/pt-PT/README.md) | [Español](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/es/README.md)

This effort is supported by Qollab & IonQ
