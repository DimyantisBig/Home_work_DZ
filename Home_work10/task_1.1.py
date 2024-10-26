from task_1 import oops

try:
    oops()
except IndexError:
    print('Error,try again!')
except KeyError:
    print('Error,try again!')
