class Person:  # создаем класс
    def __init__(self,first_name, last_name, age): # метод
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk (self):
        print(f'Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old')


person1 = Person ('Lezhana', 'Razdvinogova', 33) # Создаем объект класса Person

person1.talk () # Вызываем метод talk для объекта person1
