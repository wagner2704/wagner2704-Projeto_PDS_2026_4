import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000
t = np.linspace(0, 1, fs)

sinal = np.sin(2*np.pi*50*t)
ruido = np.random.normal(0, 0.5, len(t))

x = sinal + ruido

# Filtro Butterworth
b, a = signal.butter(4, 100, btype='low', fs=fs)

y = signal.lfilter(b, a, x)

plt.figure(figsize=(10,5))
plt.plot(t, x, label='Com Ruído')
plt.plot(t, y, label='Filtrado')
plt.legend()
plt.grid(True)

plt.savefig('../resultados/q3_iir_butterworth.png')
plt.show()
