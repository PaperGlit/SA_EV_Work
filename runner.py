import numpy as np

# Структура дерева
criteria = ["Технічна реалізація", "Вартість і ресурси"]
technical_implementation_subcriteria = ["Безпека даних", "Підприємницька зручність", "Користувацька зручність"]
cost_and_resources_subcriteria = ["Витрати на розробку системи", "Витрати на підтримку системи",
                                  "Ефективність використання ресурсів"]
alternatives = ["Комп'ютерний застосунок", "Мобільний застосунок",  "Веб-застосунок"]

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

def multiply_matrices(matrix1, matrix2):
    """Множить дві матриці, якщо їх розміри дозволяють це."""
    try:
        result = np.matmul(matrix1, matrix2)# Використовуємо функцію dot для множення
        return result
    except ValueError:
        print("Неможливо помножити ці матриці. Перевірте їх розміри.")
        return None


# Функція для збору оцінок для критеріїв
def expert_survey_for_criteria():
    # Проведення експертного опитування для критеріїв
    criteria_matrix = expert_survey("Критерії", criteria)
    return criteria_matrix, criteria


# Функція для збору оцінок для підкритеріїв
def expert_survey_for_subcriteria(criteria_name, subcriteria):
    subcriteria_matrix = expert_survey(f"Підкритерії для {criteria_name}", subcriteria)
    return subcriteria_matrix


# Функція для збору оцінок для альтернатив
def expert_survey_for_alternatives(subcriterion_name, alternatives):
    alternatives_matrix = expert_survey(f"Альтернативи для {subcriterion_name}", alternatives)
    return alternatives_matrix


# Функція для обчислення власних значень
def largest_eigenvalue(matrix):
    eigenvalues, _ = np.linalg.eig(matrix)
    return np.max(np.real(eigenvalues))


# Функція для визначення вектора власних значень
def eigenvector(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    idx = np.argmax(np.real(eigenvalues))
    return eigenvectors[:, idx]

# Функція для визначення найкращої альтернативи на основі значень
def best_alternative(alternatives, vector):
    max_index = np.argmax(vector)
    return alternatives[max_index]

# Основна логіка
def main():
    # 1. Заповнення матриці критеріїв
    criteria_matrix, criteria = expert_survey_for_criteria()
    print("\nМатриця парних порівнянь для критеріїв:")
    print(criteria_matrix)

    # 2. Заповнення матриць підкритеріїв
    technical_matrix = expert_survey_for_subcriteria("Технічна реалізація", technical_implementation_subcriteria)
    cost_matrix = expert_survey_for_subcriteria("Вартість і ресурси", cost_and_resources_subcriteria)

    print("\nМатриця парних порівнянь для Технічної реалізації:")
    print(technical_matrix)
    print("\nМатриця парних порівнянь для Вартість і ресурси:")
    print(cost_matrix)

    # 3. Заповнення матриць альтернатив
    tech_alternatives_security_matrix = expert_survey_for_alternatives("Безпека даних", alternatives)
    tech_alternatives_worker_matrix = expert_survey_for_alternatives("Підприємницька зручність", alternatives)
    tech_alternatives_user_matrix = expert_survey_for_alternatives("Користувацька зручність", alternatives)
    cost_alternatives_development_matrix = expert_survey_for_alternatives("Витрати на розробку системи", alternatives)
    cost_alternatives_maintenance_matrix = expert_survey_for_alternatives("Витрати на підтримку системи", alternatives)
    cost_alternatives_efficiency_matrix = expert_survey_for_alternatives("Ефективність використання ресурсів", alternatives)


    print("\nМатриця парних порівнянь для альтернатив Безпека даних:")
    print(tech_alternatives_security_matrix)
    print("\nМатриця парних порівнянь для альтернатив Підприємницька зручність:")
    print(tech_alternatives_worker_matrix)
    print("\nМатриця парних порівнянь для альтернатив Користувацька зручність:")
    print(tech_alternatives_user_matrix)

    print("\nМатриця парних порівнянь для альтернатив Витрати на розробку системи:")
    print(cost_alternatives_development_matrix)
    print("\nМатриця парних порівнянь для альтернатив Витрати на підтримку системи:")
    print(cost_alternatives_maintenance_matrix)
    print("\nМатриця парних порівнянь для альтернатив Вартість і ресурси (ефективність використання ресурсів):")
    print(cost_alternatives_efficiency_matrix)

    # 4. Обчислення власних значень і визначення найкращої альтернативи
    # Для критеріїв
    largest_value_criteria = largest_eigenvalue(criteria_matrix)
    print(f"\nНайбільше власне значення для критеріїв: {largest_value_criteria}")

    # Для підкритеріїв
    largest_value_technical = largest_eigenvalue(technical_matrix)
    largest_value_cost = largest_eigenvalue(cost_matrix)
    print(f"Найбільше власне значення для Технічної реалізації: {largest_value_technical}")
    print(f"Найбільше власне значення для Вартість і ресурси: {largest_value_cost}")

    # Для альтернатив
    criteria_vector = eigenvector(criteria_matrix)
    technical_vector = eigenvector(technical_matrix)
    cost_vector = eigenvector(cost_matrix)
    tech_alternatives_security_vector = eigenvector(tech_alternatives_security_matrix)
    tech_alternatives_worker_vector = eigenvector(tech_alternatives_worker_matrix)
    tech_alternatives_user_vector = eigenvector(tech_alternatives_user_matrix)
    cost_alternatives_development_vector = eigenvector(cost_alternatives_development_matrix)
    cost_alternatives_maintenance_vector = eigenvector(cost_alternatives_maintenance_matrix)
    cost_alternatives_efficiency_vector = eigenvector(cost_alternatives_efficiency_matrix)

    print("\nВектор власних значень для критеріїв:", criteria_vector)
    print("Вектор власних значень для альтернатив Технічної реалізації:", technical_vector)
    print("Вектор власних значень для альтернатив Вартість і ресурси:", cost_vector)
    print("Вектор власних значень для альтернатив Безпека даних:", tech_alternatives_security_vector)
    print("Вектор власних значень для альтернатив Підприємницька зручність:", tech_alternatives_worker_vector)
    print("Вектор власних значень для альтернатив Користувацька зручність:", tech_alternatives_user_vector)
    print("Вектор власних значень для альтернатив Витрати на розробку системи:", cost_alternatives_development_vector)
    print("Вектор власних значень для альтернатив Витрати на підтримку системи:", cost_alternatives_maintenance_vector)
    print("Вектор власних значень для альтернатив Ефективність використання ресурсів:", cost_alternatives_efficiency_vector)

    technical_vector_combined = np.array([tech_alternatives_security_vector, tech_alternatives_worker_vector, tech_alternatives_user_vector])
    cost_vector_combined = np.array([cost_alternatives_development_vector, cost_alternatives_maintenance_vector, cost_alternatives_efficiency_vector])
    print(cost_vector_combined.T)

    technical_vector_multiplied = multiply_matrices(technical_vector_combined.T, technical_vector)
    cost_vector_multiplied = multiply_matrices(cost_vector_combined.T, cost_vector)

    criteria_vector_combined  = np.array([technical_vector_multiplied, cost_vector_multiplied])

    final_vector = multiply_matrices(criteria_vector_combined.T, criteria_vector)

    best_choice = best_alternative(alternatives, final_vector)
    print("Найкращий вибір:", best_choice)
# Виконання програми
main()
