import tree
import numpy as np
from dfs import dfs
from eigenvector import eigenvector
from expert_survey import expert_survey
from multiply_matrices import multiply_matrices
from largest_eigenvalue import largest_eigenvalue

# Функція для визначення найкращої альтернативи на основі вектора власних значень
def best_alternative(vector):
    alternatives = ["Комп'ютерний застосунок", "Мобільний застосунок", "Веб-застосунок"]
    max_index = np.argmax(vector)  # Знаходимо індекс максимального значення вектора
    return alternatives[max_index]  # Повертаємо альтернативу, що відповідає цьому індексу


# Основна логіка для створення дерева критеріїв
def main():
    # Створення дерева критеріїв
    root = tree.init()

    # Заповнення матриці для факторів
    root.set_matrix(expert_survey("Фактори", [node.name for node in root.children]))

    # Заповнення матриці для критеріїв
    for node in root.children:
        subcriteria_names = [child.name for child in node.children]
        subcriteria_matrix = expert_survey(f"Критерії для {node.name}", subcriteria_names)
        node.set_matrix(subcriteria_matrix)

    # Заповнення матриць для альтернатив
    for node in root.children:
        for subnode in node.children:
            alternatives_matrix = expert_survey(f"Альтернативи для {subnode.name}", [alternative.name for alternative in subnode.children])
            subnode.set_matrix(alternatives_matrix)

    # Обчислення найбільших власних значень для факторів
    largest_value_factor = largest_eigenvalue(root.matrix)
    print(f"\nНайбільше власне значення для факторів: {largest_value_factor}")
    root.set_largest_eigenvalue(largest_value_factor)

    # Обчислення найбільших власних значень для критеріїв
    for node in root.children:
        largest_value_criteria = largest_eigenvalue(node.matrix)
        print(f"Найбільше власне значення для {node.name}: {largest_value_criteria}")
        node.set_largest_eigenvalue(largest_value_criteria)

    # Обчислення найбільших власних значень для альтернатив
    for node in root.children:
        for subnode in node.children:
            largest_value_alternatives = largest_eigenvalue(subnode.matrix)
            print(f"Найбільше власне значення для {subnode.name}: {largest_value_alternatives}")
            subnode.set_largest_eigenvalue(largest_value_alternatives)

    # Обчислення вектора власних значень для факторів
    factor_vector = eigenvector(root.matrix)
    print("\nВектор власних значень для Факторів:")
    print(factor_vector)
    root.set_eigenvector(factor_vector)

    # Обчислення вектора власних значень для критеріїв
    criteria_vector = []
    for node in root.children:
        criterion_vector = eigenvector(node.matrix)
        criteria_vector.append(criterion_vector)
        print(f"\nВектор власних значень для {node.name}:")
        print(criterion_vector)
        node.set_eigenvector(criterion_vector)

    # Обчислення вектора власних значень для альтернатив
    alternatives_vector = []
    for node in root.children:
        for subnode in node.children:
            alternative_vector = eigenvector(subnode.matrix)
            alternatives_vector.append(alternative_vector)
            print(f"\nВектор власних значень для {subnode.name}:")
            print(alternative_vector)
            subnode.set_eigenvector(alternative_vector)

    # Комбінування векторів пріоритетів альтернатив
    part_len = len(alternatives_vector) // len(criteria_vector)
    technical_vector_combined = np.array(alternatives_vector[:part_len])
    cost_vector_combined = np.array(alternatives_vector[:part_len])

    # Множення векторів критеріїв
    technical_vector_multiplied = multiply_matrices(technical_vector_combined.T, criteria_vector[0])
    cost_vector_multiplied = multiply_matrices(cost_vector_combined.T, criteria_vector[1])

    # Комбінування щойно отриманих векторів критеріїв
    factor_vector_combined = np.array([technical_vector_multiplied, cost_vector_multiplied])

    # Множення векторів факторів
    final_vector = multiply_matrices(factor_vector_combined.T, factor_vector)
    print("\nФінальний вектор власних значень:")
    print(final_vector)

    # Знаходження та виведення найкращого вибору
    best_choice = best_alternative(final_vector)
    print("\nНайкращий вибір:", best_choice)

    # Виведення фінального вигляду дерева
    print("\nФінальний вигляд дерева:")
    dfs(root)