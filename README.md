# Qubit Stories — Multilingual Quantum Learning Lab

### What if understanding a qubit began with a story—and continued with an experiment?

This effort is supported by Qollab & IonQ

**Team:** QuantGirls  
**Hackathon:** Qollab × IonQ Global Hackathon  
**Theme:** Quantum Unlocked

| Team member | Portfolio or professional profile |
| --- | --- |
| **Beatriz Karoline Cordeiro da Silva** | [Portfolio](https://soubeatrizkaroline.vercel.app/) |
| **Daiane Fonseca** | [LinkedIn](https://www.linkedin.com/in/daiane-fonseca-552655285) |
| **Sonia Janara Silva Barros** | [Portfolio](https://jhay.goskip.app/) |

**[Explore the source code](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories)** · **[Browse the learning materials](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/media/README.md)** · **[Download the Qollab runtime package](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/raw/refs/heads/main/qollab-runtime.zip)**

## What is Qubit Stories?

**Qubit Stories connects illustrated storytelling with runnable quantum experiments.**

A forest, characters and a luminous companion introduce ideas such as qubits, superposition, interference, entanglement and error correction. Learners then explore those ideas through real Qiskit circuit code.

The central learning loop is:

**Watch → predict → run → compare → explain.**

The project includes:

- **Four full illustrated videos**, approximately 9 minutes and 30 seconds each.
- **64 independently narrated chapters**, with 16 chapters per language variant.
- **Eight runnable Qiskit experiments**.
- Adjustable phase, measurement repetitions and logical input.
- Circuit diagrams, ideal probabilities and observed measurement counts.
- Narration, subtitles and accompanying text scripts.
- English, Brazilian Portuguese, European Portuguese and Spanish learning materials.

The Portuguese versions use distinct scripts and voices. The interactive interface currently combines English and Portuguese labels; the videos and documentation cover all four language variants.

## The problem and why it matters

Quantum concepts can be difficult to understand through definitions alone. Attractive metaphors can introduce a topic, but learners also need opportunities to test what those metaphors mean.

Qubit Stories connects narrative with contrasting experiments. Learners can predict a result, inspect a circuit, compare probabilities with sampled outcomes and explain what changed.

The project is intended for curious beginners, students, educators and people encountering quantum computing for the first time.

It encourages questions such as:

- Is superposition simply a hidden classical value?
- Can two states have identical measurement probabilities but different relative phases?
- How does interference make phase observable?
- What can correlated measurements tell us about a prepared Bell state?
- Which errors can a simple repetition code correct?

## Our contribution

The contribution is the integration of multilingual storytelling, direct chapter links, learner predictions and executable experiments into one learning sequence.

The project brings together established quantum concepts; it does not claim to have invented superposition, interference, Bell states or repetition codes.

For educators, it offers material for demonstrations and guided discussion. For partners and investors, a proposed next step is an educational pilot measuring usability, conceptual understanding and demand.

Learning improvement, commercial traction, revenue and market demand have not yet been demonstrated.

## Learning videos and chapters

Each language variant follows the same 16-chapter sequence, with aligned visual transitions.

| Language | Full learning video | Chapter collection |
| --- | --- | --- |
| **English** | [The Forest of Qubits](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/media/full/en/the-forest-of-qubits.mp4) | [16 chapters](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/media/chapters/en/README.md) |
| **Português — Brasil** | [A floresta dos qubits](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/media/full/pt/a-floresta-dos-qubits.mp4) | [16 chapters](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/media/chapters/pt/README.md) |
| **Español** | [El bosque de los cúbits](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/media/full/es/el-bosque-de-los-cubits.mp4) | [16 chapters](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/media/chapters/es/README.md) |
| **Português — Portugal** | [A floresta dos qubits — Portugal](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4) | [16 chapters](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/media/chapters/pt-PT/README.md) |

The experiments work independently of video playback. Learners can also use the accompanying scripts.

## How does the quantum part work?

The lab uses Qiskit to construct circuits and calculate their exact ideal probabilities. A selected backend then runs measured versions of those circuits, producing sampled counts.

These are separate outputs:

- **Ideal probabilities:** calculated from the circuit's statevector before measurement.
- **Observed counts:** returned by the backend after repeated circuit preparations and measurements.

Small differences between ideal probabilities and sampled frequencies are expected with a finite number of repetitions, called **shots**.

### The eight experiments

| Experiment | What learners investigate |
| --- | --- |
| **1. A definite zero** | A qubit prepared in state zero gives a definite result in the computational basis. |
| **2. Prepare, then measure** | A Hadamard gate prepares equal probabilities for zero and one. |
| **3. Phase hidden in Z** | Changing relative phase can leave computational-basis probabilities unchanged. |
| **4. Make phase visible** | A final Hadamard converts relative phase into different outcome probabilities. |
| **5. A shared state** | A prepared Bell state produces correlated outcomes in the Z basis. |
| **6. Change both measurement bases** | The same Bell preparation remains correlated when measured in X. |
| **7. One bit flip** | An intentionally applied X gate changes an unprotected logical bit. |
| **8. Three physical qubits** | A repetition-code example encodes, decodes and recovers from one controlled X error. |

### Phase and interference

The phase experiments compare:

```text
H → phase gate → measurement

H → phase gate → H → measurement
```

Without the final Hadamard, the Z-basis probabilities remain evenly split. With it:

```text
P(0) = cos²(phase / 2)
P(1) = sin²(phase / 2)
```

Try **0°, 90° and 180°** to observe deterministic zero, equal probabilities and deterministic one in the ideal interference circuit.

### Entanglement and correlations

The lab prepares a Bell state using Hadamard and controlled-NOT gates, then compares measurements in Z and X.

The comparison helps distinguish the coherent Bell preparation from a classical mixture that only reproduces Z-basis correlations. This demonstration is not a loophole-free Bell test, and entanglement does not enable faster-than-light messaging.

### Controlled error recovery

The repetition example protects against **one injected X error**. It does not correct arbitrary noise, phase errors or two bit flips.

The recovered logical qubit is **q0**, shown as the **rightmost bit** in Qiskit's output strings. The remaining qubits retain error-syndrome information.

This encoding is not the copying of an unknown quantum state. See the [IBM Quantum repetition-code lesson](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes) for the underlying distinction and limitations.

## How to run on Qollab

### Interactive lab

1. Download the repository's **qollab-runtime.zip**.
2. Create a project through Qollab's file-upload workflow.
3. Upload or import the runtime package, preserving its files at the project root.
4. Start the project and select an available permitted free simulator.
5. Open a story or matching chapter, write a prediction and reveal the corresponding experiment's results.
6. Change the phase, shots or logical input and run again.

Keep the large MP4 videos outside the Qollab runtime upload; the interface links to externally hosted media.

The interface uses `index.html`, `main.js`, `main.css` and `quantum.py`. JavaScript calls Python through the Qollab `callPromising` bridge.

**All eight circuits are transpiled and submitted through one backend job per run.** This is a batch of eight circuits, rather than one combined eight-qubit circuit.

### Python-only alternative

Use these files without the interactive `index.html` and `main.js`:

```text
main.py
quantum.py
requirements.txt
```

Include the license and documentation. Qollab supplies the selected `backend` and invokes `main()`.

Default Python parameters:

```text
shots = 512
phase_degrees = 0.0
logical_one = False
```

The console prints circuit diagrams, theoretical predictions, ideal probabilities, backend counts and explanations.

The interactive controls offer **128, 512 or 1024 shots** and phases of **0°, 90° or 180°**. The Python suite accepts shot counts from 32 to 4096.

Consult the [setup guide](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/en/QOLLAB_SETUP.md) and [Qollab runtime documentation](https://qollab.xyz/learn/docs/runtime-environment) for platform-specific setup.

## How to run locally

Download or clone the repository. From its root, use **Python 3.10 or newer**.

Create a virtual environment:

```sh
python -m venv .venv
```

Activate it.

**Windows:**

```text
.venv\Scripts\activate
```

**macOS/Linux:**

```sh
source .venv/bin/activate
```

Install the dependencies and run:

```sh
python -m pip install -r requirements.txt
python main.py
```

Local execution uses Qiskit's **BasicSimulator**. No quantum hardware credentials are required for this path.

The interactive web interface requires Qollab's runtime and Python bridge; opening `index.html` alone is not equivalent to running the lab.

### Verification

Run the repository's tests:

```sh
python -m unittest discover -s tests -v
```

The test suite covers:

- Phase remaining hidden in Z and becoming visible after a final Hadamard.
- Recovery of the logical state under individual controlled X errors.
- One backend job containing all eight experiments, with the expected count totals.

Local tests do not establish successful Qollab or IonQ execution.

## How to use the learning sequence

1. Choose a language and watch a relevant chapter, or read its script.
2. Write what you expect before inspecting the results.
3. Run the experiments or reveal their available outputs.
4. Compare ideal probabilities with observed frequencies.
5. Change one parameter and repeat.
6. Explain what changed and which concept accounts for it.

Prediction fields are temporary. Rerunning the interface rebuilds the experiment cards, so learners should copy any notes they want to retain.

## Accessibility

The learning materials include:

- Synthetic narration and burned-in subtitles.
- Editable ASS/SRT caption files and text scripts.
- Keyboard controls, visible focus and labelled inputs.
- Text circuit diagrams and result tables.
- Live execution-status messages.
- Optional video playback without forced autoplay.

The project does not claim a completed WCAG audit or flawless translation.

## Scope and limitations

Qubit Stories is an educational prototype.

- The forest and characters are metaphors; a qubit is a quantum state, not a glowing object.
- Repeated shots involve repeated preparations, rather than repeated measurements of one unchanged qubit.
- Correlations in a single basis alone do not establish entanglement.
- The X-error example is controlled, rather than a realistic hardware-noise model.
- The repetition example does not demonstrate full fault tolerance.
- Circuits do not simulate cooling systems, trapped-ion lasers, molecular applications or physical sensors mentioned in the stories.
- No quantum advantage, verified hardware execution or measured educational improvement is claimed.

## Credits and development transparency

The repository records the following production process:

| Contributor or tool | Recorded use |
| --- | --- |
| **QuantGirls** | Project integration and presentation of the multilingual learning experience. |
| **OpenAI Codex** | Assistance with the lab, scripts, translations, diagrams, production and documentation. |
| **Integrated image generation** | Creation of a new forest illustration for the project. |
| **edge-tts and synthetic Edge voices** | Narration for the four language variants. |
| **Pillow and FFmpeg** | Visual composition, camera movement, captions and video/audio processing. |
| **Qiskit** | Circuit construction, ideal-state calculations, transpilation and backend execution. |
| **Participant-supplied reference material** | Three YouTube story links and a short visual style reference. |

The new production uses illustrated scenes, camera movement, diagrams and captions. It is not continuous 3D character animation or lip-synchronised speech.

According to the repository's provenance record, new scripts, translations, diagrams, videos and documentation were prepared with Codex assistance on **11 October 2026**.

The provenance record states that no external tutorial code was copied. Standard Qiskit APIs and the documented Qollab bridge are used. Original source timings were informed by captions; full original transcripts and downloaded YouTube media are not redistributed.

Authorship, creation dates, production tools and media rights for the original reference stories remain unconfirmed. Any additional copied or adapted code, circuits, text, artwork or templates must be disclosed with their source, authorship, affected material and applicable license.

## References and external attribution

### Original story references

These three sources informed the research and narrative trail:

1. **The World of Qubits — English.** [YouTube reference](https://youtu.be/EAcDVqTb0lk).
2. **O Mundo dos Qubits — Brazilian Portuguese.** [YouTube reference](https://youtu.be/nkQpc2YPSCA).
3. **The Fellowship Of The Qubit — English.** [YouTube reference](https://youtu.be/uPTSfysNvgw).

The repository records the visible channel name **Aspirante Qualquer** for the first two sources. A channel name does not establish authorship or permission to reuse its material.

These original stories remain the property of their respective rights holders. Public links do not grant redistribution rights.

### Scientific and technical references

- **IBM Quantum Learning:** [Repetition codes](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes). Foundation for the educational bit-flip protection example and its limits.
- **Qiskit:** [Official documentation](https://quantum.cloud.ibm.com/docs/). Circuit construction, quantum-state calculations and execution APIs.
- **Qiskit Basic Provider:** [Official documentation](https://quantum.cloud.ibm.com/docs/en/api/qiskit/providers_basic_provider). Local simulator used by the Python entry point.
- **Qollab:** [Python/Qiskit projects](https://qollab.xyz/learn/docs/python-qiskit-projects), [runtime environment](https://qollab.xyz/learn/docs/runtime-environment), [project-page guidance](https://qollab.xyz/learn/docs/write-your-project-page) and [hackathon terms](https://qollab.xyz/programs/hackathon/terms#submissions).

### Production and provenance records

- [Provenance and authorship](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/en/PROVENANCE.md)
- [Production notes and narration details](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/en/PRODUCTION_NOTES.md)
- [Deliverables](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/en/DELIVERABLES.md)

These records distinguish reference material from newly produced learning assets.

## Documentation and reproducibility

- [English documentation](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/en/README.md)
- [Português — Brasil](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/pt-BR/README.md)
- [Português — Portugal](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/pt-PT/README.md)
- [Español](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/es/README.md)
- [Project card](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/en/QOLLAB_PROJECT_CARD.md)
- [Submission checklist](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/docs/en/SUBMISSION_CHECKLIST.md)

## Submission and execution status

The repository records GitHub publication of the learning materials as complete.

Qollab import, platform simulator checks, IonQ execution checks, platform publication and final hackathon submission remain pending confirmation.

A separate public **2–3 minute demonstration** should show the runnable lab. The longer educational videos serve a different purpose and do not replace the submission demonstration.

## License and support

The software and documentation are released under the [MIT License](https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories/blob/main/LICENSE). The original English license is the authoritative license text.

That license does not establish rights over external YouTube stories, third-party reference assets or the terms governing generated artwork and synthetic voices. Those materials retain their applicable rights and conditions.

**Created by QuantGirls: Beatriz Karoline Cordeiro da Silva, Daiane Fonseca and Sonia Janara Silva Barros.**

This effort is supported by Qollab & IonQ
