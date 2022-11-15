import numpy as np
import matplotlib.pyplot as plt
import random

piece0 = lambda : 1 if random.random()<0.49 else -1
piece1 = lambda : 1 if random.random()<0.09 else -1
piece2 = lambda : 1 if random.random()<0.74 else -1

def jeu_A(J):
    J += np.array([piece0() for i in range(100)])

def jeu_B(J):
    M = J%3==0
    J[M]+=np.array([piece1() for i in range(100)])[M]
    J[M==0]+=np.array([piece2() for i in range(100)])[M==0]

def jeu_C(J):
    if random.random()<0.5 :
        jeu_A(J)
    else :
        jeu_B(J)

Joueurs = np.full(100, 1000)
n = 1000000
N = np.arange(n)
X = np.zeros((100, n), dtype=np.ulonglong)
X[:,0] = Joueurs
for i in range(1, n):
    jeu_C(Joueurs)
    X[:,i]=Joueurs

for i in range(100):
    plt.plot(N, X[i])
plt.show()