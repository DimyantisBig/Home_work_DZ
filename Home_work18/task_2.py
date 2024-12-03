class Boss:
    def __init__(self):
        self.workers = []  # Инициализация пустого списка работников

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)  # Добавление работника в список, если он является экземпляром класса Worker
        else:
            raise ValueError("worker must be an instance of Worker")  # Исключение, если worker не является экземпляром класса Worker

class Worker:
    def __init__(self, boss=None):
        self._boss = None  # Инициализация приватного атрибута _boss
        self.boss = boss  # Установка значения для атрибута boss через сеттер

    @property
    def boss(self):
        return self._boss  # Возвращает значение приватного атрибута _boss

    @boss.setter
    def boss(self, new_boss):
        if new_boss is None or isinstance(new_boss,
                                          Boss):  # Проверка, что new_boss является либо None, либо экземпляром класса Boss
            self._boss = new_boss  # Установка значения для приватного атрибута _boss
            if new_boss is not None and self not in new_boss.workers:
                new_boss.add_worker(self)  # Добавление текущего работника в список работников нового босса
        else:
            raise ValueError(
                "boss must be an instance of Boss")  # Исключение, если new_boss не является экземпляром класса Boss


# Использования и тестирования
boss1 = Boss()  # Создание нового экземпляра класса Boss
worker1 = Worker(boss1)  # Создание нового экземпляра класса Worker и назначение ему босса boss1
worker2 = Worker()  # Создание нового экземпляра класса Worker без начальника (boss=None)

print(worker1.boss == boss1)  # True - проверка, что bосс у worker1 равен boss1
print(len(boss1.workers))  # 1 - проверка количества работников у boss1
print(boss1.workers[0] == worker1)  # True - проверка, что первый работник в списке работников boss1 равен worker1

worker2.boss = boss1  # Назначение босса boss1 для worker2
print(worker2.boss == boss1)  # True - проверка, что bосс у worker2 равен boss1
print(len(boss1.workers))  # 2 - проверка количества работников у boss1
print(boss1.workers[1] == worker2)  # True - проверка, что второй работник в списке работников boss1 равен worker2

"""
Сложная тема,требует повтор!
Детальный разбор задачи --> G:\Мой диск\Обучение\Beetroot Academy\Информация
"""
