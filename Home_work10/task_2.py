def my_func():
    try:
        a = int(input('Enter first number:')) # Переменные a и b теперь вводятся внутри блока try,
        b = int(input('Enter second number:')) # чтобы сразу поймать ошибку, если пользователь введет не числа.
        result = (a**2) / b                   # Операция (a ** 2) / b сохраняется в переменную result.
        return result                        # Если ошибок не произошло, результат возвращается функцией через return.
    except ValueError:                      # except: Если будет введен неверный тип данных или
        print('Incorrect data')
    except ZeroDivisionError:            # будет попытка деления на ноль, соответствующие сообщения об ошибках выведутся.
        print('You can not divide by zero!')



