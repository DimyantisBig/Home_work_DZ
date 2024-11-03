def local_var ():
    var_one = 'Hello'
    var_two = 'my'
    var_three = 'friend!'
    return len(locals())


result = local_var()
print('Quantity local variable -->' , result)

"""
Создал функцию local_var, внутри которой объявил три локальные переменные: 
var_one, var_two и var_three.
Затем  использовал len(locals()), чтобы посчитать количество локальных переменных. 
locals() возвращает словарь локальных переменных, 
и len(locals()) возвращает количество ключей в этом словаре, 
что соответствует числу локальных переменных.
В конце  присвоил результат переменной result и вывел его с помощью print(result).
"""

