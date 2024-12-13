import sqlite3 as sql

with sql.connect('task_1_table.db') as conn:
    cursor = conn.cursor()

    # Создаём таблицу, если она ещё не существует
    cursor.execute("""CREATE TABLE IF NOT EXISTS task_1 (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    phone INTEGER NOT NULL,
    work TEXT)""")

    # Добавляем новые столбцы
    cursor.execute("ALTER TABLE task_1 ADD COLUMN email TEXT")
    cursor.execute("ALTER TABLE task_1 ADD COLUMN profession TEXT")

    # Обновляем данные в столбце work
    cursor.execute("UPDATE task_1 SET work = 'seller' WHERE user_id = 2")

    # Удаляем строку с id = 4
    cursor.execute("DELETE FROM task_1 WHERE user_id = 4")


