import sqlite3 as sql

with sql.connect('task_2_table.db') as conn:  # Подключаемся к базе данных
    cursor = conn.cursor()

cursor.execute("SELECT first_name AS 'First Name',last_name AS 'Last Name' "
               "FROM employees")
for row in cursor.fetchall():
    print(row)