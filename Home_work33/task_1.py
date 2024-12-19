import requests

# Функция для скачивания файла robots.txt
def download_robots_txt(url, filename):
    # Выполнение HTTP GET-запроса
    response = requests.get(url)

    # Проверка статуса ответа (200 означает успех)
    if response.status_code == 200:
        # Открытие файла для записи в бинарном режиме
        with open(filename, 'wb') as file:
            # Запись содержимого ответа в файл
            file.write(response.content)
        print(f'Файл {filename} успешно скачан и сохранен.')
    else:
        print(f'Ошибка {response.status_code}: не удалось скачать файл {filename}.')


# URL-адреса для Wikipedia и Twitter
wikipedia_url = 'https://en.wikipedia.org/robots.txt'
twitter_url = 'https://twitter.com/robots.txt'

# Скачивание и сохранение файлов robots.txt
download_robots_txt(wikipedia_url, 'wikipedia_robots(task_1).txt')
download_robots_txt(twitter_url, 'twitter_robots(task_1).txt')

"""
Подробное объяснение:

import requests
Эта строка импортирует библиотеку requests, которая позволяет выполнять HTTP-запросы.

Определение функции download_robots_txt:

def download_robots_txt(url, filename):
Эта строка объявляет функцию download_robots_txt, которая принимает два аргумента: url (адрес, откуда нужно скачать файл) и filename (имя файла, в который нужно сохранить скачанное содержимое).

Выполнение HTTP GET-запроса:

response = requests.get(url)
Эта строка выполняет HTTP GET-запрос к указанному URL-адресу и сохраняет ответ в переменной response.

Проверка статуса ответа:

if response.status_code == 200:
Эта строка проверяет, успешен ли запрос. Код состояния 200 означает, что запрос был выполнен успешно.

Открытие файла для записи:

with open(filename, 'wb') as file:
Эта строка открывает файл для записи в бинарном режиме ('wb' означает 'write binary') и сохраняет ссылку на файл в переменной file.

Запись содержимого ответа в файл:

file.write(response.content)
Эта строка записывает содержимое ответа (файл robots.txt) в открытый файл.

Вывод сообщения об успешном скачивании:

print(f'Файл {filename} успешно скачан и сохранен.')
Эта строка выводит сообщение в консоль о том, что файл был успешно скачан и сохранен.

Обработка ошибки:

else:
    print(f'Ошибка {response.status_code}: не удалось скачать файл {filename}.')
Если статус ответа не 200, выводится сообщение об ошибке с указанием кода ошибки.

Применение функции для Wikipedia и Twitter:
URL-адреса для Wikipedia и Twitter:

wikipedia_url = 'https://en.wikipedia.org/robots.txt'
twitter_url = 'https://twitter.com/robots.txt'
Эти строки задают URL-адреса для скачивания файлов robots.txt с Wikipedia и Twitter.

Вызов функции для скачивания и сохранения файлов:

download_robots_txt(wikipedia_url, 'wikipedia_robots.txt')
download_robots_txt(twitter_url, 'twitter_robots.txt')
Эти строки вызывают функцию download_robots_txt для скачивания и сохранения файлов robots.txtиз Wikipedia и Twitter.
"""