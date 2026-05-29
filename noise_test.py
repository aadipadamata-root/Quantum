from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

# 1. Create a "Noisy" Hardware Environment
noise_model = NoiseModel()
error = depolarizing_error(0.05, 1) # 5% gate error (very high!)
noise_model.add_all_qubit_quantum_error(error, ['h'])

# 2. Build a simple circuit
qc = QuantumCircuit(1)
qc.h(0) # Flip it to superposition
qc.measure_all()

# 3. Run on a "Perfect" Simulator vs "Noisy" Hardware
sim = AerSimulator()
perfect_counts = sim.run(qc).result().get_counts()
noisy_counts = sim.run(qc, noise_model=noise_model).result().get_counts()

print(f"Perfect Hardware: {perfect_counts}")
print(f"Noisy Hardware  : {noisy_counts}")