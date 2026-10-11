# Qubit Stories — Multilingual Quantum Learning Lab

[English](docs/en/README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [Português (Portugal)](docs/pt-PT/README.md) | [Español](docs/es/README.md)

An illustrated learning series connects storytelling to eight runnable Qiskit experiments. There are four full videos of approximately 9min30s and 64 independent narrated chapters: 16 per language variant. The visuals and chapter transitions are aligned. Brazilian and European Portuguese have distinct scripts and voices; these are separate language variants. The original three YouTube sources remain linked as references.

| | Full videos | Chapters |
|---|---|---|
| English | [The Forest of Qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/en/the-forest-of-qubits.mp4) | [16](media/chapters/en/README.md) |
| Português (Brasil) | [A floresta dos qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt/a-floresta-dos-qubits.mp4) | [16](media/chapters/pt/README.md) |
| Español | [El bosque de los cúbits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/es/el-bosque-de-los-cubits.mp4) | [16](media/chapters/es/README.md) |
| Português (Portugal) | [A floresta dos qubits — Portugal](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4) | [16](media/chapters/pt-PT/README.md) |

Watch the relevant chapter, write a prediction, run the circuit and explain the results. Compare ideal probabilities with sampled counts. Change the relative phase to 0°, 90° or 180° and compare measurements before and after a final Hadamard. Compare Bell correlations in Z and X and investigate recovery from one controlled X error. Predictions are temporary and no learner data is collected. Educational benefits have not been measured in a user study.

## Run on Qollab

1. Create a project using **Upload your own files** and upload `qollab-runtime.zip`. Keep the runtime files at the project root; do not upload the MP4 videos to Qollab.
2. Press **Run** and choose a free simulator. Qollab supplies `backend`; no account credentials are included in the project.
3. Choose a language, open a matching chapter and write a prediction before revealing the result.
4. Adjust phase, shots or logical input and run again. All eight circuits are transpiled and submitted in one backend job per run, following Qollab's IonQ constraint.

`index.html` and `main.js` select the JS/Qiskit interface; JavaScript calls Python via the documented `callPromising` bridge. This interface needs the Qollab runtime. For the Python-only alternative, use `main.py`, `quantum.py` and `requirements.txt` without `index.html` or `main.js`; Qollab calls `main()` automatically.

[Download the Qollab package](qollab-runtime.zip)

## Run locally and validate

Python 3.10+ and Qiskit 2.x are required. Local execution uses Qiskit's free `BasicSimulator`. The three local tests cover phase/interference, coherent single-X recovery at every physical-qubit position and a single job with count totals. Qollab and IonQ execution have not yet been verified.

```sh
python -m pip install -r requirements.txt
python main.py
python -m unittest discover -s tests -v
```

## Scientific scope

- Characters and the forest are visual metaphors; a qubit is a quantum state, not a glowing ball.
- Amplitudes and relative phase distinguish superposition from classical ignorance. Measurements return one outcome; distributions require repeated preparations.
- Correlations in one basis alone do not prove entanglement. The Bell preparation and X/Z comparison highlight coherence; this is not a loophole-free Bell test. Entanglement does not enable faster-than-light messages.
- The three-qubit repetition example recovers one injected X error. It does not correct arbitrary noise, phase errors or two bit flips, and does not demonstrate fault tolerance. The recovered logical qubit is q0, the rightmost bit in Qiskit strings; the others hold syndrome information.
- Exact ideal probabilities differ from sampled backend counts. No real-hardware execution, quantum advantage or measured learning improvement is claimed.
- The circuits do not model superconducting cooling, trapped-ion lasers, molecular simulation or sensors discussed in the stories.

## Accessibility

Videos include synthetic narration, burned-in subtitles and editable ASS/SRT captions. Text scripts accompany the media. The lab provides keyboard controls, visible focus, labelled inputs, text result tables and live status. Playback is optional; no flashing or forced autoplay is used. Interface labels are in English and Portuguese, while videos and documentation cover all four language variants. A completed WCAG audit is not claimed.

## Sources, authorship and license

MIT covers the software and documentation. The original YouTube stories remain the property of their rights holders; public links do not grant redistribution rights. Their authorship, dates and tools remain unconfirmed. New scripts, translations, diagrams and production were prepared with Codex assistance on October 11, 2026. Generated artwork and synthetic narration are disclosed in the production notes. Keep the original English MIT license as the authoritative license text; these explanations do not replace it.

- [The World of Qubits — English](https://youtu.be/EAcDVqTb0lk)
- [O Mundo dos Qubits — pt-BR](https://youtu.be/nkQpc2YPSCA)
- [The Fellowship Of The Qubit — English](https://youtu.be/uPTSfysNvgw)

## Submission status

GitHub publication of the learning materials is complete. Qollab import, free-simulator and IonQ checks, MIT publication and final hackathon submission remain pending. A separate public 2–3 minute demonstration must show the runnable lab; the long educational videos do not replace it.

## Documentation

- [README](docs/en/README.md)
- [Project Card](docs/en/QOLLAB_PROJECT_CARD.md)
- [Setup guide](docs/en/QOLLAB_SETUP.md)
- [Checklist](docs/en/SUBMISSION_CHECKLIST.md)
- [Provenance](docs/en/PROVENANCE.md)
- [Production notes](docs/en/PRODUCTION_NOTES.md)
- [Deliverables](docs/en/DELIVERABLES.md)

- [Qollab — hackathon](https://qollab.xyz/programs/hackathon/terms#submissions)
- [Qollab — Python/Qiskit](https://qollab.xyz/learn/docs/python-qiskit-projects)
- [Qollab — runtime](https://qollab.xyz/learn/docs/runtime-environment)
- [Qollab — project page](https://qollab.xyz/learn/docs/write-your-project-page)
- [IBM Quantum — repetition codes](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes)


---

[English](docs/en/README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [Português (Portugal)](docs/pt-PT/README.md) | [Español](docs/es/README.md)

This effort is supported by Qollab & IonQ
