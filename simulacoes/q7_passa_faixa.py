import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000
t = np.linspace(0, 1, fs)

x = (
    np.sin(2*np.pi*50*t)
    + np.sin(2*np.pi*150*t)
    + np.sin(2*np.pi*300*t)
)

# Passa-faixa
b, a = signal.butter(4, [100, 200], btype='bandpass', fs=fs)

y = signal.lfilter(b, a, x)

plt.figure(figsize=(10,5))
plt.plot(t, y)
plt.title('Filtro Passa-Faixa')
plt.grid(True)

plt.savefig('../resultados/q7_passa_faixa.png')
plt.show()
