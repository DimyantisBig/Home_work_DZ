def first_func ():
    def second_func ():
        print('Hello my dear friend , this is inner function. ')
    return  second_func  # Возвращаем саму функцию, без вызова

                           # Вызовем внутреннюю функцию через переменную
call_func = first_func ()  # Здесь получаем функцию second_func
call_func ()               # А тут вызываем её


