class MyIterable:
    def __init__(self, data): # Cоздал класс MyIterable с методом __init__ для инициализации данных.
        self.data = data

    def __iter__(self):
        """
        Метод __iter__ возвращает сам объект,
        так как мы будем использовать его же в качестве итератора.
        Мы также инициализируем индекс, который будет использоваться для отслеживания
        текущей позиции в данных.
        """
        self.index = 0
        return self
                    # Методы __iter__ и __next__ делают наш класс итерируемым.
    def __next__(self):
        """
        Метод __next__ возвращает следующий элемент из данных и увеличивает индекс.
        Если индекс выходит за пределы данных, то вызывается исключение StopIteration,
        сигнализирующее о конце итерации.
        """
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        """
        Метод __getitem__ позволяет получать элементы по индексу,
        используя синтаксис квадратных скобок.
        """
        return self.data[index]


