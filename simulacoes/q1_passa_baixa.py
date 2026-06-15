import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Frequência de amostragem
fs = 1000

# Vetor de tempo
t = np.linspace(0, 1, fs, endpoint=False)

# Sinal composto
x = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*250*t)

# Projeto do filtro FIR passa-baixa
b = signal.firwin(51, cutoff=100, fs=fs)

# Aplicação do filtro
y = signal.lfilter(b, [1.0], x)

# Plotagem
plt.figure(figsize=(10,4))
plt.plot(t, x, label='Sinal Original')
plt.plot(t, y, label='Sinal Filtrado')
plt.legend()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Filtro FIR Passa-Baixa')
plt.grid(True)

plt.savefig('../resultados/q1_filtro_passa_baixa.png')
plt.show()
