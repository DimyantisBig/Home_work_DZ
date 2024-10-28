import  sys

new_path = 'C:\\Users\\dimya\\Desktop\\new_path_example'
sys.path.append(new_path)

import test_module

test_module.hello()

print('Список sys.path после добавления нового пути:')
print(sys.path)


