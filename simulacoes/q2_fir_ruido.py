import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000
t = np.linspace(0, 1, fs)

# Sinal original
sinal = np.sin(2*np.pi*50*t)

# Ruído branco
ruido = np.random.normal(0, 0.5, len(t))

# Sinal ruidoso
x = sinal + ruido

# Filtro FIR
b = signal.firwin(101, cutoff=100, fs=fs)

# Filtragem
y = signal.lfilter(b, [1.0], x)

# Gráficos
plt.figure(figsize=(10,5))
plt.plot(t, x, label='Sinal com Ruído')
plt.plot(t, y, label='Sinal Filtrado')
plt.legend()
plt.grid(True)

plt.savefig('../resultados/q2_fir_ruido.png')
plt.show()
