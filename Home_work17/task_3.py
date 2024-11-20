class Fraction:
    def __init__(self, numerator, denominator):
        # Проверяем, что знаменатель не равен нулю
        if denominator == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")
        self.numerator = numerator  # Сохраняем числитель
        self.denominator = denominator  # Сохраняем знаменатель
        self._reduce()  # Сокращаем дробь при создании объекта

    def _reduce(self):
        # Находим наибольший общий делитель (НОД)
        gcd = self.gcd(self.numerator, self.denominator)
        # Делим числитель и знаменатель на НОД для сокращения дроби
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod  # Используется для определения статического метода внутри класса.
    def gcd(a, b):
        # Используем алгоритм Евклида для нахождения НОД
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        # Возвращаем строковое представление дроби
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        # Сложение двух дробей
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)  # Возвращаем новый объект Fraction

    def __sub__(self, other):
        # Вычитание двух дробей
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)  # Возвращаем новый объект Fraction

    def __mul__(self, other):
        # Умножение двух дробей
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)  # Возвращаем новый объект Fraction

    def __truediv__(self, other):
        # Деление двух дробей
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        if new_denominator == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")
        return Fraction(new_numerator, new_denominator)  # Возвращаем новый объект Fraction

    def __eq__(self, other):
        # Проверка на равенство двух дробей
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        # Проверка, меньше ли одна дробь другой
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        # Проверка, меньше или равно ли одна дробь другой
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        # Проверка, больше ли одна дробь другой
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        # Проверка, больше или равно ли одна дробь другой
        return self.numerator * other.denominator >= other.numerator * self.denominator

