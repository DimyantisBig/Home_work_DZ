import requests  # Библиотека для отправки HTTP-запросов
import json      # Библиотека для работы с JSON-файлами
import time      # Библиотека для паузы между запросами

# 1. Ввод данных: выберите сабреддит
subreddit = "Python"  # Название сабреддита, например, "Python"

# 2. Формируем базовый URL для API
base_url = "https://api.pushshift.io/reddit/comment/search/"
params = {
    "subreddit": subreddit,  # Указываем сабреддит
    "size": 100,             # Количество комментариев за один запрос (максимум 100)
    "sort": "asc",           # Хронологический порядок (по возрастанию времени)
    "after": 0               # Начинаем с самого раннего времени
}

# 3. Создаем список для хранения всех комментариев
all_comments = []

while True:
    # Отправляем GET-запрос к API
    response = requests.get(base_url, params=params)
    data = response.json()  # Преобразуем ответ в JSON

    # Проверяем, есть ли комментарии в ответе
    comments = data.get("data", [])
    if not comments:
        # Если комментариев больше нет, выходим из цикла
        break

    # Добавляем комментарии в общий список
    all_comments.extend(comments)

    # Обновляем параметр "after" для следующего запроса
    # Берем время последнего комментария из текущего ответа
    params["after"] = comments[-1]["created_utc"]

    # Печатаем количество загруженных комментариев (для отслеживания процесса)
    print(f"Загружено комментариев: {len(all_comments)}")

    # Добавляем паузу между запросами, чтобы не перегружать API
    time.sleep(2)

# 4. Сохраняем все комментарии в файл JSON
output_file = f"{subreddit}_comments(task_2).json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_comments, f, ensure_ascii=False, indent=4)

print(f"Сохранено {len(all_comments)} комментариев в файл {output_file}")

"""
Подробное объяснение:

Импорт библиотек

import requests
import json
import time
requests: Для отправки HTTP-запросов.
json: Для обработки данных в формате JSON.
time: Для добавления пауз между запросами.

Выбор сабреддита

subreddit = "Python"
Это строка с названием сабреддита, из которого вы хотите загружать комментарии.

Формирование базового URL

base_url = "https://api.pushshift.io/reddit/comment/search/"
params = {
    "subreddit": subreddit,
    "size": 100,
    "sort": "asc",
    "after": 0
}
base_url: Базовый адрес для запросов к API.
params: Словарь параметров запроса:
subreddit: Название сабреддита.
size: Количество комментариев за один запрос (максимум 100).
sort: Указывает сортировку (по возрастанию времени).
after: Фильтр по времени; начнем с самого раннего (0).

Получение данных

response = requests.get(base_url, params=params)
data = response.json()
comments = data.get("data", [])
requests.get(): Отправляет запрос к API.
response.json(): Преобразует ответ сервера в формат JSON.
data.get("data", []): Извлекаем список комментариев из ответа.

Добавление комментариев в список

all_comments.extend(comments)
params["after"] = comments[-1]["created_utc"]
all_comments.extend(): Добавляет новые комментарии к общему списку.
params["after"]: Обновляет временной фильтр для следующего запроса.

Пауза между запросами

time.sleep(1)
Добавляем паузу, чтобы не перегружать сервер API.

Сохранение данных в файл

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_comments, f, ensure_ascii=False, indent=4)
open(): Открываем файл для записи.
json.dump(): Сохраняем данные в формате JSON с отступами для читабельности.
"""