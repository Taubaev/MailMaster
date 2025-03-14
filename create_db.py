import sqlite3

def create_db():
    conn = sqlite3.connect('email_templates.db')  # Создаем базу данных
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            body TEXT NOT NULL
        )
    ''')  # Создаем таблицу для шаблонов
    conn.commit()
    conn.close()


