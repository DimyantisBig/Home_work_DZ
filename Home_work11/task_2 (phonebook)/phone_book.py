import json  # Для работы с JSON-файлами
import os  # Для проверки существования файла
import sys  # Для получения аргументов командной строки

# Проверяем, передано ли название файла в аргументах
if len(sys.argv) < 2:
    print("Ошибка: Укажите имя файла телефонной книги.")
    sys.exit(1)  # Завершаем программу с кодом ошибки

# Получаем имя файла из аргументов
filename = sys.argv[1]

# Загружаем данные из файла, если он существует
if os.path.exists(filename):
    with open(filename, 'r') as file:
        phonebook = json.load(file)  # Загружаем данные JSON в переменную phonebook
else:
    print("Файл не найден. Убедитесь, что телефонная книга существует.")
    sys.exit(1)  # Завершаем программу, если файла нет


# Функция для добавления нового контакта
def add_contact(phonebook):
    """
    Добавляет новый контакт в телефонную книгу.
    """
    # Запрашиваем данные у пользователя
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    city = input("Введите город: ")
    state = input("Введите штат: ")

    # Создаем словарь для нового контакта
    contact = {
        "name": name,
        "surname": surname,
        "phone": phone,
        "city": city,
        "state": state
    }

    # Добавляем новый контакт в список phonebook
    phonebook.append(contact)
    print("Контакт добавлен.")  # Сообщаем, что контакт успешно добавлен


# Функция для поиска контактов
def search_contact(phonebook):
    """
    Ищет контакты по указанному полю.
    """
    # Запрашиваем, по какому критерию искать
    criterion = input("По какому полю искать (name, surname, phone, city, state): ")
    value = input(f"Введите значение для поиска по '{criterion}': ")

    # Ищем контакты, которые соответствуют введенному критерию
    results = [c for c in phonebook if c.get(criterion) == value]

    # Если результаты найдены, выводим их
    if results:
        print("Найденные контакты:")
        for contact in results:
            print(contact)  # Выводим каждый найденный контакт
    else:
        print("Контакты не найдены.")  # Если ничего не найдено


# Функция для удаления контакта
def delete_contact(phonebook):
    """
    Удаляет контакт по номеру телефона.
    """
    # Запрашиваем номер телефона для удаления
    phone = input("Введите номер телефона для удаления: ")

    # Фильтруем список, исключая контакт с указанным номером телефона
    initial_length = len(phonebook)  # Сохраняем начальное количество контактов
    phonebook[:] = [c for c in phonebook if c.get("phone") != phone]

    # Проверяем, изменился ли список
    if len(phonebook) < initial_length:
        print("Контакт удален.")  # Контакт удален
    else:
        print("Контакт с таким номером не найден.")  # Контакт не найден


# Функция для обновления контакта
def update_contact(phonebook):
    """
    Обновляет данные контакта по номеру телефона.
    """
    # Запрашиваем номер телефона для обновления
    phone = input("Введите номер телефона для обновления: ")

    # Ищем контакт с указанным номером телефона
    for contact in phonebook:
        if contact.get("phone") == phone:
            print("Что вы хотите обновить?")
            # Запрашиваем обновленные данные. Если пользователь ничего не вводит, сохраняем старое значение
            contact["name"] = input("Новое имя: ") or contact["name"]
            contact["surname"] = input("Новая фамилия: ") or contact["surname"]
            contact["city"] = input("Новый город: ") or contact["city"]
            contact["state"] = input("Новый штат: ") or contact["state"]
            print("Контакт обновлен.")  # Сообщаем об успешном обновлении
            return
    # Если контакт не найден, выводим сообщение
    print("Контакт с таким номером не найден.")


# Основной цикл программы
while True:
    # Выводим меню для пользователя
    print("\nТелефонная книга")
    print("1. Добавить запись")
    print("2. Найти запись")
    print("3. Удалить запись")
    print("4. Обновить запись")
    print("5. Выйти")

    # Запрашиваем выбор действия
    choice = input("Выберите действие: ")

    # Выполняем действие в зависимости от выбора
    if choice == "1":
        add_contact(phonebook)  # Добавляем контакт
    elif choice == "2":
        search_contact(phonebook)  # Ищем контакт
    elif choice == "3":
        delete_contact(phonebook)  # Удаляем контакт
    elif choice == "4":
        update_contact(phonebook)  # Обновляем контакт
    elif choice == "5":
        # Сохраняем данные в файл при выходе
        with open(filename, 'w') as file:
            json.dump(phonebook, file, indent=4)  # Записываем JSON с отступами
        print("Данные сохранены. До свидания!")  # Сообщаем о сохранении и выходим
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")  # Обрабатываем некорректный ввод
