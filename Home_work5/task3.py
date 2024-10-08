import random
import string

text = input('Write you word:')
for _ in range(5):
    random_word = ''.join(random.choice(text) for _ in range(len(text)))
    print(random_word)

"""
for _ in range(5):: Это цикл, который выполняется 5 раз.
 _ используется как имя переменной, когда её значение не нужно.

random_string = ''.join(random.choice(text) for _ in range(len(text))):

random.choice(text): Выбирает случайный символ из строки text.
for _ in range(len(text)): Здесь мы указываем, сколько символов нужно выбрать. 
Мы выбираем столько символов, сколько в введённой строке.
''.join(...): Эта часть объединяет все выбранные символы в одну строку.
print(random_string): Выводим сгенерированную строку на экран.
"""