class UnsortedList:
    # Класс для работы с неупорядоченным списком.
    # Реализует основные методы, позволяющие добавлять, удалять элементы,
    # находить их индекс, вставлять элементы в определенное место и брать срезы.

    def __init__(self):
        # Конструктор класса. Создает пустой список для хранения элементов.
        self.items = []  # Список для хранения элементов, переданных пользователем.

    def append(self, item):
        # Метод для добавления элемента в конец списка.
        # Аргументы:
        # - item: добавляемый элемент.
        self.items.append(item)  # Встроенный метод append добавляет элемент в конец списка.

    def index(self, item):
        # Метод для поиска индекса первого вхождения заданного элемента.
        # Аргументы:
        # - item: элемент, индекс которого нужно найти.
        # Возвращает:
        # - Индекс элемента, если он найден.
        # Вызывает исключение ValueError, если элемент отсутствует.
        for i in range(len(self.items)):  # Проходим по всем индексам в списке.
            if self.items[i] == item:  # Проверяем, равен ли текущий элемент искомому.
                return i  # Возвращаем индекс, если элемент найден.
        raise ValueError("Item not found")  # Исключение, если элемент не найден.

    def pop(self, i=None):
        # Метод для удаления и возврата элемента из списка.
        # Аргументы:
        # - i: индекс элемента для удаления (по умолчанию None). Если индекс не указан, удаляется последний элемент.
        # Возвращает:
        # - Удаленный элемент.
        if i is None:  # Если индекс не указан...
            return self.items.pop()  # ...удаляем и возвращаем последний элемент списка.
        else:
            return self.items.pop(i)  # Удаляем и возвращаем элемент по заданному индексу.

    def insert(self, i, item):
        # Метод для вставки элемента на заданную позицию.
        # Аргументы:
        # - i: индекс, на который нужно вставить элемент.
        # - item: элемент для вставки.
        self.items.insert(i, item)  # Встроенный метод insert добавляет элемент на указанный индекс.

    def slice(self, start, stop):
        # Метод для получения среза списка.
        # Аргументы:
        # - start: начальный индекс среза (включительно).
        # - stop: конечный индекс среза (не включается).
        # Возвращает:
        # - Новый список, содержащий элементы от start до stop.
        return self.items[start:stop]  # Возвращаем срез списка, используя стандартный синтаксис Python.