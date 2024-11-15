class Dog:
    age_factor = 7  #  age_factor атрибут класса Dog, общий для всех экземпляров (собак),
    def __init__(self , age):  #  Конструктор __init__() принимает параметр age
        self.age = age  #   атрибут экземпляра self.age

    def human_age (self):
        return self.age * self.age_factor


rex = Dog(2)
rex.human_age()
print(f'Rex age in human equivalent : {rex.human_age()} year old.')