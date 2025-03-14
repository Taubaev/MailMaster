import sqlite3

def insert_template(name, body):
    conn = sqlite3.connect('email_templates.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO templates (name, body)
        VALUES (?, ?)
    ''', (name, body))  # Добавляем шаблон в базу
    conn.commit()
    conn.close()

# Пример добавления шаблона
