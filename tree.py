# Клас для створення дерева
class Node:
    def __init__(self, name, parent=None):
        self.name = name  # Назва вузла
        self.parent = parent  # Батьківський елемент
        self.children = []  # Дочірні елементи
        self.matrix = None  # Матриця порівнянь
        self.largest_eigenvalue = None # Найбільше власне значення
        self.eigenvector = None  # Вектор власних значень

    def __repr__(self, level=0):
        indent = "    " * level
        representation = f"{indent}- {self.name}\n"
        for child in self.children:
            representation += child.__repr__(level + 1)
        return representation

    def add_child(self, child_node):
        self.children.append(child_node)

    def set_matrix(self, matrix):
        self.matrix = matrix

    def set_largest_eigenvalue(self, eigenvalue):
        self.largest_eigenvalue = eigenvalue

    def set_eigenvector(self, eigenvector):
        self.eigenvector = eigenvector

# Функція ініціалізації дерева
def init():
    root = Node("Тифлокоментування")  # Батьківський вузол для всіх критеріїв

    # Фактори
    technical_implementation = Node("Технічна реалізація", parent=root)
    cost_and_resources = Node("Вартість і ресурси", parent=root)

    root.add_child(technical_implementation)
    root.add_child(cost_and_resources)

    # Критерії для Технічної реалізації
    convenience = Node("Підприємницька зручність", parent=technical_implementation)
    user_friendly = Node("Користувацька зручність", parent=technical_implementation)
    security = Node("Безпека даних", parent=technical_implementation)

    technical_implementation.add_child(convenience)
    technical_implementation.add_child(user_friendly)
    technical_implementation.add_child(security)

    # Критерії для Вартість і ресурси
    development_cost = Node("Витрати на розробку системи", parent=cost_and_resources)
    maintenance_cost = Node("Витрати на підтримку системи", parent=cost_and_resources)
    resource_efficiency = Node("Ефективність використання ресурсів", parent=cost_and_resources)

    cost_and_resources.add_child(development_cost)
    cost_and_resources.add_child(maintenance_cost)
    cost_and_resources.add_child(resource_efficiency)

    # Заповнення критеріїв альтернативами
    alternatives = ["Комп'ютерний застосунок", "Мобільний застосунок", "Веб-застосунок"]
    for second_level_node in root.children:
        for third_level_node in second_level_node.children:
            for alternative in alternatives:
                third_level_node.add_child(Node(alternative))

    # Вивід вигляду дерева
    print("Вигляд дерева:")
    print(root)

    return root