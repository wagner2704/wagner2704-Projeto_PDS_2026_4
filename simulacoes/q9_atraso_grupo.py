import matplotlib.pyplot as plt
from scipy import signal

# FIR
b_fir = signal.firwin(51, 0.3)
w1, gd1 = signal.group_delay((b_fir, [1]))

# IIR
b_iir, a_iir = signal.butter(4, 0.3)
w2, gd2 = signal.group_delay((b_iir, a_iir))

plt.figure(figsize=(10,5))

plt.plot(w1, gd1, label='FIR')
plt.plot(w2, gd2, label='IIR')

plt.title('Atraso de Grupo')
plt.legend()
plt.grid(True)

plt.savefig('../resultados/q9_atraso_grupo.png')
plt.show()
