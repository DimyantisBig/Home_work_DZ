import  re  # модуль re, который предоставляет функции для работы с регулярными выражениями.

class EmailValidator:
    def __init__(self, email):
        # Сохраняем переданный параметр email как атрибут объекта
        self.email = email
        # Вызываем метод validate для проверки корректности email
        self.validate()

    def validate(self):
        # Проверяем, является ли email строкой
        if not isinstance(self.email, str):
            # Если email не строка, выбрасываем исключение TypeError с сообщением об ошибке
            raise TypeError('Email must be a string!')

        # Создаем шаблон регулярного выражения для проверки формата email
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        # Проверяем, соответствует ли email шаблону регулярного выражения
        if not re.match(email_pattern, self.email):
            # Если email не соответствует шаблону, выбрасываем исключение TypeError с сообщением об ошибке
            raise TypeError('Email must be a valid email address!')


"""
Сложная тема.
Подробный разбор задания -> G:\Мой диск\Обучение\Beetroot Academy\Информация
"""

