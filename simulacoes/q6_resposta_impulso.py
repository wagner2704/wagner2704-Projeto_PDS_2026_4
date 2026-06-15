import matplotlib.pyplot as plt
from scipy import signal

# FIR
b_fir = signal.firwin(21, 0.3)
imp_fir = signal.dimpulse((b_fir, [1]))

# IIR
b_iir, a_iir = signal.butter(4, 0.3)
imp_iir = signal.dimpulse((b_iir, a_iir))

print("Resposta FIR:", imp_fir)
print("Resposta IIR:", imp_iir)
