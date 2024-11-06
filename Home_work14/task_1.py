
def print_operation (func): # Сам декоратор
    def wrapper (*args , **kwargs):  # Функция обертка что оборачивает вызываемую функцию

        print('Function',func.__name__) # Что должна выводить вызывыемая функция
        print('Argument', args )
        print('Key word argument' , kwargs)
    return wrapper

@print_operation
def call_func ():   # Вызываемая функция
    print('Original function is called')

call_func ()

