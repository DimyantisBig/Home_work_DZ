def bubble_sort_bidirectional(arr):
  """Сортировка пузырьком в обоих направлениях.

  Args:
    arr: Список для сортировки.

  Returns:
    Отсортированный список.
  """

  n = len(arr) # Определяет длину списка.
  swapped = True # Флаг, указывающий, были ли произведены какие-либо перестановки на текущем проходе.
  start, end = 0, n-1 # Указатели начала и конца области, которую нужно сортировать.

  while swapped:
    swapped = False # Основной цикл продолжается до тех пор, пока происходит хотя бы одна перестановка.

    # Движение "вверх"
    for i in range(start, end):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        swapped = True
    end -= 1

    # Если список уже отсортирован, то цикл прервется

    if not swapped:
      break

    swapped = False

    # Движение "вниз"
    for i in range(end-1, start-1, -1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        swapped = True
    start += 1

  return arr

# Пример использования
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort_bidirectional(my_list)
print(sorted_list)

"""
Важно!
Тема алгоритмы сложная.Требуется повторение!!!
"""