def in_range (start, stop, step): # Определение функции:
    current = start  # Инициализация переменной:
    while current < stop: # Цикл для генерации последовательности:
        yield current
        current += step

"""
Цикл while: Продолжает работать, пока current меньше end.
yield: Вместо того, чтобы возвращать весь список сразу, мы используем yield, чтобы сделать нашу функцию генератором. 
Это позволяет нам генерировать значения по одному при каждой итерации цикла, что более эффективно для больших последовательностей.
Обновление current: После каждого yield мы увеличиваем current на step.
"""

# Пример использования

for num in in_range(1, 20, 2):
    print(num)