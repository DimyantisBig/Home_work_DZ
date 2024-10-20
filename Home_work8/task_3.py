def make_operation(operator , *args):
    if operator == '+' :
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









