import numpy as np


# Функція для визначення вектора власних значень
def eigenvector(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    idx = np.argmax(np.real(eigenvalues))
    return eigenvectors[:, idx]
