import unittest
from task_1 import MyOpen


class TestMyOpen(unittest.TestCase):

    def test_open_and_close(self):
        # Тестируем открытие и закрытие файла
        with MyOpen('testfile.txt', 'w') as file:
            self.assertEqual(file.filename, 'testfile.txt')
            self.assertEqual(file.mode, 'w')
            self.assertIn("Открыт файл testfile.txt в режиме w", file.log)

        # Проверяем логи после выхода из контекста
        self.assertIn("Закрыт файл testfile.txt", file.log)

    def test_exception_handling(self):
        # Тестируем обработку исключений
        try:
            with MyOpen('testfile.txt', 'r') as file:
                raise ValueError("Test exception")
        except ValueError:
            pass

        # Проверяем, что исключение было записано в лог
        self.assertIn("Исключение: <class 'ValueError'>, Test exception", file.log)


if __name__ == '__main__':
    unittest.main()
