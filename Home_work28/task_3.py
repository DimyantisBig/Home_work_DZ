import random

# Функция сортировки вставкой
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы, которые больше ключа, на одну позицию вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функция быстрой сортировки
def quicksort(arr, low, high, threshold):
    if high - low + 1 <= threshold:
        # Если размер списка меньше или равен порогу, используем сортировку вставкой
        insertion_sort(arr[low:high + 1])
    else:
        if low < high:
            # Получаем индекс опорного элемента
            pivot_index = partition(arr, low, high)
            # Рекурсивно сортируем элементы до и после опорного элемента
            quicksort(arr, low, pivot_index - 1, threshold)
            quicksort(arr, pivot_index + 1, high, threshold)

# Функция для разделения списка и выбора опорного элемента
def partition(arr, low, high):
    pivot = arr[high]  # Выбираем последний элемент как опорный
    i = low - 1  # Индекс меньшего элемента
    for j in range(low, high):
        # Если текущий элемент меньше или равен опорному
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами элементы
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Меняем местами элементы
    return i + 1

# Генерируем случайный список целых чисел
random_list = [random.randint(0, 100) for _ in range(20)]
print("Исходный список:", random_list)

# Определяем порог
threshold = 5

# Сортируем список
quicksort(random_list, 0, len(random_list) - 1, threshold)
print("Отсортированный список:", random_list)

"""
Разбор:
Функция insertion_sort - сортирует список вставкой.

Функция quicksort - рекурсивно сортирует список методом быстрой сортировки.

Если размер списка меньше или равен порогу threshold, используется сортировка вставкой.

В противном случае список делится на части с помощью функции partition.

Функция partition - выбирает опорный элемент и делит список на части.

Генерация случайного списка - создает список случайных целых чисел.

Порог threshold - определяет, когда использовать сортировку вставкой.

Сортировка списка - вызывает функцию quicksort для сортировки случайного списка.
"""
# --------------------------------------------------------------
"""
Быстрая сортировка
Quicksort - это рекурсивный алгоритм, который выбирает "опорный элемент" (pivot) и разбивает список 
на две части: элементы, меньшие опорного элемента, и элементы, большие опорного элемента. 
Затем он рекурсивно сортирует обе части.

Сортировка вставкой 
Insertion sort - это алгоритм сортировки, который проходит по списку и вставляет каждый элемент 
на нужное место. Он эффективен для небольших списков.
"""

"""
Важно!
Повторить!
Довольно таки не понятная тема.
"""