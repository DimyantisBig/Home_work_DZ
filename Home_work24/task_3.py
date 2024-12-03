class MyStack:
    def __init__(self):
        """Инициализирует стек.
        Создает пустой список для хранения элементов стека.
        """
        self.items = []

    def push(self, item):
        """Добавляет элемент в стек.
        Добавляет элемент в конец списка.
        """
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент стека.
        Удаляет и возвращает последний элемент списка.
        """
        return self.items.pop()

    def get_from_stack(self, e):
        """Ищет и возвращает элемент в стеке.
        Создает временный стек для хранения элементов, пока не найдем нужный.
        Удаляем элементы из основного стека и помещаем их во временный стек.
        Если найден нужный элемент, возвращаем его.
        Если не найден, восстанавливаем исходный порядок элементов в основном стеке из временного стека.
        """
        temp_stack = []
        while self.items:
            item = self.items.pop()
            if item == e:
                return item
            temp_stack.append(item)
        while temp_stack:
            self.items.append(temp_stack.pop())
        raise ValueError("Element not found")

class MyQueue:
    def __init__(self):
        """Инициализирует очередь.
        Создает пустой список для хранения элементов очереди.
        """
        self.items = []

    def push(self, item):
        """Добавляет элемент в очередь.
        Добавляет элемент в конец списка.
        """
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает первый элемент очереди.
        Удаляет и возвращает первый элемент списка.
        """
        return self.items.pop(0)

    def get_from_queue(self, e):
        """Ищет и возвращает элемент в очереди.
        Создает временную очередь для хранения элементов, пока не найдем нужный.
        Удаляем элементы из основной очереди и помещаем их во временную очередь.
        Если найден нужный элемент, возвращаем его.
        Если не найден, восстанавливаем исходный порядок элементов в основной очереди из временной очереди.
        """
        temp_queue = []
        while self.items:
            item = self.items.pop(0)
            if item == e:
                return item
            temp_queue.append(item)
        while temp_queue:
            self.items.append(temp_queue.pop(0))
        raise ValueError("Element not found")

    """Тема на повторение!!!
    Нужно досконально разобраться как и что происходит.Повторить правила!"""