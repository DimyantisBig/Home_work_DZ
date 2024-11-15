class CustomException(Exception):  # Наследуемся от встроенного Exception
    def __init__(self, message):
        super().__init__(message)  # Передаем сообщение в базовый класс Exception
        with open('logs.txt', 'a') as file:
            file.write(message + '\n')  # Записываем сообщение в файл