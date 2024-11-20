import numpy as np


# Функція для заповнення матриці парних порівнянь
def expert_survey(matrix_name, items):
    matrix = []
    print(f"\nЗаповнення матриці парних порівнянь для {matrix_name}:")
    for i in range(len(items)):
        row = []
        for j in range(len(items)):
            if i == j:
                row.append(1)
            elif i < j:
                value = float(input(f"Порівняти {items[i]} з {items[j]} (оцінка): "))
                row.append(value)
            else:
                row.append(1 / matrix[j][i])  # Зворотній елемент
        matrix.append(row)
    return np.array(matrix)