import random
num = random.randint(1,10)
num_1 = input('Enter a number from 1 to 10: ')
if int(num_1) == num:
    print('You got it!')
else:
    print('Sorry, that is not correct.')