import matplotlib.pyplot as plt
from scipy import signal

fs = 1000

# FIR
b_fir = signal.firwin(51, 100, fs=fs)
w1, h1 = signal.freqz(b_fir)

# IIR
b_iir, a_iir = signal.butter(4, 100, fs=fs)
w2, h2 = signal.freqz(b_iir, a_iir)

plt.figure(figsize=(10,5))

plt.plot(w1, abs(h1), label='FIR')
plt.plot(w2, abs(h2), label='IIR')

plt.title('Resposta em Frequência')
plt.legend()
plt.grid(True)

plt.savefig('../resultados/q4_comparacao.png')
plt.show()
