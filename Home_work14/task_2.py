def test_text(*args):  # Внешняя функция, принимает список стоп-слов
    def decorator(func):  # Средняя функция — сам декоратор
        def wrapper(text):  # Внутренняя функция — обертка для обработки текста
            for word in args:  # Заменяем каждое стоп-слово в тексте на звёздочки
                text = text.replace(word, '*' , len(word))
            return text  # Возвращаем обработанный текст после обработки всех стоп-слов
        return wrapper  # Возвращаем обертку
    return decorator  # Возвращаем декоратор


# Использование - вызов
@test_text('and', 'the', 'is', 'in', 'on', 'with', 'for', 'when', 'where')
def get_txt(text):
    return text


result = get_txt('And the time is in the friend on with you!')
print(result)


