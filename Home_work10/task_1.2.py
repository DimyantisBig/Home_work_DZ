def oops():
    dict_1 = {'a': 1, 'b': 2}
    return dict_1['c']  # ключа 'c' нет в словаре, возникнет KeyError
try:
    oops()
except KeyError:
    print('KeyError caught!')