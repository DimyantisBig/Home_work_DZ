# Декоратор arg_rules принимает три аргумента:
# max_length - максимальная допустимая длина текста,
# type_ - ожидаемый тип данных для аргумента (например, str),
# contains - список символов, которые должны присутствовать в аргументе текста.
def arg_rules(max_length: int, type_: type, contains: list):
    # Определяем функцию-декоратор, которая принимает функцию func, которую будем проверять
    def decorator(func):
        # Определяем обёртку (wrapper) для функции func, которая принимает один аргумент text
        def wrapper(text):
            # Проверка: если длина text больше max_length, выводим сообщение об ошибке
            if len(text) > max_length:
                print('Length exceeds the specified length')

            # Проверка: если text не соответствует указанному типу type_, выводим сообщение об ошибке
            if not isinstance(text, type_):
                print('Not a text')

            # Проверка: для каждого символа из списка contains проверяем, есть ли он в text
            for symbol in contains:
                # Если символ отсутствует в text, выводим сообщение об ошибке
                if symbol not in text:
                    print('Missing character')

            # Если все проверки пройдены, возвращаем результат вызова функции func с аргументом text
            return func(text)

        # Возвращаем обёрнутую функцию wrapper
        return wrapper

    # Возвращаем декоратор decorator
    return decorator


# Применяем декоратор arg_rules к функции call_func
# Указываем, что максимальная длина 25, тип str, и text должен содержать символ '@'
@arg_rules(25, str, ['@'])
def call_func(text):
    # Функция возвращает переданный аргумент text
    return text


# Вызываем функцию call_func с аргументом 'dimyantis@gmail.com'
a = call_func('dimyantis@gmail.com')
print(a)




