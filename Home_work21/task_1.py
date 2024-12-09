class MyOpen:
    """
    Класс, имитирующий работу встроенной функции open().
    """

    def __init__(self, filename, mode='r'):
        """
        Инициализирует объект класса.

        Args:
            filename (str): Имя файла.
            mode (str, optional): Режим открытия файла (r, w, a ). По умолчанию 'r'.
        """
        self.filename = filename
        self.mode = mode
        self.counter = 0  # Счетчик операций с файлом
        self.log = []  # Список для хранения логов
        self.file = open(filename, mode)  # Открываем файл с помощью стандартной функции open()

    def __enter__(self):
        """
        Вызывается при входе в блок with.

        Returns:
            MyOpen: Возвращает сам объект класса для дальнейшей работы.
        """
        self.counter += 1
        self.log.append(f"Открыт файл {self.filename} в режиме {self.mode}")
        return self  # Возвращаем сам объект MyOpen

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Вызывается при выходе из блока with.

        Args:
            exc_type: Тип исключения (если произошло).
            exc_val: Значение исключения (если произошло).
            exc_tb: Traceback исключения (если произошло).
        """
        self.file.close()  # Закрываем файл
        self.log.append(f"Закрыт файл {self.filename}")
        # Если исключение произошло, оно будет подавлено, если вернуть True
        if exc_type:
            self.log.append(f"Исключение: {exc_type}, {exc_val}")
        return False  # Исключение не подавляется


# Пример использования:
with MyOpen('my_file.txt', 'w') as f:
    f.file.write('Hello, world!')  # Используем f.file для записи в файл
    print(f"Количество операций: {f.counter}")
    print(f"Лог: {f.log}")
