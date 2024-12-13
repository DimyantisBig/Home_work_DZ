import sqlite3 as sql

with sql.connect('task_2_table.db') as c:  # Подключаемся к базе данных
    cursor = c.cursor()

cursor.execute("SELECT first_name , last_name FROM employees") # Запрос на вывод И.Ф.
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT department_id FROM employees") # Идентификаторы отделов
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM employees ORDER BY first_name DESC") # Сведения о сотрудниках по имени
for row in cursor.fetchall(): # DESC с оператором ORDER BY, результаты должны быть отсортированы в порядке убывания.
    print(row)                # * выбирает все столбцы

cursor.execute("SELECT first_name , last_name , salary , (salary * 12) AS пф FROM employees") # Имена, оклад и ПФ
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT MAX(salary)AS максимальная_зарплата , MIN(salary)AS минимальная_зарплата FROM employees") #  Максимальная и минимальная зарплата
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT first_name , last_name , ROUND(salary / 12 ,2)AS зарплата_месяц FROM employees") # Месячная зарплата
for row in cursor.fetchall(): # salary / 12: Делим годовую зарплату на 12, чтобы получить месячную.
                             # ROUND(_, 2): Округляем результат до 2 знаков после запятой.
    print(row)


