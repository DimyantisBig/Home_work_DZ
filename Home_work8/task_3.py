def make_operation(operator , *args): # Создали функцию где "operator" -> +/-/*,a "*args" аргумент 5,2,6 любое количество
    if operator == '+' :             #  * для обозначения любого кол-ва аргументов/ ** для любого кол-ва ключевых слов
        result = 0
        for num in args:
            result = result + num

    elif operator == '-' :
        result = args[0]
        for num in args [1:]:
            result = result - num

    elif operator == '*' :
        result = 1
        for num in args:
            result = result * num
        return result









