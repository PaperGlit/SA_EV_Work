import numpy as np


# Функція для обчислення власних значень
def largest_eigenvalue(matrix):
    eigenvalues, _ = np.linalg.eig(matrix)
    return np.max(np.real(eigenvalues))