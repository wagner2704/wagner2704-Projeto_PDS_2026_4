import matplotlib.pyplot as plt
from scipy import signal

b, a = signal.butter(4, 0.2)

z, p, k = signal.tf2zpk(b, a)

plt.figure(figsize=(6,6))

plt.scatter(z.real, z.imag, label='Zeros')
plt.scatter(p.real, p.imag, label='Polos')

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')

plt.legend()
plt.grid(True)

plt.savefig('../resultados/q5_polos_zeros.png')
plt.show()
