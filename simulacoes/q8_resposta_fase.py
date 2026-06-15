import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# FIR
b_fir = signal.firwin(51, 0.3)
w1, h1 = signal.freqz(b_fir)

# IIR
b_iir, a_iir = signal.butter(4, 0.3)
w2, h2 = signal.freqz(b_iir, a_iir)

plt.figure(figsize=(10,5))

plt.plot(w1, np.angle(h1), label='FIR')
plt.plot(w2, np.angle(h2), label='IIR')

plt.title('Resposta de Fase')
plt.legend()
plt.grid(True)

plt.savefig('../resultados/q8_resposta_fase.png')
plt.show()
