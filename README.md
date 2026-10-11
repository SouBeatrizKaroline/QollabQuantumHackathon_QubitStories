# Qubit Stories — Watch, Predict, Run, Explain

**Three animated quantum stories, connected to eight runnable Qiskit experiments.**

Qubit Stories addresses an educational gap: an animation can make an unfamiliar idea approachable, but learners also need to test what the story says. Here, every experiment points back to an exact scene in the supplied videos. Learners watch, write a prediction, reveal simulated results and explain the connection. English and Portuguese introductions reach different audiences; the fantasy story extends the pathway toward engineering and error correction.

**Hackathon theme:** Quantum Unlocked. **License:** MIT for the software and repository documentation.

This effort is supported by Qollab & IonQ

## Illustrated chapters in three languages

The expanded educational series is available as **48 individual videos**, with 16 chapters in each language. Every chapter includes narration and burned-in subtitles.

- [Português brasileiro](media/chapters/pt/README.md)
- [English](media/chapters/en/README.md)
- [Español latinoamericano](media/chapters/es/README.md)

See the [complete chapter index](media/chapters/README.md) for direct MP4 links and editable captions. These files extend the learning materials; the original public videos remain below.

## The three videos

| Story | Audience / language | Link |
|---|---|---|
| The World of Qubits | Young explorers, English; Cuby introduces the concepts | [Watch](https://youtu.be/EAcDVqTb0lk) |
| O Mundo dos Qubits | Young explorers, Portuguese; Kubi introduces the concepts | [Assistir](https://youtu.be/nkQpc2YPSCA) |
| The Fellowship Of The Qubit | Fantasy framing, English; concepts, hardware, noise and error correction | [Watch](https://youtu.be/uPTSfysNvgw) |

The repository contains links, not downloaded copies of the videos. Video playback uses YouTube; quantum experiments do not depend on YouTube availability. External video and third-party media rights remain with their respective rights holders. The MIT license does not assert ownership of music, voices, assets or other third-party material appearing in linked videos.

## From scene to experiment

| Concept | English introduction | Portuguese introduction | Fellowship | Runnable experiment |
|---|---|---|---|---|
| Bit versus qubit | 0:20 | 0:15 | 0:12 | Definite zero versus H-prepared superposition |
| Preparation and measurement | 0:48–1:34 | 0:38–1:19 | 0:12–0:20 | Repeated preparations give a frequency distribution |
| Interference | 1:37 | 1:21 | 0:24 | Compare H–P(phase) with H–P(phase)–H |
| Entanglement | 1:57 | 1:38 | 0:40 | Bell measurements in Z and X bases |
| Noise and logical qubits | Not covered | Not covered | 1:10–1:25 | Inject one X error; compare unprotected and encoded recovery |

Timestamps were checked against auto-generated captions; slight offsets may occur. The executable activities extend the video explanations; the videos do not show the specific circuits implemented here.

## Run on Qollab — visual experience

1. Create a project with **Upload your own files**. Upload `index.html`, `main.js`, `main.css`, `quantum.py` and `requirements.txt` at the project root. A ZIP containing these files is supplied separately.
2. The top-level `index.html` and `main.js` select Qollab's JS/Qiskit runtime. `main.js` calls Python through Qollab's documented `callPromising` bridge.
3. Press **Run** and select a **free simulator**. Qollab supplies `backend`; there are no credentials in this repository.
4. Choose a video. Write a prediction before opening an experiment's results.
5. Compare phase 0°, 90° and 180°. Z measurements remain 50/50, while the interference experiment changes. Encode zero or one to test bit-flip recovery.
6. All eight circuits are transpiled and submitted as **one backend job per run**, following Qollab's IonQ limit. Exact ideal probabilities are labelled separately from observed backend counts.

The Python-only alternative uses `main.py`, `quantum.py` and `requirements.txt`, **without** `index.html` or `main.js`. Qollab automatically calls `main()` and displays phase, shots and logical-one inputs. Do not add a second call to `main()` in the Qollab editor.

## Run locally

Requires Python 3.10+ and Qiskit 2.x:

```sh
python -m pip install -r requirements.txt
python main.py
python -m unittest discover -s tests -v
```

Local `main.py` uses Qiskit's free `BasicSimulator`. The visual interface relies on Qollab's module bridge and is not a standalone HTML app. It should be imported into Qollab, not opened directly from disk.

## Educational contribution beyond a starter circuit

The contribution is a bilingual, timestamp-linked **watch → predict → run → explain** pathway, rather than an isolated Bell-state tutorial. Two experiments expose phase invisible in Z but visible after H. Bell correlations are compared across two measurement bases. A simplified three-qubit recovery activity connects a specific engineering claim in the third video to an executable circuit. Prediction fields are temporary and do not collect learner data.

These are proposed educational benefits, not measured learning outcomes. No user study or quantum advantage benchmark is claimed.

## Scientific scope and limitations

- A qubit is a quantum state, not a literal glowing ball. Characters and landscapes are visual metaphors.
- Measurements return one classical result; frequencies estimate probabilities across new preparations.
- Correlated Z outcomes alone do not establish entanglement. The Bell state is known from its preparation; the X comparison highlights coherence. This is not a loophole-free Bell test.
- Entanglement does not enable faster-than-light messaging.
- The repetition example encodes a single qubit into three physical qubits and coherently recovers one injected **X** error. It does not correct arbitrary noise, phase errors or two bit flips, and it is not a fault-tolerant implementation.
- Other output bits in the recovery experiment are syndrome ancillas. The logical output is q0, displayed on the **right** of Qiskit bitstrings.
- Exact probabilities assume ideal operations. Backend shot counts may fluctuate or reflect a simulator noise model. No real hardware result is claimed.
- The circuits do not model superconducting cooling, trapped-ion lasers, molecular simulation or quantum sensors mentioned in the third video.

## Accessibility

Keyboard-operable controls, visible focus, labelled inputs, semantic headings, tables with text outcomes and live status are included. Information does not rely only on colour. No flashing or forced autoplay is used. English/Portuguese labels accompany navigation; scientific explanations are in English. Review and correct video captions before final submission; auto-generated captions can misrecognize “qubit”. No claim of a completed WCAG audit is made.

## Hackathon submission

See [QOLLAB_PROJECT_CARD.md](QOLLAB_PROJECT_CARD.md) for copy-ready project text and [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md) for remaining platform steps. Creating this Git repository does **not** publish a runnable Qollab project or submit an entry. Registration, publication and submission must be completed in the participant's Qollab account.

See [PROVENANCE.md](PROVENANCE.md) for what is known and what the author still needs to disclose. Video creation dates and production tools have not yet been confirmed.

## Sources

- [Qollab submission rules and themes](https://qollab.xyz/programs/hackathon/terms#submissions)
- [Qollab Python/Qiskit projects](https://qollab.xyz/learn/docs/python-qiskit-projects)
- [Qollab runtime and Python/JS bridge](https://qollab.xyz/learn/docs/runtime-environment)
- [Qollab project documentation](https://qollab.xyz/learn/docs/write-your-project-page)

## Reuse

Fork the MIT-licensed software and documentation to add your own story and aligned experiments. Preserve attribution, identify new contributions and disclose any pre-existing material. Links to external videos do not provide a redistribution license for their media.
