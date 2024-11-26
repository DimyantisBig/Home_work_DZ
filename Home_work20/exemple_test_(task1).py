import unittest
from task_1 import Name

class TestName(unittest.TestCase):
    """
    Класс для тестирования методов класса Name.
    """

    def setUp(self):
        """
        Метод, который вызывается перед каждым тестом.
        Создаём экземпляр класса Name.
        """
        self.name = Name()

    def test_full_name(self):
        """
        Тестируем метод full_name.
        """
        result = self.name.full_name("сидр", "валериянович")
        self.assertEqual(result, "Сидр Валериянович")

        result = self.name.full_name("сИДр", "ВалЕРияНовиЧ")
        self.assertEqual(result, "Сидр Валериянович")

    def test_initials(self):
        """
        Тестируем метод initials.
        """
        result = self.name.initials("вахлак", "вахлакович")
        self.assertEqual(result, "В.В.")

        result = self.name.initials("ВаЛак", "вАХЛАКОВИЧ")
        self.assertEqual(result, "В.В.")

    def test_full_name_empty_input(self):
        """
        Проверяем метод full_name с пустыми строками.
        """
        result = self.name.full_name("", "")
        self.assertEqual(result, " ")

    def test_initials_empty_input(self):
        """
        Проверяем метод initials с пустыми строками.
        """
        with self.assertRaises(IndexError):  # Ожидаем ошибку IndexError
            self.name.initials("", "") # Если передать пустые строки в initials,
                                                         # ожидаем, что возникнет ошибка IndexError,
                                                        # так как доступ к первому символу невозможен.
