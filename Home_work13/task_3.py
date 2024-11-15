
num = list(range(-8, 88, 8))  # Создаём список чисел от -8 до 80 с шагом 8
def choose_func(num: list, func1, func2):   # Определяем функцию choose_func, которая принимает список чисел num и две другие функции func1 и func2
    is_positive = all(n > 0 for n in num) # Проверяем, что все числа в списке num положительные, результат проверки сохраняем в is_positive
    if is_positive == True: # Если is_positive равно True (все числа положительные)
       return func1(num) # Возвращаем результат вызова функции func1, передавая ей num
    else:
        return func2(num) # Иначе возвращаем результат вызова функции func2, передавая ей num

# Определяем первую функцию call_func, которая принимает список num
def call_func1(num):
    print('All numbers are positive:')
    # Возвращаем сам список num
    return num

# Определяем вторую функцию call_func_2, которая также принимает список num
def call_func_2(num):
    print('There are negative numbers:')
    return num

# Вызов функции choose_func с аргументами: список num, функция call_func и функция call_func_2
result = choose_func(num, call_func1, call_func_2)
print('Result:', result)

