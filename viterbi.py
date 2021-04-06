from numpy import load
import numpy as np


def viterbi(A, C, B, O):
    

    I = A.shape[0]    
    N = len(O)  

    D = np.zeros((I, N))
    E = np.zeros((I, N-1)).astype(np.int32)
    D[:, 0] = np.multiply(C, B[:, 0])


    for n in range(1, N):
        for i in range(I):
            temp_product = np.multiply(A[:, i], D[:, n-1])
            D[i, n] = np.max(temp_product) * B[i, O[n]]
            E[i, n-1] = np.argmax(temp_product)

    S_opt = np.zeros(N).astype(np.int32)
    S_opt[-1] = np.argmax(D[:, -1])
    for n in range(N-2, 0, -1):
        S_opt[n] = E[int(S_opt[n+1]), n]

    return S_opt, D, E



data = load('model.npy', allow_pickle=True)

A = np.array(data[4])

C = np.array(data[2])

B = np.array(data[3])
print(data[4])