import numpy as np

# Функція множень матриць
def multiply_matrices(matrix1, matrix2):
    """Множить дві матриці, якщо їх розміри дозволяють це."""
    try:
        result = np.matmul(matrix1, matrix2)  # Використовуємо функцію dot для множення
        return result
    except ValueError:
        print("Неможливо помножити ці матриці. Перевірте їх розміри.")
        return None