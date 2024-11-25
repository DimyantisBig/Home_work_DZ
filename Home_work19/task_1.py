def with_index(iterable, start):
    """
    Функция, имитирующая поведение встроенной функции enumerate.

    Args:
        iterable: Итерируемый объект.
        start: Начальное значение индекса.

    Yields:
        Кортеж из индекса и соответствующего элемента из iterable.
    """

    index = start
    for item in iterable:
        yield index, item
        index += 1

# Пример работы функции

my_list = ['apple', 'banana', 'cherry']
"""
    index, fruit: Здесь мы распаковываем возвращаемые значения функции with_index в две переменные: 
    index (индекс) и fruit (элемент списка)
"""
for index, fruit in with_index(my_list, start=1):
    """
    Вызов нашей пользовательской функции with_index. 
    Мы передаем ей список my_list и указываем, что отсчет индексов нужно начинать с 1 (параметр start=1). 
    Функция with_index возвращает генератор, который будет последовательно выдавать кортежи 
    из индекса и соответствующего элемента списка.
    """
    print(f"Индекс: {index}, Фрукт: {fruit}")
