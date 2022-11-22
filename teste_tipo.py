from sympy import *
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2,2)

bis_vet_resul = [0.5, 0.25, 0.375, 0.3125, 0.34375, 0.328125, 0.3359375, 0.33984375, 0.337890625, 0.3369140625, 0.33740234375, 0.337646484375, 0.3375244140625, 0.33758544921875]
pf_vet_resul = [0.375000000000000, 0.338624338624339, 0.337635045511401, 0.337609625287334, 0.337608973136452, 0.337608956406328, 0.337608955977138, 0.337608955966128, 0.337608955965845, 0.337608955965838, 0.337608955965838]
nw_vet_resul = [0.16666666666666663, 0.33541017653167193, 0.3376083931509949, 0.33760895596580065]
bir_vet_resul = [0.333333333333333, 0.337606837606838, 0.337608955965313]

x_val = np.arange(0, len(bis_vet_resul), 1)
axs[0,0].plot(x_val,bis_vet_resul)
axs[0,0].set_title("Bissecção")
x_val = np.arange(0, len(pf_vet_resul), 1)
axs[0,1].plot(x_val,pf_vet_resul)
axs[0,1].set_title("Posição Falsa")
x_val = np.arange(0, len(nw_vet_resul), 1)
axs[1,0].plot(x_val,nw_vet_resul)
axs[1,0].set_title("Newton Raphson")
x_val = np.arange(0, len(bir_vet_resul), 1)
axs[1,1].plot(x_val,bir_vet_resul)
axs[1,1].set_title("Birge Vieta")

for ax in axs.flat:
    ax.set(xlabel='Número de iterações (N)', ylabel='Valor calculado (xi_1)')

plt.show()