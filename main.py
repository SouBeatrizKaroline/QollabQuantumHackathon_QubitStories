"""Python fallback: upload this and quantum.py without index.html/main.js."""
import json
import math
from quantum import run_suite

def main(shots: int = 512, phase_degrees: float = 0.0, logical_one: bool = False):
    report = json.loads(run_suite(backend, shots, math.radians(phase_degrees), logical_one))
    print("Qubit Stories — Watch. Predict. Run. Explain.")
    for video in report["videos"]:
        print(video["title"], video["url"])
    for lesson in report["experiments"]:
        print("\n" + lesson["title"])
        print("Predict:", lesson["prediction"])
        print(lesson["diagram"])
        print("Exact ideal probabilities:", lesson["ideal"])
        print("Backend counts:", lesson["counts"])
        print(lesson["explanation"])
    print("This effort is supported by Qollab & IonQ")

# Qollab calls main automatically. A local run uses only its free simulator.
if __name__ == "__main__" and "backend" not in globals():
    from qiskit.providers.basic_provider import BasicSimulator
    backend = BasicSimulator()
    main()
