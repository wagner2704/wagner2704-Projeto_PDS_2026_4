import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 500
t = np.linspace(0, 5, fs*5)

# Simulação de sensor com ruído
sensor = np.sin(2*np.pi*2*t)
ruido = np.random.normal(0, 0.3, len(t))

x = sensor + ruido

# Filtro passa-baixa
b, a = signal.butter(4, 5, btype='low', fs=fs)

y = signal.lfilter(b, a, x)

plt.figure(figsize=(10,5))

plt.plot(t, x, label='Sensor com Ruído')
plt.plot(t, y, label='Filtrado')

plt.legend()
plt.grid(True)

plt.title('Aplicação Prática — Filtragem de Sensor')

plt.savefig('../resultados/q10_sensor.png')
plt.show()
