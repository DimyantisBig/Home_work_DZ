import  random

list1 = []
while len(list1) < 10:
    num1 = random.randint(1, 10)
    list1.append(num1)
list2 = []
while len(list2) < 10:
    num2 = random.randint(1, 10)
    list2.append(num2)
common_list = []
i = 0
while i < len(list1):
    if list1[i] in list2 and list1[i] not in common_list:
        common_list.append(list1[i])
    i += 1
print("The first list:", list1)
print("The second list:", list2)
print("Common elements without duplicates:", common_list)

"""Импортировать модуль random:

Нужно импортировать модуль random для генерации случайных чисел.

Сгенерировать первый список:

Создайте пустой список list1.

Используйте цикл while, чтобы добавить в list1 10 случайных целых чисел от 1 до 10.

Сгенерировать второй список:

Аналогично, создайте пустой список list2.

Используйте еще один цикл while, чтобы добавить в list2 10 случайных целых чисел от 1 до 10.

Создать третий список для общих элементов:

Создайте пустой список common_list.

Используйте цикл while, чтобы пройтись по элементам list1.

Если элемент из list1 присутствует в list2 и отсутствует в common_list, добавьте его в common_list.

"""






