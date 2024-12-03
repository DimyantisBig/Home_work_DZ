# Проверяет, сбалансированы ли скобки в выражении.
def is_balanced(expression):
    """
    Args:
        expression: Строка с выражением.

    Returns:
        True, если скобки сбалансированы, иначе False.
    """

    # Инициализируем пустой стек для хранения открывающихся скобок
    stack = []

    # Задаем строки с открывающими и закрывающими скобками
    opening_brackets = '({['  # Открывающиеся скобки
    closing_brackets = ')}]'  # Закрывающиеся скобки

    # Создаем словарь, связывающий открывающиеся и закрывающиеся скобки
    brackets_map = dict(zip(opening_brackets, closing_brackets))

    # Проходим по каждому символу в строке
    for char in expression:
        if char in opening_brackets:
            # Если символ - открывающая скобка, добавляем его в стек
            stack.append(char)
        elif char in closing_brackets:
            # Если символ - закрывающая скобка, проверяем соответствие
            if not stack or brackets_map[stack.pop()] != char:
                # Если стек пуст или последняя открывающая скобка не соответствует текущей закрывающей
                return False

    # Если стек пуст после обработки всех символов, скобки сбалансированы
    return not stack


# Реализация вспомогательного класса Stack
class Stack:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов стека
        self.items = []

    def push(self, item):
        # Добавляем элемент в стек
        self.items.append(item)

    def pop(self):
        # Удаляем и возвращаем верхний элемент стека, если он не пустой
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def isEmpty(self):
        # Проверяем, пуст ли стек
        return len(self.items) == 0


# Функция для реверсирования строки с использованием стека
def reverse_string(input_string):
    # Создаем экземпляр класса Stack
    stack = Stack()

    # Помещаем каждый символ строки в стек
    for char in input_string:
        stack.push(char)

    # Инициализируем пустую строку для хранения результата
    reversed_string = ""

    # Удаляем символы из стека и добавляем их к результату
    while not stack.isEmpty():
        reversed_string += stack.pop()

    # Возвращаем перевернутую строку
    return reversed_string


# Примеры использования:
print(is_balanced("({[]})"))  # Вывод: True
print(is_balanced("({)}"))   # Вывод: False
print(is_balanced("([]"))    # Вывод: False

"""Тудная тема.Частично не понятно.
Требуется повтор предидущих тем.!"""