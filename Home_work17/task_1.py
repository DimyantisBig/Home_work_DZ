# Определяем базовый класс Animal.
# Этот класс служит общей основой для других классов животных.
class Animal:
    def talk(self):
        # Метод talk пока не реализован, используется как шаблон для наследников.
        pass

# Определяем класс Dog, который наследуется от класса Animal.
class Dog(Animal):
    # Переопределяем метод talk для класса Dog.
    def talk(self):
        # В методе talk добавляем функционал: печать сообщения, характерного для собаки.
        print('Dog sey Wof-wof!')

# Определяем класс Cat, который также наследуется от класса Animal.
class Cat(Animal):
    # Переопределяем метод talk для класса Cat.
    def talk(self):
        # В методе talk добавляем функционал: печать сообщения, характерного для кошки.
        print('Cat sey Myau - myau!')

# Определяем функцию make_animal_talk, которая принимает объект животного.
def make_animal_talk(animal):
    # Вызываем метод talk у переданного объекта animal.
    animal.talk()

# Создаем объект класса Dog. Этот объект обладает поведением, определенным в классе Dog.
d = Dog()

# Создаем объект класса Cat. Этот объект обладает поведением, определенным в классе Cat.
c = Cat()

# Вызываем функцию make_animal_talk, передавая ей объект d (собаку).
# Функция вызывает метод talk у объекта Dog.
make_animal_talk(d)

# Вызываем функцию make_animal_talk, передавая ей объект c (кошку).
# Функция вызывает метод talk у объекта Cat.
make_animal_talk(c)

