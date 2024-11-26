class Name:
    # Метод для получения полного имени
    def full_name(self, first_name, last_name):
        f_name = first_name.title() + ' ' + last_name.title()
        return f_name

    # Метод для получения инициалов
    def initials(self, first_name, last_name):
        initials = first_name[0].upper() + '.' + last_name[0].upper() + '.'
        return initials

# Создаем экземпляр класса Name
name_instance = Name()

# Вызываем метод full_name и передаем необходимые аргументы
full_name_result = name_instance.full_name("сидр" , "вальериянович")
print("Полное имя:", full_name_result)

# Вызываем метод initials и передаем необходимые аргументы
initials_result = name_instance.initials("сидр", "вальериянович")
print("Инициалы:", initials_result)





