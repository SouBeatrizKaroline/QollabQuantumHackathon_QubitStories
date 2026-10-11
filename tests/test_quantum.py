import json
import math
import unittest
from qiskit.quantum_info import Statevector, partial_trace, state_fidelity
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
from quantum import experiments, repetition_circuit, run_suite

class QuantumLessons(unittest.TestCase):
    def test_phase_is_hidden_in_z_but_visible_after_h(self):
        for phase in [0, math.pi/2, math.pi]:
            lessons = {x['key']:x for x in experiments(phase)}
            self.assertAlmostEqual(lessons['phase_z']['ideal']['0'], .5)
            self.assertAlmostEqual(lessons['interference']['ideal'].get('0',0), math.cos(phase/2)**2, places=7)

    def test_repetition_recovers_coherence_for_each_single_bit_flip(self):
        for theta in [0, .37, math.pi/2, math.pi]:
            target = QuantumCircuit(1); target.ry(theta,0)
            for error in [-1,0,1,2]:
                actual = Statevector.from_instruction(repetition_circuit(theta,error))
                self.assertAlmostEqual(state_fidelity(partial_trace(actual,[1,2]), Statevector.from_instruction(target)),1,places=7)

    def test_one_job_and_counts_for_every_lesson(self):
        class CountingBackend:
            def __init__(self): self.calls = 0; self.real = BasicSimulator()
            def run(self,*args,**kwargs): self.calls += 1; return self.real.run(*args,**kwargs)
            def __getattr__(self,name): return getattr(self.real,name)
        backend = CountingBackend()
        data = json.loads(run_suite(backend,128,math.pi,True))
        self.assertEqual(backend.calls,1)
        self.assertEqual(len(data['experiments']),8)
        for lesson in data['experiments']: self.assertEqual(sum(lesson['counts'].values()),128)
        corrected = next(x for x in data['experiments'] if x['key']=='corrected')
        self.assertTrue(all(bits.endswith('1') for bits in corrected['counts']))

if __name__ == '__main__': unittest.main()
