import sqlite3

def get_email_body_from_db(template_id):
    conn = sqlite3.connect('email_templates.db')
    cursor = conn.cursor()
    cursor.execute("SELECT body FROM templates WHERE id=?", (template_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
