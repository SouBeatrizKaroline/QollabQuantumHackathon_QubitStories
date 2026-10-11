"""Video-linked Qiskit experiments; no network, credentials or paid backend."""
import json
import math
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector

VIDEOS = [
    {"id": "EAcDVqTb0lk", "title": "The World of Qubits", "language": "English", "url": "https://youtu.be/EAcDVqTb0lk"},
    {"id": "nkQpc2YPSCA", "title": "O Mundo dos Qubits", "language": "Português", "url": "https://youtu.be/nkQpc2YPSCA"},
    {"id": "uPTSfysNvgw", "title": "The Fellowship Of The Qubit", "language": "English", "url": "https://youtu.be/uPTSfysNvgw"},
]

def repetition_circuit(theta=0.0, error_qubit=0):
    """Encode, inject one X, coherently decode and correct. q0 is recovered."""
    qc = QuantumCircuit(3)
    qc.ry(theta, 0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    if error_qubit in (0, 1, 2):
        qc.x(error_qubit)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.ccx(1, 2, 0)
    return qc

def experiments(phase=0.0, logical_one=False):
    """Exact predictions are separate from backend shot counts."""
    items = []
    def add(key, title, circuit, links, prediction, explanation):
        ideal = {k: round(float(v), 8) for k, v in Statevector.from_instruction(circuit).probabilities_dict().items() if v > 1e-10}
        measured = circuit.copy()
        measured.measure_all()
        items.append({"key": key, "title": title, "circuit": measured, "ideal": ideal, "links": links, "prediction": prediction, "explanation": explanation})
    c = QuantumCircuit(1)
    add("bit", "A definite zero / Um zero definido", c, [20, 15, 12], "0: 100%", "A computational-basis state gives a definite outcome in this basis.")
    c = QuantumCircuit(1); c.h(0)
    add("superposition", "Prepare, then measure / Preparar e medir", c, [48, 38, 12], "0: 50%, 1: 50%", "H prepares |+>. Repeated shots repeat preparation; they are not repeated measurements of one unchanged qubit.")
    c = QuantumCircuit(1); c.h(0); c.p(phase, 0)
    add("phase_z", "Phase hidden in Z / Fase oculta em Z", c, [97, 81, 24], "0: 50%, 1: 50% for every phase", "Changing relative phase leaves Z-basis probabilities unchanged. This is why superposition is more than a classical coin.")
    c = QuantumCircuit(1); c.h(0); c.p(phase, 0); c.h(0)
    add("interference", "Make phase visible / Tornar a fase visível", c, [97, 81, 24], f"P(0) = cos²(phase/2) = {math.cos(phase / 2)**2:.3f}", "The final H converts relative phase into a change in outcome probabilities. Phase 0 returns zero; phase pi returns one.")
    c = QuantumCircuit(2); c.h(0); c.cx(0, 1)
    add("bell_z", "A shared state / Um estado conjunto", c, [117, 98, 40], "00: 50%, 11: 50%", "Bell-state Z measurements are correlated. Each qubit's marginal remains 50/50. These correlations alone are not a proof of entanglement and do not transmit messages.")
    c = QuantumCircuit(2); c.h(0); c.cx(0, 1); c.h(0); c.h(1)
    add("bell_x", "Change both measurement bases / Mudar as duas bases", c, [117, 98, 40], "00: 50%, 11: 50%", "H before measurement measures X. The prepared Bell state stays correlated in both X and Z; a classical 00/11 mixture would be uncorrelated in X.")
    c = QuantumCircuit(1)
    if logical_one: c.x(0)
    c.x(0)
    add("unprotected", "One bit flip / Um erro de bit", c, [None, None, 70], f"Incorrect logical bit: {0 if logical_one else 1}", "We deliberately inject an X gate. This is a controlled error, not a realistic hardware noise model.")
    c = repetition_circuit(math.pi if logical_one else 0.0, 0)
    add("corrected", "Three physical qubits / Três qubits físicos", c, [None, None, 78], "Recovered q0 equals the input logical bit", "A three-qubit repetition code corrects one X error. Read q0 as the RIGHTMOST bit. Ancillas retain syndrome information. It does not protect against phase errors or demonstrate fault tolerance.")
    return items

def run_suite(selected_backend, shots=512, phase=0.0, logical_one=False):
    shots = int(shots); phase = float(phase)
    if not 32 <= shots <= 4096: raise ValueError("Shots must be between 32 and 4096")
    if not math.isfinite(phase): raise ValueError("Phase must be finite")
    items = experiments(phase, bool(logical_one))
    circuits = transpile([x["circuit"] for x in items], selected_backend, optimization_level=1)
    # One job per run, including on IonQ. Never create another provider here.
    result = selected_backend.run(circuits, shots=shots).result()
    output = []
    for i, x in enumerate(items):
        counts = result.get_counts(i)
        output.append({k: v for k, v in x.items() if k != "circuit"} | {"counts": counts, "diagram": str(x["circuit"].draw(output="text"))})
    return json.dumps({"videos": VIDEOS, "shots": shots, "phase": phase, "logical_one": bool(logical_one), "experiments": output}, ensure_ascii=False)
