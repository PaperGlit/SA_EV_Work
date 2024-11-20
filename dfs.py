# Функція руху по дереву методом DFS
def dfs(node):
    if node is None:
        return

    # Виведення інформації про поточний вузол
    print(f"\nІм'я: {node.name}")
    if node.largest_eigenvalue is not None:
        print(f"Найбільше власне значення: {node.largest_eigenvalue}")
    if node.eigenvector is not None:
        print(f"Вектор власних значень: {node.eigenvector}")
    if node.matrix is not None:
        print(f"Матриця пріоритетів:\n{node.matrix}")

    # Рекурсивний обхід дочірніх вузлів
    for child in node.children:
        dfs(child)