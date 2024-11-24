from functools import wraps  # Импортируем декоратор wraps из модуля functools

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)  # wraps сохраняет оригинальные атрибуты функции func
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # Вызываем оригинальную функцию и сохраняем ее результат
            try:
                return int(result)  # Пытаемся преобразовать результат к целому числу
            except (ValueError, TypeError):  # Если возникли исключения ValueError или TypeError
                return None  # Возвращаем None
        return wrapper  # Возвращаем функцию-обертку

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # Вызываем оригинальную функцию и сохраняем ее результат
            try:
                return str(result)  # Пытаемся преобразовать результат к строке
            except (ValueError, TypeError):  # Если возникли исключения ValueError или TypeError
                return None  # Возвращаем None
        return wrapper  # Возвращаем функцию-обертку

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # Вызываем оригинальную функцию и сохраняем ее результат
            try:
                return bool(result)  # Пытаемся преобразовать результат к логическому значению
            except (ValueError, TypeError):  # Если возникли исключения ValueError или TypeError
                return None  # Возвращаем None
        return wrapper  # Возвращаем функцию-обертку

    @staticmethod
    def to_float(func):
        @wraps(func)  # wraps сохраняет оригинальные атрибуты функции func
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # Вызываем оригинальную функцию и сохраняем ее результат
            try:
                return float(result)  # Пытаемся преобразовать результат к числу с плавающей запятой
            except (ValueError, TypeError):  # Если возникли исключения ValueError или TypeError
                return None  # Возвращаем None
        return wrapper  # Возвращаем функцию-обертку


"""
Сложная тема!Требуется повтор!
Подробный разбор задачи --> G:\Мой диск\Обучение\Beetroot Academy\Информация
"""
